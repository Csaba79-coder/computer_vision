import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class LinearHistogramStretching:
    def __init__(self, image_path):
        # Load the image in grayscale mode.
        self.src = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        if self.src is None:
            raise ValueError("Image not found or the path is incorrect")

    def perform_stretching(self):
        # Perform linear histogram stretching.
        min_val = np.min(self.src)
        max_val = np.max(self.src)
        self.stretched = 255.0 / (max_val - min_val) * (self.src - min_val)
        # Convert the result to an 8-bit image format for display.
        self.stretched = np.clip(self.stretched, 0, 255).astype(np.uint8)

    def display_results(self):
        # Create a layout with 1 row and 2 columns for displaying images.
        f, axs = plt.subplots(1, 2, figsize=(20, 8))

        # Display the original image.
        axs[0].imshow(self.src, cmap='gray', vmin=0, vmax=255)
        axs[0].set_title('Original Image')
        axs[0].axis('off')

        # Display the stretched image.
        axs[1].imshow(self.stretched, cmap='gray', vmin=0, vmax=255)
        axs[1].set_title('Stretched Image')
        axs[1].axis('off')

        # Show the plot.
        plt.tight_layout()
        plt.show()


# Example usage:
if __name__ == '__main__':
    image_path = 'heli_sotet.bmp'
    histogram_stretching = LinearHistogramStretching(image_path)
    histogram_stretching.perform_stretching()
    histogram_stretching.display_results()
