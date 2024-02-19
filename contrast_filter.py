import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance_contrast(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    return equalized

# Load image
image = cv2.imread('image1.jpg')
brightened_image = image.astype(np.int32) +30

# Enhance contrast
enhanced_image = enhance_contrast(image)

# Display original and enhanced images
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(enhanced_image, cmap='gray')
plt.title('Enhanced Image')
plt.subplot(1, 3, 3)
plt.imshow(brightened_image, cmap='gray')
plt.title('brightened Image')
plt.show()
