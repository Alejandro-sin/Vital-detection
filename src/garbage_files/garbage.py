# -- Modules and packages to import for demo
import numpy as np
from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
from pyVHR.methods.chrom import CHROM
from pyVHR.analysis.testsuite import TestSuite, TestResult
from pyVHR.datasets.sample import SAMPLE
from pyVHR.datasets.dataset import Dataset
from pyVHR.utils.errors import getErrors, printErrors, displayErrors


# -- Video object
videoFilename = ".record.avi"
video = Video(videoFilename)

# -- extract faces
video.getCroppedFaces(detector='mtcnn', extractor='skvideo')


# Adapt Funciotn
# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
video.printROIInfo()


#Fix
# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_fix',skinThresh_fix=[30, 50])
video.printROIInfo()




# TUNING
# -- define some params in the form of dict (those in the cfg file) 
params = {"video": video, "verb":32, "ROImask":"skin_adapt", "skinAdapt":0.2}

# -- invoke the method
m = CHROM(**params)
#m = POS(**params)

# -- invoke the method
bpmES, timesES = m.runOffline(**params)
bpmES  # BPM by frame  como un promedio. np.mean()


