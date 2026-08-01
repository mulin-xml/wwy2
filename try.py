import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('\\\\192.169.3.200\\share\\a.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


sobelx = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
sobel = cv2.addWeighted(sobel, 0.2, img, 0.8, 0)
sobel = cv2.normalize(sobel,None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('1', sobel)
cv2.imshow('img', img)
cv2.waitKey()
