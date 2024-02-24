import numpy as np
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


#reading the image
image = cv2.imread('image1.jpg')

#display image
plt.figure(figsize=(10, 5))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
#convert to gray scale
def rgb_to_grayscale(rgb_img):
    # Convert RGB image to grayscale
    grayscale_img = np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])
    return grayscale_img

gray_image = rgb_to_grayscale(image)
plt.subplot(2, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('gray Image')


#apply filter
def new_filter(image):
    # Define the emboss kernel
    kernel = np.array([[0, 1, -1],
                       [1,  0, -1],
                       [1,  1,  1]])
    
    # Apply the kernel to the image using filter2D convolution
    embossed_img = cv2.filter2D(image, -1, kernel)
    
    return embossed_img
new_image = new_filter(image)
plt.subplot(2,2, 3)
plt.imshow(new_image, cmap='gray')
plt.title('enhance Image')

#combine filter
def new_filter_on_grayscale(rgb_img):
    # Convert RGB image to grayscale
    grayscale_img = rgb_to_grayscale(rgb_img)
    
    # Apply the new_filter function to the grayscale image
    filtered_img = new_filter(grayscale_img)
    
    return filtered_img
#display processed image
filtered_image = new_filter_on_grayscale(image)
plt.subplot(2, 2, 4)
plt.imshow(filtered_image, cmap='gray')
plt.title('filtered Image')
plt.close()
#user interaction
#in another file