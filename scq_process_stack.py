#this is an outer wrapper
#apply singlecell quant to single images 
#save the results in an array of [cell ID, average intensity, time]
# ilastik_singlecell_quant should be subordinate. 
#just hardcoding these for now (easy to do)
#sys.path.insert(0, 'C:\\Users\\Owner\\Documents\\SO\\scq')
from sys import modules #standard, includes sys.path #sys.path is an all-star for OS io. print/insert sys.path very useful
import sys.modules
import sys.path #depends on sys.modules #insert is not permanent without an export (temp mods to sys.path)
sys.path.insert(0, 'C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\scq') #work path (remote) (works)
#sys.path.insert(0, 'C:\\Documents\\Ilastik\\scq') #work path (local) 
import ilastik_singlecell_quant

trackDir = r'C:\Users\Owner\Documents\SO\scq\WellA02_Tracking-Results\'
trackName = "WellA02_ChannelFITC,mCherry_Seq0001__Tracking-Result__00.tif"
trackPath = trackDir+trackName
#C:\Users\davidsonk2\OneDrive - UPMC\Documents\Ilastik\WellA02_gfp
#rawDir = "C:\\Users\\davidsonk2\\OneDrive - UPMC\\Documents\\Ilastik\\WellA02_gfp\\"
#rawName = 'WellA02_ChannelFITC,mCherry_Seq0001_00.tif'
#rawPath = rawDir + 

rawDir = r'C:\Users\Owner\Documents\SO\scq\WellA02_gfp' #trailing \ escapes ' in a rawstring 
rawName = r'\WellA02_ChannelFITC,mCherry_Seq0001_00.tif'
rawPath = rawDir + rawName




#ilastik_singlecell_quant.scq(rawPath, trackPath)

#the goal: get per cell averages per frame, assigned to 