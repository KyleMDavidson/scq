from java.util import ArrayList
from array import array, zeros
#from itertools import groupby
import os
import sys
from ij import IJ

	#this recieves the imageDir and imageName of the raw images
def sort_intensities_on_lineage(enumeratedTrackPixels, rawPixels):
	#enumeratedTrack pixels : (index, then cellID).  maskAndRaw = [ index, cellID, rawPixelValue ] 
	maskAndRaw = zip([set[0] for set in enumeratedTrackPixels], [set[1] for set in enumeratedTrackPixels], rawPixels)
	sortedMaskAndRaw = sorted(maskAndRaw, key=lambda x:x[1])  # proven MVP sort lambda. return sorted on cellID.
	backgroundPixels = 0
	print 'first entry: ' + str(sortedMaskAndRaw[0])
	print 'last entry: ' + str(sortedMaskAndRaw[len(sortedMaskAndRaw)-1]) #both as expected
	for entry in sortedMaskAndRaw:
		if entry[1] == 0:
			backgroundPixels = backgroundPixels+1

	#print ' total pixels processed: ' + str(len(sortedMaskAndRaw))
	#print ' background pixels removed : ' + str(backgroundPixels)
	#print ' pixels being passed on: ' + str(len(sortedMaskAndRaw[backgroundPixels:])) 
	'''this should return
 first entry: (2, 0.0, 179.0)
 last entry: (9434783, 1309.0, 625.0)
 total pixels processed: 9437184
 background pixels removed : 9313495
 pixels being passed on: 123689
 for A02 00 #passing 0319
'''
	return sortedMaskAndRaw[backgroundPixels:] #this is correct. backgroundPixels-1 returns 0 value. (despite 1 being missing)
	
	#preIntensityByCell [ index, cellID, rawPixelValue] sorted on cellID from sort_intensities_on_lineage
	#this excludes all pixels with value = 0 (background)
	#memory use is far less than average lineage intensity (easily handles entire images). No need to block this.
def average_lineage_intensity(preIntensityByCell):
	#0319 itertools rewrite (no strings) still a lockout - this maxes out memory use. (93-97%) 
	#0319 standard arrays rewrite but with subsetting: this entirely processes 100 cells at a time - this hits about 50% memory within five minutes
	#and continues to rise after that.
	#this was logical.
	#blockedPreIntensityByCell = []
	#blockIndex = 0 #also in cells
	#blockSize = 100 #this needs to be in cells (and here, it is!) 
	#lineages start @ 1 (background removed)
	#access lineage @ [1] in PIBC
	#preIntensityByCell = preIntensityByCell[1:100] #testing subset
	currentCell = []
	averageIntensityByCell = []
	cellIDs = []
	currentCellPixelCount = 0
	#iterate through PIBC for each cellID, adding cell intensities and then averaging upon new cell
	currentCellID = preIntensityByCell[0][1]
	cellIDs.append(currentCellID)
	intensitySum=0
	i=0
	for cell in preIntensityByCell:
		print currentCell,' ', cell[1]
		if  cell[1] == currentCellID:   # first cell will always match (if there is a cell)
			#print 'lineage, intensity: ' + str(cell[1]) +', '+str(cell[2])
			currentCell.append(cell[2]) # append intensity
			currentCellPixelCount = currentCellPixelCount + 1 #increment divisor
		else:
			cellIDs.append(cell[1])
			averageIntensity = sum(currentCell) / len(currentCell)
			averageIntensityByCell.append(averageIntensity) 
			
			currentCell = []  # empty currentCell after calculations
			currentCell.append (cell[2])	# add the first new cell intensity
			currentCellPixelCount = 1  # reset the pixel count for the new cells

	averageIntensity = sum(currentCell) / len(currentCell) # the last cell will never match
	averageIntensityByCell.append(averageIntensity) 
	cellIDs.append(currentCellID)
	averageIntensityByCell.append(averageIntensity)
	
	return averageIntensityByCell
	
#   append blocks to below and compute
#	lineages = max([set[1] for set in preIntensityByCell])
#	cellAverageIntensities = []
			
	#recombine the blocks into one list -> averages
	#list(chain(odd, even)) can make one list out of all the blocks of cells

#			for pixel in preIntensityByCell:	
	#for cell, pixel in itertools.groupby(preIntensityByCell, lambda x:x[1]):
	#	for intensity in pixel:	
	#		currentSum += intensity
	#	cellAverageIntensities.append(currentSum)
	#	currentSum = 0

	
	
		# sorted on cellID. [index, cellID, rawPixelValue]
	#for set, member in groupby( preIntensityByCell, lambda x:x[1]):
	#	cells.append(list(set[3])) #stores group iterator as a list
	#	print 'list(cell): ' + list(set[3])
		
		
		#curr_lineage_intensity_sum = curr_lineage_intensity_sum + preIntensityByCell[pixel]
		#curr_average = curr_average + preIntensityByCell[3]
		#curr_lineage = preIntensityByCell
		
	#itertools approach	(very slow 0318) # possibly due to string processing?
	#for cell, intensity in groupby((preIntensityByCell), lambda x: x[2]):
	#	print('cell: ' + str(cell) + ' intensity: '+ str(intensity))

	#def average intensities - non-itertools approach. Slow as heck.
	#for i in range(int(lineages)): #lineages is a float.
	#	print lineages
	#	print 'index:' + str(i)
	#	for pixelTuple in preIntensityByCell:
	#		print pixelTuple
	#		currentSum = currentSum + pixelTuple[2]
	#		pixelsInLineage = pixelsInLineage+1
	#		cellAverageIntensities.append(currentSum / pixelsInLineage)
	#	print 'lineage average intensity: ' + str(cellAverageIntensities[i])
	
	