#LE SEUILLAGE : Méthode de binarisation d'une image (deux couleurs)
import cv2

img = cv2.imread("img/img-tuto4.jpg", 0)

#Pour le seuillage Binaire
_, thres1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("image_seuillée", thres1)

#seuilllage avec trunkature
_, thres2 = cv2.threshold(img, 255, 255, cv2.THRESH_TRUNC)
cv2.imshow("image_Trunké", thres2)

#Seuillage intelligent
thres3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 2)

#affichage de l'image seuillée
cv2.imshow("image_seuillée_intélligement", thres3)
k = cv2.waitKey(0)

#utiliser une touche pour sauvégarder une image
if k == ord("s"):
# Comment sauvégarder une image sous un autre format (png, jpg)
 cv2.imwrite("img/seuillage_picture.png", thres3)
 print('image sauvegarder')

#detruire l'image si la bonne touche n'est pas tapée
else :
 cv2.destroyAllWindows()
 print('image detruite')

