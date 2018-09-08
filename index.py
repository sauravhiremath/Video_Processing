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

	def convert_to_ocr(self):
		pass


	def frames_to_videos(self,csq):
		pass


	def video_to_frames(self,cap,x,x1,y,y1):
		count = 0
		ret, frame = cap.read()
		while(ret):
			count+=1
			frame=frame[x:x1,y:y1]
			ts = str(format(float(count)*0.1,"0.1f"))
			sorc='./test_images/'+ ts+ '.jpg'
			denoiseImg = imageDenoising(frame)
			csvData = convert_to_ocr(denoiseImg)

			# with open('ocrText.csv', 'w') as csvFile:
		 #    	writer = csv.writer(csvFile)
		 #    	writer.writerows(csvData)
		 #    csvFile.close()

			ret, frame = cap.read()

if __name__=="__main__":
	sample = []

	myFiles = ['Adrift_bug.avi', 'Airspeed_digit.avi', 'Airspeed_digit_1.avi' ,'Altitude_Digits.avi' , 'BARO_M_Bug_Digit.avi' , 'compass_scale_heading.avi' ,'EVS_Bug.avi' , 'Flash_ICE_VTA.avi', 'LAT_DEV.avi', 'Load_speed_cue.avi', 'partial_compass.avi', 'slip.avi', 'Vertical_Speed_Pointer.avi', 'WNAV_target_altitude_bug_Digit.avi', 'Wind_Arrow.avi']

	testVid = videoDetection()
	cap = cv2.VideoCapture(myFiles[1])
	x,x1,y,y1 = 0,0,0,0
	testVid.video_to_frames(cap,x,x1,y,y1) #Left Side Bar Changing Value

	testVid = videoDetection()
	cap = cv2.VideoCapture(myFiles[2])
	x,x1,y,y1 = 0,0,0,0
	testVid.video_to_frames(cap,x,x1,y,y1) #Left Side Bar Changing Value

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
	x,x1,y,y1 = 0,0,0,0
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










