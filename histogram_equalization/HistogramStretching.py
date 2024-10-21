import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Define the class for Quadratic Histogram Stretching
class QuadraticHistogramStretching:
    def __init__(self, src):
        self.src = src
        self.min_val = np.min(src)
        self.max_val = np.max(src)
        self.stretched = None

    def apply_stretching(self):
        # Normalize the input image to [0, 1]
        normalized = (self.src - self.min_val) / (self.max_val - self.min_val)

        # Apply the quadratic stretching formula
        self.stretched = 255.0 * (normalized ** 2)

        # Convert the result back to an 8-bit image
        self.stretched = np.clip(self.stretched, 0, 255).astype(np.uint8)
        return self.stretched


# Define the class for Square Root Histogram Stretching
class SquareRootHistogramStretching:
    def __init__(self, src):
        self.src = src
        self.min_val = np.min(src)
        self.max_val = np.max(src)
        self.stretched = None

    def apply_stretching(self):
        # Normalize the input image to [0, 1]
        normalized = (self.src - self.min_val) / (self.max_val - self.min_val)

        # Apply the square root stretching formula
        self.stretched = 255.0 * np.sqrt(normalized)

        # Convert the result back to an 8-bit image
        self.stretched = np.clip(self.stretched, 0, 255).astype(np.uint8)
        return self.stretched


# Load the grayscale image
src = cv.imread("/content/drive/MyDrive/ComputerVision/images/modified/heli_sotet.bmp", cv.IMREAD_GRAYSCALE)

# Apply quadratic stretching
quadratic_stretch = QuadraticHistogramStretching(src)
quadratic_result = quadratic_stretch.apply_stretching()

# Apply square root stretching
square_root_stretch = SquareRootHistogramStretching(src)
square_root_result = square_root_stretch.apply_stretching()

# Display the original and transformed images
f, axs = plt.subplots(1, 3, figsize=(30, 10))
plt.subplot(131), plt.imshow(src, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image")
plt.subplot(132), plt.imshow(quadratic_result, cmap='gray', vmin=0, vmax=255)
plt.title("Quadratic Stretched Image")
plt.subplot(133), plt.imshow(square_root_result, cmap='gray', vmin=0, vmax=255)
plt.title("Square Root Stretched Image")
plt.show()
