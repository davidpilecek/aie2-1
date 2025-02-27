import time
import numpy as np
import cv2

from picamera2 import Picamera2, Preview
from libcamera import controls, Transform


picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main = {"size": (600, 400)}, transform = Transform(hflip=1, vflip=1)))
picam2.start()
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
picam2.set_controls({"ScalerCrop": (0, 0, 400, 400)})

time.sleep(2)



while True:
    
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )
    cv2.imshow('frame', frame)
    # ~ cv2.imshow('gray', gray)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite("/home/pi/Desktop/aie2/pics/frameAr2.jpg", frame)
        break
    

time.sleep(2)
