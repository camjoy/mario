#!/usr/bin/env python3

import numpy as np
import cv2
import pyscreenshot as pss
import time
import sys, string, os
from pynput.keyboard import Key, Controller

keyboard = Controller()


last_time = time.time()
while(True):
    screen = pss.grab(bbox=(75,75,700,570))
    print('Loop took {} seconds',format(time.time()-last_time))
    edges = []

    edges = cv2.Canny(np.array(screen), 100, 200)

    cv2.imshow("test", np.array(edges))

    keyboard.press(Key.right)
    time.sleep(3)
    keyboard.release(Key.right)

    last_time = time.time()
    # waits 25 ms for the user to press q and
    # exits if q is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
