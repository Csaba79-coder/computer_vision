import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class QuadraticHistogramStretching:
    def __init__(self, image_path):
        # Load the image in grayscale mode.
        self.src = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        if self.src is None:
            raise ValueError("Image not found or the path is incorrect")

        # Calculate the minimum and maximum pixel values of the image.
        self.min_val = np.min(self.src)
        self.max_val = np.max(self.src)

    def perform_stretching(self):
        # Normalize the pixel values to the range [0, 1].
        normalized = (self.src - self.min_val) / (self.max_val - self.min_val)

        # Apply the quadratic transformation and scale back to [0, 255].
        self.stretched = 255.0 * np.power(normalized, 2)

        # Convert the result to an 8-bit image format for display.
        self.stretched = np.clip(self.stretched, 0, 255).astype(np.uint8)

    def display_results(self):
        # Create a layout with 1 row and 2 columns for displaying images.
        f, axs = plt.subplots(1, 2, figsize=(20, 8))

        # Display the original image.
        axs[0].imshow(self.src, cmap='gray', vmin=0, vmax=255)
        axs[0].set_title('Original Image')
        axs[0].axis('off')

        # Display the quadratic stretched image.
        axs[1].imshow(self.stretched, cmap='gray', vmin=0, vmax=255)
        axs[1].set_title('Quadratic Stretched Image')
        axs[1].axis('off')

        # Show the plot.
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == '__main__':
    image_path = 'heli_sotet.bmp'
    histogram_stretching = QuadraticHistogramStretching(image_path)
    histogram_stretching.perform_stretching()
    histogram_stretching.display_results()
