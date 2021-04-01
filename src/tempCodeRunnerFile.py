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
def load_data():
    # -- Video object
    videoFilename = "./data/data_test.mp4"
    video = Video(videoFilename)

 # -- extract faces  ¿Se necesita esto como argumento de otra función?
    # video.getCroppedFaces(detector='mtcnn', extractor='skvideo')
    # video.showVideo()
    return video
   


video = load_data()
print(type(video))
video.printROIInfo() # Reduelve corrdenada
print("▬"*30)
video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
video.printROIInfo()

