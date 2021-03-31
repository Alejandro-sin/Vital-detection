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
    videoFilename = "./data/record.avi"
    video = Video(videoFilename)

 # -- extract faces  ¿Se necesita esto como argumento de otra función?

    # video.getCroppedFaces(detector='mtcnn', extractor='skvideo')
    # video.showVideo()

    
    return video
   

data = load_data()


#-------------PROCESS ROI FUNCTIONS
def skin_adapt(data):
    # Adapt Funciotn
    # -- define ROIs: using skin, with threshold param
    adapt = data.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
    # roi_info = adapt.printROIInfo()
    # video.showVideo()
    return adapt


adapt = skin_adapt(data)
print(adapt)

