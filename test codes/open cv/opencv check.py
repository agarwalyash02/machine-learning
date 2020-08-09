import cv2

img=cv2.imread('back.png')

gray=cv2.imread('back.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('dog image',img)
cv2.imshow('gra dog image',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()