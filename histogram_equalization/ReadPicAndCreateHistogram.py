import cv2 as cv
from matplotlib import pyplot as plt
import os
class CreateHistogram:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.gray_image = None
        self.equalized_image = None
        self.read_pic()

    def read_pic(self):
        print("Current working directory:", os.getcwd())
        print(f"Attempting to read image from: {self.image_path}")
        self.image = cv.imread(self.image_path)

        if self.image is None:
            print("Error: Image not found.")
        else:
            # Convert the image to grayscale
            self.gray_image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

            # Apply histogram equalization
            self.equalized_image = cv.equalizeHist(self.gray_image)

            # Display the images and histograms
            self.display_images_and_histograms()

    def display_images_and_histograms(self):
        # Create a single figure to hold the images and histograms
        plt.figure(figsize=(12, 10))

        # Original Image
        plt.subplot(2, 2, 1)
        plt.imshow(self.gray_image, cmap='gray')
        plt.title('Original Grayscale Image')
        plt.axis('off')

        # Histogram of Original Image
        hist_src = cv.calcHist([self.gray_image], [0], None, [256], [0, 256])
        plt.subplot(2, 2, 2)
        plt.plot(hist_src, color='black')
        plt.title('Histogram of Original Grayscale Image')
        plt.xlim([0, 256])
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        # Equalized Image
        plt.subplot(2, 2, 3)
        plt.imshow(self.equalized_image, cmap='gray')
        plt.title('Equalized Image')
        plt.axis('off')

        # Histogram of Equalized Image
        hist_equalized = cv.calcHist([self.equalized_image], [0], None, [256], [0, 256])
        plt.subplot(2, 2, 4)
        plt.plot(hist_equalized, color='black')
        plt.title('Histogram of Equalized Image')
        plt.xlim([0, 256])
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    histogram_creator = CreateHistogram('lena.png')