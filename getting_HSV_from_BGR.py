import cv2
import numpy as np


#Building color BGR code in OpenStreetMaps
light_brown = np.uint8([[[224,217,211 ]]]) 

hsv_light_brown = cv2.cvtColor(light_brown,cv2.COLOR_BGR2HSV)

#Get The HSV Color code for masking
print (hsv_light_brown)