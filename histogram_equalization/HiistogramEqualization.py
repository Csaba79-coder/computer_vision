import cv2 as cv
from matplotlib import pyplot as plt

# https://docs.opencv.org/4.8.0/d4/d1b/tutorial_histogram_equalization.html

class HistogramEqualization:
    def __init__(self, image_path):
        # Load the image in grayscale mode.
        self.src = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        if self.src is None:
            raise ValueError("Image not found or the path is incorrect")

    def perform_histogram_equalization(self):
        # Perform histogram equalization on the src image and store the result in dst.
        self.dst = cv.equalizeHist(self.src)

        # Calculate the histogram of the equalized image.
        self.hist_dst = cv.calcHist([self.dst], [0], None, [256], [0, 256])

    def perform_clahe(self):
        # Create a CLAHE object (Contrast Limited Adaptive Histogram Equalization).
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        # Apply the CLAHE algorithm to the src image and store the result in dst2.
        self.dst2 = clahe.apply(self.src)

        # Calculate the histogram of the CLAHE-processed image.
        self.hist_dst2 = cv.calcHist([self.dst2], [0], None, [256], [0, 256])

    def display_results(self):
        # Calculate the histogram of the original image.
        hist_src = cv.calcHist([self.src], [0], None, [256], [0, 256])

        # Create a layout with 2 rows and 3 columns for displaying images and their histograms.
        f, axs = plt.subplots(2, 3, figsize=(20, 8))

        # First row: original image, histogram-equalized image (dst), and CLAHE-processed image (dst2).
        axs[0, 0].imshow(self.src, cmap='gray')
        axs[0, 0].set_title('Original Image')
        axs[0, 1].imshow(self.dst, cmap='gray')
        axs[0, 1].set_title('Equalized Image')
        axs[0, 2].imshow(self.dst2, cmap='gray')
        axs[0, 2].set_title('CLAHE Image')

        # Second row: histograms of the original image, equalized image, and CLAHE-processed image.
        axs[1, 0].plot(hist_src)
        axs[1, 0].set_title('Histogram of Original Image')
        axs[1, 1].plot(self.hist_dst)
        axs[1, 1].set_title('Histogram of Equalized Image')
        axs[1, 2].plot(self.hist_dst2)
        axs[1, 2].set_title('Histogram of CLAHE Image')

        # Set the x-axis limit for better visualization.
        for ax in axs[1]:
            ax.set_xlim([0, 256])

        # Show the plot.
        plt.tight_layout()
        plt.show()


# Example usage:
if __name__ == '__main__':
    image_path = 'lena.png'  # Using the updated path for the image.
    histogram_equalization = HistogramEqualization(image_path)
    histogram_equalization.perform_histogram_equalization()
    histogram_equalization.perform_clahe()
    histogram_equalization.display_results()
