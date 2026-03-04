import cv2

# afficher une image en couleur ou en noir blanc
img = cv2.imread("img/bird.jpg", 0)
print(img.shape)

cv2.imshow("image test", img)
k = cv2.waitKey(0)

#utiliser une touche pour sauvégarder une image
if k == ord("s"):
# Comment sauvégarder une image sous un autre format (png, jpg)
 cv2.imwrite("img/bird_as_png.png", img)
 print('image sauvegarder')

#detruire l'image si la bonne touche n'est pas tapée
else :
 cv2.destroyAllWindows()
 print('image detruite')
 

#automatiser un évènement avec une touche du cclavier

