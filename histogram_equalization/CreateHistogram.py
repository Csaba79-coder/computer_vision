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

            # Display the original and equalized images or the histogram
            # Comment out what you don't need
            # You can see in ReadPicAndCreateHistogram py all 4 at once! 2 pix + 2 histograms
            self.display_images()
            self.display_histograms()

    def display_images(self):
        # Display the original and equalized images
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.imshow(self.gray_image, cmap='gray')
        plt.title('Original Grayscale Image')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(self.equalized_image, cmap='gray')
        plt.title('Equalized Image')
        plt.axis('off')

        plt.show()

    def display_histograms(self):
        # Calculate histograms
        hist_src = cv.calcHist([self.gray_image], [0], None, [256], [0, 256])
        hist_equalized = cv.calcHist([self.equalized_image], [0], None, [256], [0, 256])

        # Plot histograms
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.plot(hist_src, color='black')
        plt.title('Histogram of Original Grayscale Image')
        plt.xlim([0, 256])
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.subplot(1, 2, 2)
        plt.plot(hist_equalized, color='black')
        plt.title('Histogram of Equalized Image')
        plt.xlim([0, 256])
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.show()

if __name__ == '__main__':
    histogram_creator = CreateHistogram('lena.png')
