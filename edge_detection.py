import cv2
import matplotlib.pyplot as plt

# read the image
image = cv2.imread(input("image name: "))

# convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show the grayscale image
plt.imshow(gray, cmap="gray")
plt.show()

# perform the canny edge detector to detect image edges
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
