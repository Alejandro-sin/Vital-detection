import numpy as np
import pandas as pd
import cv2
import time


'''
Revisar si constuyo la clase con métodos para  modularizar
las opciones dependientes de cv2 como métodos unificados en la clase "Caps"

class Caps():
    def __init__(self, video_capture,  close_cap, take_picture):
        pass


video_capture: El método de video_cap
close_cap: Cerrar la captura del frame que se abre
take_picture: Tomar una foto.



'''


def take_picture():
    '''
    This function taks a pictue whn the video captures ends.
    '''
    pass





def video_cap():
    capture_duration = 11
    capture = cv2.VideoCapture(0)
    # Encoding
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Write and save
    out = cv2.VideoWriter('./data/record.avi',fourcc, 20.0, (640,480))
    start_time = time.time()

    # Time interval
    while(int(time.time() - start_time) < capture_duration):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow('Vide Capture', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    out.release()
    cv2.destroyAllWindows()









if __name__ == '__main__':
    video_cap()