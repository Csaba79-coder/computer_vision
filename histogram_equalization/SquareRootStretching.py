import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class SquareRootStretching:
    def __init__(self, image_path):
        # Load the image in grayscale mode.
        self.src = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        if self.src is None:
            raise ValueError("Image not found or the path is incorrect")

    def perform_stretching(self):
        # Normalize the pixel values to the range [0, 1].
        normalized = self.src / 255.0

        # Apply the square root transformation.
        self.stretched = np.sqrt(normalized) * 255

        # Convert the result to an 8-bit image format for display.
        self.stretched = np.clip(self.stretched, 0, 255).astype(np.uint8)

    def display_results(self):
        # Create a layout with 1 row and 2 columns for displaying images.
        f, axs = plt.subplots(1, 2, figsize=(20, 8))

        # Display the original image.
        axs[0].imshow(self.src, cmap='gray', vmin=0, vmax=255)
        axs[0].set_title('Original Image')
        axs[0].axis('off')

        # Display the square root stretched image.
        axs[1].imshow(self.stretched, cmap='gray', vmin=0, vmax=255)
        axs[1].set_title('Square Root Stretched Image')
        axs[1].axis('off')

        # Show the plot.
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == '__main__':
    image_path = 'heli_sotet.bmp'
    square_root_stretching = SquareRootStretching(image_path)
    square_root_stretching.perform_stretching()
    square_root_stretching.display_results()
