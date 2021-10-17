import cv2
import numpy as np
import os

mv = cv2.VideoCapture('my_video')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    ret, frame = cap.read()

    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    currentFrame += 1

mv.release()
cv2.destroyAllWindows()
