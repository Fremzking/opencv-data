import cv2
import numpy as np

img = cv2.imread("img/bird.jpg", 1)
#cv2.imshow("bird", img)
#cv2.waitKey(0)

# Etude des pixels

# Afficher une portion de l'image
"""roi = img[300:470, 570:787]

#créer une image double

img[300:470, 570:787] = roi

cv2.imshow("image coupée", img)
cv2.waitKey(0)"""

#Propriété de l'image

"""dimension = img.shape
print("dimension de l'images (Hauteur, largeur et nb de cannaux):", dimension)

#Determiner le nombre de pixel
nb_pixel = img.size
print("le nombre de pixel correstpond a {}".format(nb_pixel))

#connaitre la nature des éléments qui constitue l'image 
data_type = img.dtype
print("nous avons des {}".format(data_type))"""

#comment afficher juste les pixels d'une seule couleur
