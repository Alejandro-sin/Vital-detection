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



#-------------PROCESS ROI FUNCTIONS
def skin_adapt(video):
    # Adapt Funciotn
    # -- define ROIs: using skin, with threshold param
    adapt = video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
    # adapt = adapt.printROIInfo()
    # video.showVideo()
    return adapt


adapt = skin_adapt(video)
print(type(adapt))



def skin_fix(video):
    #Fix
    # -- define ROIs: using skin, with threshold param 
    fix = video.setMask(typeROI='skin_fix',skinThresh_fix=[30, 50])
    # video.printROIInfo()
    # video.showVideo()
    return fix


fix = skin_fix(video)
print(type(fix)) ## Retunr NoNe







""" # -----------------------------TUNING
params = {
    "video":video, 
    "verb":32, 
    "ROImask":"skin_adapt", 
    "skinAdapt":0.2
    }


def CHROM(params):
    params = {
    "video":video, 
    "verb":32, 
    "ROImask":"skin_adapt", 
    "skinAdapt":0.2
    }

    # -- define some params in the form of dict (those in the cfg file) 
    m = CHROM(**params) 
    bpmES, timesES = m.runOffline(**params)
    return [bpmES, timesES]



c = CHROM(params)
print(c)
print(type(c))
print("▬"*30)



def POS(params):
    m = POS(**params)
    bpmES, timesES = m.runOffline(**params)
    return bpmES  



print(POS(params))
print(type(POS(params)))
print("▬"*30)

 """