import cv2
#import os
#from os.path import isfile, join
import matplotlib.image as mpimg
#from pandas import read_csv
#from PIL import Image
#from pytesseract import image_to_string
#import pytesseract
#import argparse

class videoDetection:

    def imageDenoising(self, fileName):
        file_path = './test_images/'  + fileName
        input_img = mpimg.imread(file_path)
        output_img = cv2.fastNlMeansDenoisingColored(input_img, None, 10, 10, 7, 21)

        return output_img

    def convert_to_ocr(self,img_src):
        img_rgb = cv2.imread(img_src)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        for j in (1,2):
            for i in range(3,91):
                temp_src='temp_match/'+str(j)+'/'+str(i)+'.jpg'
                template = cv2.imread(temp_src,0)
                if template is None :
                    continue
                w, h = template.shape[::-1]

                res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
                threshold = 0.95
                loc = np.where( res >= threshold)
                match = False

                for pt in zip(*loc[::-1]):
                    if pt is not None:
                        match=True
                if (match):
                    print(i)


    def frames_to_videos(self,csq):
        pass


    def video_to_frames(self,cap,x=0,x1=0,y=0,y1=0):
        count = 0
        finalList = []
        ret, frame = cap.read()
        while(ret):
            count+=1
            #frame=frame[x:x1,y:y1]
            ts = str(format(float(count)*0.1,"0.1f"))
            src = './test_images/'+ ts+ '.jpg'
            denoiseImg = imageDenoising(frame)
            csvData = convert_to_ocr(denoiseImg)
            ret, frame = cap.read()
            finalList.append(csvData)
        return finalList


if __name__=="__main__":
    sample = []

    myFiles = ['./sample_videos/Adrift_bug.avi', './sample_videos/Airspeed_digit.avi', './sample_videos/Airspeed_digit_1.avi' ,'./sample_videos/Altitude_Digits.avi' , './sample_videos/BARO_M_Bug_Digit.avi' , './sample_videos/compass_scale_heading.avi' ,'./sample_videos/EVS_Bug.avi' , './sample_videos/Flash_ICE_VTA.avi', './sample_videos/LAT_DEV.avi', './sample_videos/Load_speed_cue.avi', './sample_videos/partial_compass.avi', './sample_videos/slip.avi', './sample_videos/Vertical_Speed_Pointer.avi', './sample_videos/WNAV_target_altitude_bug_Digit.avi', './sample_videos/Wind_Arrow.avi']

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[1])
    #x,x1,y,y1 = 22,88,232,271,
    testVid.video_to_frames(cap) #Left Side Bar Changing Value

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[2])
    #x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap) #Left Side Bar Changing Value

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[3])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) # ICE Blink
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) # Right HAnd Side Bar Changing value

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[4])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Barometer Value

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[5])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Barometer Spinning Value Given
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #ICE Blink

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[6])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Code from Siddharth for vertical movement capture

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[7])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Blink ICE
    x,x1,y,y1 = 555,599,44,74
    testVid.video_to_frames(cap,x,x1,y,y1) #VTA Blink

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[8])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Blink ICE
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #VTA Blink
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Horizontal bar moving Code from Siddharth

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[9])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Code from Siddharth
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #VTA Blink

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[10])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Different type of compass

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[11])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Upper Bar Horizontal Movement Code from Siddharth

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[12])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Right Side speedometer Value Given

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[13])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1) #Value on right side above the speedometer bit towards middle

    testVid = videoDetection()
    cap = cv2.VideoCapture(myFiles[14])
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1)# ICE Blink
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1)# VTA Blink
    x,x1,y,y1 = 0,0,0,0
    testVid.video_to_frames(cap,x,x1,y,y1)#Wind-Arrow Rotating










