# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:36:43 2018

@author: Saurav
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('vtest.avi')

# create a list of first 5 frames
img = [cap.read()[1] for i in range(5)]

# convert all to color_scalescale
gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]

# convert all to float64
gray = [np.float64(i) for i in gray]

# create a noise of variance 25
noise = np.random.randn(*gray[1].shape)*10

# Add this noise to images
noisy = [i+noise for i in gray]

# Convert back to uint8
noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]

# Denoise 3rd frame considering all the 5 frames
dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 20, 15, 105)

plt.subplot(1,3,1),plt.imshow(gray[2],'gray')
plt.subplot(1,3,2),plt.imshow(noisy[2],'gray')
plt.subplot(1,3,3),plt.imshow(dst,'gray')
plt.show()
cv2.imwrite('output-trial-1.jpg', gray[2])
cv2.imwrite('output-trial-2.jpg', noisy[2])
cv2.imwrite('output-trial-3.jpg', dst)

#image_channels = np.concatenate((color_scale[2], noisy[2], dst), axis=3)