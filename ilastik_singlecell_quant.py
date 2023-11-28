from ij import IJ #demonstrated in examples

from sys import modules 
import sys.path 
#insert is not permanent without an export (temp mods to sys.path)
path_to_images_dir = 'your_path_here'
sys.path.insert(0, path_to_images_dir)

import get_ilastik_unique_cells_locations 
import get_intensity_per_cell
from ij.io import FileSaver #works
from java.util import ArrayList #standard
from array import array, zeros #standard
import os

import itertools
print 'imports'
print os.path


def scq(rawPath, trackPath, intensityByCell, maximumCellSize):
	maximumCellOccupancy1D = 100*307
	# Grab the image processor with data converted to float values (an easy type), then get pixels from it.
	rawImage=IJ.openImage(rawPath)
	rawImp = rawImage.getProcessor().convertToFloat()
	rawPixels = rawImp.getPixels()
	# Ditto as above but for the masks
	trackImage=IJ.openImage(trackPath)
	trackImp = trackImage.getProcessor().convertToFloat()
	trackPixels = trackImp.getPixels()
	#get indexed lineages by pixel and get their intensities in the mask
	#trackPixels = trackPixels[1:200] # testing subset 0322
	enumeratedTrackPixels = get_ilastik_unique_cells_locations.get_ilastik_unique_cells_locations(trackPixels)
	preIntensityByCell = get_intensity_per_cell.sort_intensities_on_lineage(enumeratedTrackPixels, rawPixels)
	intensityByCell = get_intensity_per_cell.average_lineage_intensity2(preIntensityByCell, intensityByCell) #0402 major rewrite - static rectangular stack processing

	if intensityByCell is None:
		print 'null IBC' 
	return intensityByCell



