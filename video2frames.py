# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 08:33:36 2018

@author: Saurav
"""

import cv2
import os
 
from os.path import isfile, join

def video_to_frames(cap):
    img_list = [cap.read()[1] for i in range(1000)]
    count = 0
    for num in img_list:
        count+=1
        cv2.imwrite('./test_images/img%d.jpg' %(count), num)
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    files.sort(key = lambda x: list(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
 
def main():
    pathIn= './test_images/'
    pathOut = 'video.avi'
    fps = 25.0
    cap = cv2.VideoCapture('vtest.avi')
    video_to_frames(cap)
    convert_frames_to_video(pathIn, pathOut, fps)
 
if __name__=="__main__":
    main()