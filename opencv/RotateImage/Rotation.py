import cv2

image = cv2.imread(r'A:\UnityProjects\SNS\Python\Main\imgs\1.jpg')

# first option - analogue
height, width = image.shape[:2]
# get the center of the image
center_x, center_y = (width/2, height/2)
# rotate the imagey
M = cv2.getRotationMatrix2D((center_x, center_y), 90, 1.0)
rotated_image = cv2.warpAffine(image, M, (width, height))


# second option
img_rotate_90_clockwise = cv2.rotate(image, 0)

cv2.imshow("Rotated image", img_rotate_90_clockwise)
cv2.waitKey(0)