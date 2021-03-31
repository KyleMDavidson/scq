from ij import IJ
from sys.float_info import max as MAX_FLOAT

imp=IJ.getImage()
ip=imp.getProcessor().convertToFloat()
pixels=ip.getPixels()