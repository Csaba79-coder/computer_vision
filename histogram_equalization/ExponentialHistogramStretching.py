import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class ExponentialHistogramStretching:
    def __init__(self, image_path, gamma=1.0):
        # Load the image in grayscale mode.
        self.src = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        if self.src is None:
            raise ValueError("Image not found or the path is incorrect")
        self.gamma = gamma

    def perform_stretching(self):
        # Normalize the pixel values to the range [0, 1].
        normalized = self.src / 255.0

        # Apply the exponential transformation using gamma correction.
        # res = 255 * (255/src) ** gamma
        # Here:
        # - res: The transformed pixel value.
        # - src: The original pixel value.
        # - gamma: The gamma correction value.
        # This formula enhances the contrast by raising normalized values to the power of gamma.
        self.stretched = np.power(normalized, self.gamma) * 255

        # Convert the result to an 8-bit image format for display.
        self.stretched = np.clip(self.stretched, 0, 255).astype(np.uint8)

    def display_results(self):
        # Create a layout with 1 row and 2 columns for displaying images.
        f, axs = plt.subplots(1, 2, figsize=(20, 8))

        # Display the original image.
        axs[0].imshow(self.src, cmap='gray', vmin=0, vmax=255)
        axs[0].set_title('Original Image')
        axs[0].axis('off')

        # Display the exponentially stretched image.
        axs[1].imshow(self.stretched, cmap='gray', vmin=0, vmax=255)
        axs[1].set_title(f'Exponential Stretched Image (gamma={self.gamma})')
        axs[1].axis('off')

        # Show the plot.
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == '__main__':
    image_path = 'heli_sotet.bmp'
    gamma_value = 0.5  # Adjust the gamma value for different contrast levels.
    histogram_stretching = ExponentialHistogramStretching(image_path, gamma=gamma_value)
    histogram_stretching.perform_stretching()
    histogram_stretching.display_results()
