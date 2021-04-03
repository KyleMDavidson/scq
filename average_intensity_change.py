#this takes a list (t dimension) of lists (cell dimension) of average cell intensity and makes a cell-major list of lists
def remajor_intensity_change_by_time(intensityByCellByTime):
	
	#[0] * n creates simply that many zeros, and is the preferred py2 way w/o numpy
	#somehow IBTCM is a fucking int 
	#make empty array
	intensityByTimeCellMajor = []
	
	intensityByCellByTime
	for lineage in range(len(intensityByCellByTime[1])): #this is across cells
		intensityCellMajorOverTime = [] #the final list
		oneCellMajor = [] #per cell
		for time in range(len(intensityByCellByTime)): #this is across t
			oneCellMajor.append(intensityByCellByTime[time][lineage])
		intensityCellMajorOverTime.append(oneCellMajor)
'''
	for i in range(len(intensityByCellByTime)):
		innerList = []
		for j in range(len(intensityByCellByTime[1])):
			innerList.append(intensityByCellByTime[j][i])
		intensityByTimeCellMajor.append(innerList)
			
	for t in range(len(intensityByCellByTime)): # [IBCTM] = [ T X C ] = intensity 
		work = intensityByCellByTime[t] # [ C ] = intensity
		innerList = [] 
		for c in range(len(work)):
			innerList.append(intensityByCellByTime)
	return intensityByTimeCellMajor
	'''
#takes cell major intensities by time
#should return per lineage per time deltas
def average_intensity_change_by_cell(intensityChangeByCell):
	intensityDeltasByCell = []
	averageIntensities = []	
	for cell in intensityChangeByCell:
		intensityDeltas = []
		initialIntensity = cell[0]
		i = 1
		while i != length(cell)-1:
			intensityDeltas.append(cell[i]-cell[i-1])
			i = i + 1
		intensitySum = sum(intensityDeltas)
		averageIntensityDelta = intensitySum / len(intensitySum)
		intensityDeltasByCell.append(averageIntensityDelta)
	return intensityDeltasByCell
	
			
			
		
	
	