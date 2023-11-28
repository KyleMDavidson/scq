#this is an outer wrapper
#apply singlecell quant to single images 
#save the results in an array of [cell ID, average intensity, time]
from sys import modules #standard, includes sys.path #sys.path is an all-star for OS io. print/insert sys.path very useful
import sys.modules
import sys.path #depends on sys.modules #insert is not permanent without an export (temp mods to sys.path)
import os.path
homepath = 'directory_with_images_path_here'
outputPath = 'path_to_output_file_here'
sys.path.insert(0, homepath)
print sys.path
import ilastik_singlecell_quant
import average_intensity_change
import csv
from array import zeros
from ij import IJ
from datetime import datetime

def scq_stack(raw_names, track_names):
	rawPaths = []
	trackPaths = []
	for track in track_names:
		trackPath = trackDir + '\\' + track
		trackPaths.append(trackPath)
	for raw in raw_names:
		rawPath = rawDir + '\\' + raw
		rawPaths.append(rawPath)
	maxLineages = 0 
	for track in trackPaths: # passing 0402
		trackImage = IJ.openImage(track)
		trackImp = trackImage.getProcessor().convertToFloat()
		trackPixels = trackImp.getPixels()
		for pixel in trackPixels:
			if pixel > maxLineages:
				maxLineages = int(pixel)
				
	print 'maxLineages: ' + str(maxLineages) # passing 0402
	tracks = len(trackPaths)

	IBCBT = []
	for imagePair in zip(trackPaths,rawPaths):
		intensityByCell = ilastik_singlecell_quant.scq(imagePair[1], imagePair[0], [0]*maxLineages) #raw, track, IBC
		IBCBT.append(intensityByCell) 
	return IBCBT # list (t dimension) of lists (cell dimension) of average cell intensity

raw_names = os.listdir(rawDir)
track_names = os.listdir(trackDir)

# list (t dimension) of lists (cell dimension) of average cell intensity #R naturally takes None as NA. No coercion needed. 
intensityByCellByTime = scq_stack(raw_names, track_names) 

#writes to a static filename here.
with open (outputPath) as csvfile:
	IBCBTwriter = csvfile.writer(csvfile, delimiter = ',')
	for row in intensityByCellByTime: # each of these is being written as a value
		IBCBTwriter.writerow(row)
		
print 'finished and wrote'
