from ij import IJ #demonstrated in examples

#modules.clear() 
#this was causing os.path to fail down the line - it depends on sys.modules. reordered.

#using sys instead of os here because it works. os is more sys-agnostic but is throwing rarefied errors
from sys import modules #standard, includes sys.path #sys.path is an all-star for OS io. print/insert sys.path very useful
import sys.path #depends on sys.modules
#insert is not permanent without an export (temp mods to sys.path)
sys.path.insert(0, 'C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\scq') #work path

#sys.path.insert(0, 'C:\\Users\\Owner\\Documents\\SO\\scq')
import get_ilastik_unique_cells_locations 
import get_intensity_per_cell
from ij.io import FileSaver #works
from java.util import ArrayList #standard
from array import array, zeros #standard
import os
#import pickle 
#file extension is necessary or filenotfound exception
#escaping backslash necessary or compiler will modify
#sorted_enumerated_list=get_ilastik_unique_cells_locations('C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\WellA02_Tracking-Results\\','WellA02_ChannelFITC,mCherry_Seq0001__Tracking-Result__00.tif')
import itertools
print 'imports'
print os.path
#home testing os.getcwd() > C:\Program Files (x86)\fiji-win64\Fiji.app
#os.path.abspath
#check this out - if there is a trailing \, even in a raw string,
#it will escape the character after it (i.e. goodbye closing quote)

#trackDir = r'C:\Users\Owner\Documents\SO\scq\WellA02_Tracking-Results\\'
#rawDir = r'C:\Users\Owner\Documents\SO\scq\WellA02_gfp\\'

#work testing
#this needs you to spell out T I F F and escape '\'
#trackDir = "C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\WellA02_Tracking-Results\\" 

#trackName = "WellA02_ChannelFITC,mCherry_Seq0001__Tracking-Result__00.tif"
#trackPath = trackDir+trackName
#C:\Users\davidsonk2\OneDrive - UPMC\Documents\Ilastik\WellA02_gfp
#rawDir = "C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\WellA02_gfp\\"
#rawName = 'WellA02_ChannelFITC,mCherry_Seq0001_00.tif'
#rawPath = rawDir + rawName
#in pixels. This allows get intensity to do it's thing without maxing out memory. 
#in a 32 bit 3072x3072 bit tiff, the 926 masks have a maximum width under 100 
#intensityByCell is solely for lineage averages and identity is by index.
def scq(rawPath, trackPath, intensityByCell):
	maximumCellSize = 100
	maximumCellOccupancy1D = 100*3072
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

'''
if os.path.exists(objectivePath):
	print "exists"
else:
	print "file doesn't exist"

objectivePath = os.path.dirname(os.path.abspath(imagePath)) 
this returns the path C:\Java\Fiji.app
'''




#fs = FileSaver(image)
#if os.path.exists(output_folder):
#	print 'output dir exists!'
#else:
#	print "output location failed"


	'''
