# -- Modules and packages to import for demo
import numpy as np
from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
from pyVHR.methods.chrom import CHROM
from pyVHR.analysis.testsuite import TestSuite, TestResult
from pyVHR.datasets.sample import SAMPLE
from pyVHR.datasets.dataset import Dataset
from pyVHR.utils.errors import getErrors, printErrors, displayErrors


#-------------------- HANDLE DATA

videoFilename = "./data/record.avi"
video = Video(videoFilename)

 # -- extract faces  ¿Se necesita esto como argumento de otra función?
video.getCroppedFaces(detector='mtcnn', extractor='skvideo')

""" 
print(type(video))
video.printROIInfo() 
print("▬"*30)
  """

video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
video.printROIInfo()


""" print("▬"*30) """

video.setMask(typeROI='skin_fix',skinThresh_fix=[30, 50])
video.printROIInfo()


# -----------------------------TUNING

# -- define some params in the form of dict (those in the cfg file) 
params = {"video": video, "verb":0, "ROImask":"skin_adapt", "skinAdapt":0.2}

# -- invoke the method
m = CHROM(**params)
#m = POS(**params)

# -- invoke the method
bpmES, timesES = m.runOffline(**params)
print(bpmES)



if __name__=='__main__':
    pass

