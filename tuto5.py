import cv2
import numpy as np 

img = cv2.imread("img/img-tuto5.png", 0)

#filtrage-normal
img_blur = cv2.blur(img, (7, 7))

#filtrage-gaussien
img_gaussian = cv2.GaussianBlur(img, (7, 7), 0)

#filtrage-median
img_median = cv2.medianBlur(img, 7)

cv2.imshow("Original", img)
cv2.imshow("img_fluté_simple", img_blur)
cv2.imshow("img_fluté_gaussian", img_gaussian)
cv2.imshow("img_fluté_median", img_median)
k = cv2.waitKey(0)

if k == ord("s"):
# Comment sauvégarder une image sous un autre format (png, jpg)
 cv2.imwrite("img/img_blur.png", img_blur)
 cv2.imwrite("img/img_gaussian.png", img_gaussian)
 cv2.imwrite("img/img_median.png", img_median)

 print('image sauvegarder')

#detruire l'image si la bonne touche n'est pas tapée
else :
 cv2.destroyAllWindows()
 print('image detruite')