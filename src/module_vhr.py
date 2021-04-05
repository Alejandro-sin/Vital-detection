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
    videoFilename = "./data/record.avi"
    video = Video(videoFilename)
    video.getCroppedFaces(detector='mtcnn', extractor='skvideo')
    # -- extract faces  ¿Se necesita esto como argumento de otra función?
    return video



def adapt():
    video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
    return video.printROIInfo()


def fix():
    video.setMask(typeROI='skin_fix',skinThresh_fix=[30, 50])
    return video.printROIInfo()


# -----------------------------TUNING

video = load_data()
# Aquí falta definir cuales son los parámetros de entrada para "params" en skin_fix
params = {"video": video, "verb":0, "ROImask":"skin_adapt", "skinAdapt":0.2}

def chrom():
# -- define some params in the form of dict (those in the cfg file) 
    # -- invoke the method
    m = CHROM(**params)
    bpmES, timesES = m.runOffline(**params)
    return print(bpmES)


def pos():
    m = POS(**params)
# -- invoke the method
    bpmES, timesES = m.runOffline(**params)
    return print(bpmES)


def run(): 
    load_data()
    chrom()



if __name__=='__main__':
    run()
    