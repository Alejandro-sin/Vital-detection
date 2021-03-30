from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
from pyVHR.methods.chrom import CHROM
from pyVHR.analysis.testsuite import TestSuite, TestResult

# -- Video object
videoFilename = "./data/record.avi"
video = Video(videoFilename)

# -- extract faces
video.getCroppedFaces(detector='mtcnn', extractor='skvideo')
video.printVideoInfo()

print("\nShow video cropped faces, crop size:", video.cropSize)
video.showVideo()



# -- define ROIs: free rectangular regions
video.setMask(typeROI='rect', rectCoords=[[15,20,140,50],[10,120,100,30]])
video.printROIInfo()
video.showVideo()


# -- define ROIs: standard regions, i.e. 'forehead', 'lcheek', 'rcheek', 'nose'
video.setMask(typeROI='rect', rectRegions=['forehead', 'lcheek', 'rcheek', 'nose'])
video.printROIInfo()
video.showVideo()


# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
video.printROIInfo()
video.showVideo()



# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_fix',skinThresh_fix=[20, 50])
video.printROIInfo()
video.showVideo()

# -- Detailed pipeline for rafinement steps and tuning  

# -- define some params in the form of dict (those in the cfg file) 
params = {"video": video, "verb":32, "ROImask":"skin_adapt", "skinAdapt":0.2}

# -- invoke the method
m = CHROM(**params)
#m = POS(**params)

# -- invoke the method
bpmES, timesES = m.runOffline(**params)