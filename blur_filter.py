import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def blur_filter(image, kernel_size=9):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    blurred_image = np.zeros_like(image, dtype=np.float32)
    for i in range(image.shape[2]):  # Loop over color channels
        blurred_image[:, :, i] = convolve2d(image[:, :, i], kernel, mode='same')
    return blurred_image.astype(np.uint8)

# Load color image
image = cv2.imread('image1.jpg')

# Apply blur filter
blurred_image = blur_filter(image)

# Display original and blurred images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image')
plt.show()
