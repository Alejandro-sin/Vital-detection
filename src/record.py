import numpy as np
import pandas as pd
import cv2

capture = cv2.VideoCapture(0)
# Encoding
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Write and save
out = cv2.VideoWriter('./data/record.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
out.release()
cv2.destroyAllWindows()