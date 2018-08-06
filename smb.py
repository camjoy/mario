#!/usr/bin/env python3

import numpy as np
import cv2
import pyscreenshot as pss
import time
import sys, string, os


last_time = time.time()
while(True):
    screen = pss.grab(bbox=(50,50,800,640))
    print('Loop took {} seconds',format(time.time()-last_time))
    cv2.imshow("test", np.array(screen))
    last_time = time.time()
    # waits 25 ms for the user to press q and
    # exits if q is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
