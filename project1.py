import numpy as np
import cv2
import matplotlib.pyplot as plt

#reading the image
image = cv2.imread('image1.jpg')

#display image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
#convert to gray scale
def rgb_to_grayscale(rgb_img):
    # Convert RGB image to grayscale
    grayscale_img = np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])
    return grayscale_img
gray_image = rgb_to_grayscale(image)
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('gray Image')
plt.show()

#apply filter
#combine filter
#display processed image
#user interaction