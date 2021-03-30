
# -- Modules and packages to import for demo
from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
from pyVHR.methods.chrom import CHROM
from pyVHR.analysis.testsuite import TestSuite, TestResult
from pyVHR.datasets.sample import SAMPLE
from pyVHR.datasets.dataset import Dataset
from pyVHR.utils.errors import getErrors, printErrors, displayErrors


# -- Video object
videoFilename = "./data/record.avi"
video = Video(videoFilename)

# -- extract faces
video.getCroppedFaces(detector='mtcnn', extractor='skvideo')
video.printVideoInfo()

print("\nShow video cropped faces, crop size:", video.cropSize)
video.showVideo()


# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
video.printROIInfo()
video.showVideo()



# -- define ROIs: using skin, with threshold param 
video.setMask(typeROI='skin_fix',skinThresh_fix=[30, 50])
video.printROIInfo()
video.showVideo()


# -- define some params in the form of dict (those in the cfg file) 
params = {"video": video, "verb":32, "ROImask":"skin_adapt", "skinAdapt":0.2}

# -- invoke the method
m = CHROM(**params)
#m = POS(**params)

# -- invoke the method
bpmES, timesES = m.runOffline(**params)
# bpmES

# -- dataset object
dataset = SAMPLE(videodataDIR="./data/record.avi", BVPdataDIR="./data/record.avi")  # ¿Que carpeta necesito?

# -- ground-truth (GT) signal
idx = 0   # index of signal within the list dataset.videoFilenames
fname = dataset.getSigFilename(idx)

# -- load signal and build a BVPsignal or ECGsignal object
sigGT = dataset.readSigfile(fname)
sigGT.plot()

# -- plot signal + peaks
sigGT.findPeaks(distance=20)
sigGT.plotBPMPeaks()

# -- compute BPM GT
winSizeGT = 7
bpmGT, timesGT = sigGT.getBPM(winSizeGT)


# -- error metrics
RMSE, MAE, MAX, PCC = getErrors(bpmES, bpmGT, timesES, timesGT)
printErrors(RMSE, MAE, MAX, PCC)
displayErrors(bpmES, bpmGT, timesES, timesGT)
#bpmGT



# -- print BPM
print("BPMs of the GT signal averaged on winSizeGT = %d sec:" %winSizeGT)
print(bpmGT)

# -- plot spectrogram
sigGT.displaySpectrum()





