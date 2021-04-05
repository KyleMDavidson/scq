#this takes a list (t dimension) of lists (cell dimension) of average cell intensity and makes a cell-major list of lists
def remajor_intensity_change_by_time(intensityByCellByTime):
	#[0] * n creates simply that many zeros, and is the preferred py2 way w/o numpy
	intensityCellMajorOverTime = [] #initialize 
	for lineage in range(len(intensityByCellByTime[1])): 
		scTimeSeries = [] #single cell time series
		for time in range(len(intensityByCellByTime)): 
			scTimeSeries.append(intensityByCellByTime[time][lineage])
		intensityCellMajorOverTime.append(scTimeSeries) 
	return intensityCellMajorOverTime	


	
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
#for each time (each cell: t2 - t1, t3-t2, t4-t3 (tabled)
'''def average_intensity_change_per_time(intensityChangeByCell):
	print 'remajored data: IBC in average intensity change / time: ',
	print intensityChangeByCell[1]
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
'''	
			
#across all T - seems wise to implement this after finishing the above
#def average_intensity_change_by_cell(intensityChangeByCell)
	
	