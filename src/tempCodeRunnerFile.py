import numpy as np
import pandas as pd
#import cv2
import time
import module_vhr as vhr



results = vhr.run()
print(type(results))

mean_r = np.mean(results)
print(type(mean_r))
