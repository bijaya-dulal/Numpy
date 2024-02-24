import numpy as np
import cv2
import matplotlib.pyplot as plt

#reading the image
image = cv2.imread('image1.jpg')

#display image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
#convert to gray scale
#apply filter
#combine filter
#display processed image
#user interaction