#this is an outer wrapper
#apply singlecell quant to single images 
#save the results in an array of [cell ID, average intensity, time]
#sys.path.insert(0, 'C:\\Users\\Owner\\Documents\\SO\\scq')
from sys import modules #standard, includes sys.path #sys.path is an all-star for OS io. print/insert sys.path very useful
import sys.modules
import sys.path #depends on sys.modules #insert is not permanent without an export (temp mods to sys.path)
import os.path
#sys.path.insert(0, 'C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\scq') #work path (remote) (works)
#sys.path.insert(0, 'C:\\Documents\\Ilastik\\scq') #work path (local) 
#C:\Users\davidsonk2\OneDrive - UPMC\Documents\Ilastik\WellA02_gfp
sys.path.insert(0, 'C:\\Users\\Owner\\Documents\\SO\\scq\\scq') #homepath
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


#trackDir = r'C:\Users\davidsonk2\OneDrive - UPMC\Documents\Ilastik\WellA02_Tracking-Results' #work
#rawDir = r'C:\Users\davidsonk2\OneDrive - UPMC\Documents\Ilastik\WellA02_gfp'
#trackDir = r'C:\Users\Owner\Documents\SO\scq\WellA02_Tracking-Results' #home, full
#rawDir = r'C:\Users\Owner\Documents\SO\scq\WellA02_gfp'

raw_names = os.listdir(rawDir)[0:2]	 #first two for testing, 4/2
track_names = os.listdir(trackDir)[0:2]



# list (t dimension) of lists (cell dimension) of average cell intensity #R naturally takes None as NA. No coercion needed. 
# indices simple style list[i][j] approved, stack
intensityByCellByTime = scq_stack(raw_names, track_names) 

#print 'length of cellmajor IBC : ' + str(len(IBCBT))
#print ' first 5, IBCBT: ' + str(IBCBT[0:5]) # 4/4 this returns cellmajorIBC with 2 lists. 

#with open('C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\scq\\wellA02_t1,2_IBCBT_numbered','wb') as csvfile: 
with open ('.\scq_stack_output') as csvfile:
	IBCBTwriter = csvfile.writer(csvfile, delimiter = ',')
	for row in intensityByCellByTime: # each of these is being written as a value
		IBCBTwriter.writerow(row)
		
print 'finished and wrote'

#pixels = len(trackImp.getPixels()) #checking out.  9437184 for the current images
#the goal: get per cell averages per frame (x axis is time, y axis is average per cell intensity)