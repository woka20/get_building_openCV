import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import hsv_to_rgb


#BGR code color for Building in OpenStreetMaps is (224,217,211)
light_brown = np.uint8([[[202,208,216 ]]]) 

color_codes=[]
#Convert BGR to HSV for masking
hsv_light_brown = cv2.cvtColor(light_brown,cv2.COLOR_BGR2HSV)

for index in hsv_light_brown:
    color_codes=index[0]


#Start masking the image here
image=cv2.imread("map.png",1)
maps=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray=cv2.cvtColor(maps, cv2.COLOR_RGB2HSV)

cream = (float(color_codes[0]), float(color_codes[1]), float(color_codes[2]))
brown = (float(color_codes[0])+30, float(color_codes[1])+30, float(color_codes[2])+30)

# cream= (13, 17, 216)
# brown = (100, 100, 226)

mask = cv2.inRange(gray, cream,brown)
hsv=cv2.bitwise_and(image,image, mask=mask)

plt.subplot(1,2,1)
plt.imshow(hsv, cmap="gray")
plt.title('OSM Image')
plt.xticks([]), plt.yticks([])
plt.show()