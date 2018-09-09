import cv2
import numpy as np

def return_Airspeed(img_src):
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
				return i

	return 0

print(return_Airspeed('check6.jpg'))
