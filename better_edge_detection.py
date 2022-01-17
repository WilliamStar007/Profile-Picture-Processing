import cv2

# Read the original image
img = cv2.imread(input("image name: "))

# # Display original image
# cv2.imshow('Original', img)
# cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=30, threshold2=100)
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)

result = cv2.bitwise_and(img, img, mask=edges)
cv2.imshow('Result', result)
cv2.waitKey(0)

cv2.destroyAllWindows()
