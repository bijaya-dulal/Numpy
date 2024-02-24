from project1 import new_filter, new_filter_on_grayscale
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def open_file():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load the selected image file
        input_image = cv2.imread(file_path)
        
        # Apply the new filter on the grayscale image
        filtered_image = new_filter_on_grayscale(input_image)
        
        # Display the original and filtered images
        plt.figure(figsize=(10, 5))
        plt.subplot(2, 2, 1)
        plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')
        plt.subplot(2, 2, 4)
        plt.imshow(filtered_image, cmap='gray')
        plt.title('filtered Image')
        plt.show()
        root.destroy()
# Create Tkinter GUI window
root = tk.Tk()
root.title("Image Filter")

# Add button to select image file and apply filter
btn_open = tk.Button(root, text="Open Image", command=open_file)
btn_open.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()