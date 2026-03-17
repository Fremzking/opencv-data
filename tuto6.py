import cv2
import numpy as np

#Methode qui permet de representer les lignes
def display_lines(img, lines):
    for line in lines:
        x1, y1, x2, y2 = line
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(img, (x1, y1), 1, (0, 0, 255), 2)
        cv2.circle(img, (x2, y2), 1, (0, 0, 255), 2)

    cv2.imshow("Les lignes sur l'image", img)
    cv2.waitKey(0)

img = cv2.imread("img/img-tuto6.jpg", 1)
img = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 3))

#Mettre l'image en binaire de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Mettre en evidence les ligne en flutant le reste
gray = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)[1]

#Determiner les lignes
lines = cv2.HoughLinesP(gray, 1, np.pi / 180, 50, minLineLength=80, maxLineGap=20)

#Afficher le nombre de lignes
print(lines.shape)
lines = np.squeeze(lines)

#Appel de la méthode
display_lines(img, lines)

cv2.imshow("image_Orignal", gray)
k=cv2.waitKey(0)

if k == ord("s"):
# Comment sauvégarder une image sous un autre format (png, jpg)
 cv2.imwrite("img/les_lignes.png", img)
 print('image sauvegarder')

#detruire l'image si la bonne touche n'est pas tapée
else :
 cv2.destroyAllWindows()
 print('image detruite')
 

