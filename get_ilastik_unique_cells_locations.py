from ij import IJ
from sys import modules
from sys.float_info import max as MAX_FLOAT  
from java.util import ArrayList
from array import array, zeros
import os
import sys

#export PYTHONPATH='C:\Users\davidsonk2\OneDrive - UPMC\Documents\Ilastik\scq'

#'C:\Java\Fiji.app' is the working dir from ImageJ
#file extension is necessary or filenotfound exceptions
#escaping backslash necessary or compiler will modify
#input: ilastik greyscale tiffs of any resolution and depth
def get_ilastik_unique_cells_locations(mask_pixels):
	#returns list of tuples like (2085103, 0.0), (2085104, 0.0)
	enumeratedPixels = list(enumerate(mask_pixels))
	return enumeratedPixels


	
#filehandler = open('sorted_enumerated_926_t1','w')
#pickle.dump(sorted_enumerated_list, filehandler)'''
#get_ilastik_unique_cells_locations('C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\WellA02_Tracking-Results\\','WellA02_ChannelFITC,mCherry_Seq0001__Tracking-Result__00.tif')
	
'''objectIDs=set(sorted_enumerated_list)
averageIntensities=int[len(objectIDs)]
objectID=objectIDs[1]
i=1
while i<=len(sorted_enumerated_list):
	sorted_enumerated_list
	
	'''
	
'''
#fs = FileSaver(image)
#if os.path.exists(output_folder):
#	print 'output dir exists!'
#else:
#	print "output location failed"


	'''

'''
print 'imagepath: ' + imagePath
print 'objectivepath: ' + objectivePath

if os.path.exists(objectivePath):
	print "exists"
else:
	print "file doesn't exist"'''
#objectivePath = os.path.dirname(os.path.abspath(imagePath)) 
#this returns the path C:\Java\Fiji.app

#pickle save if necessary import pickle

