import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('youtube.jpg')

font = cv.FONT_HERSHEY_SIMPLEX

org = (50, 50)

fontScale = 1

color = (0, 0, 255)

thickness = 2

blur = cv.blur(img, (5, 5))
gauss = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateral = cv.bilateralFilter(img, 9, 75, 75)

plt.subplot(3, 3, 5), plt.imshow(img), plt.title('1')
plt.text(0.05, 0.95, 'Original', horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, color="red")
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 1), plt.imshow(gauss), plt.title('2')
plt.text(0.05, 0.95, 'Gaussian Blur', horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, color="red")
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 3), plt.imshow(median), plt.title('3')
plt.text(0.05, 0.95, 'Median Blur', horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, color="red")
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 7), plt.imshow(bilateral), plt.title('4')
plt.text(0.05, 0.95, 'Bilateral Filter', horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, color="red")
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 9), plt.imshow(blur), plt.title('5')
plt.text(0.05, 0.95, 'Average Blur', horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, color="red")
plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()