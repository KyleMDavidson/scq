from java.util import ArrayList
from array import array, zeros
import os
import sys
from ij import IJ

	#this recieves the imageDir and imageName of the raw images
def sort_intensities_on_lineage(enumeratedTrackPixels, rawPixels):
	#enumeratedTrack pixels : (index, then cellID).  maskAndRaw = [ index, cellID, rawPixelValue ] 
	maskAndRaw = zip([set[0] for set in enumeratedTrackPixels], [set[1] for set in enumeratedTrackPixels], rawPixels)
	sortedMaskAndRaw = sorted(maskAndRaw, key=lambda x:x[1])  # proven MVP sort lambda. return sorted on cellID.
	backgroundPixels = 0
	for entry in sortedMaskAndRaw:
		if entry[1] == 0:
			backgroundPixels = backgroundPixels+1
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
	averageIntensityByCell = zip(cellIDs, averageIntensityByCell)
	
	return averageIntensityByCell
	
#preIntensityByCell [ index, cellID, rawPixelValue] sorted on cellID from sort_intensities_on_lineage, excludes non-cell pixels.
#iterate through PIBC for each cellID, adding cell intensities and then averaging upon new cell
# 0402 major rewrite - rectangular, final array as an argument, index by cellID
#PIBC going in with 1309 cells expected across the test stack 0402
def average_lineage_intensity2(preIntensityByCell, intensityByCell):
	currentCellPixelCount = 0
	currentCellID = preIntensityByCell[0][1]
	intensitySum=0
	currentCell = []
	for cell in preIntensityByCell:
		#if cell[1]>1300:
		if  cell[1] == currentCellID:   # first cell will always match (if there is a cell)
			currentCell.append(cell[2]) 
		else:
			averageIntensity = sum(currentCell) / len(currentCell)
			intensityByCell[int(cell[1])] = averageIntensity #index by cellID #0402 coming back out of range
			currentCell = []  # empty currentCell after calculations
			currentCell.append (cell[2])	# add the first new cell intensity
			
	averageIntensity = sum(currentCell) / len(currentCell) # the last cell will never match
	intensityByCell[int(cell[1])] = averageIntensity
	return intensityByCell

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
	#		currentSum = currentSum +csv1 = read.csv('C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\scq\\wellA02_t1,2_IBCBT)pixelTuple[2]
	#		pixelsInLineage = pixelsInLineage+1
	#		cellAverageIntensities.append(currentSum / pixelsInLineage)
	#	print 'lineage average intensity: ' + str(cellAverageIntensities[i])
	
	