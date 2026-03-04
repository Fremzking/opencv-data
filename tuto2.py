import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('img/bird.jpg', 1)
H, W = img.shape[:2]
print(H, W)


#utiliser matplotlib pour placer les axes, les repère et les coordonnées
 
#desinner les lignes
img = cv2.line(img, (0, 0), (0, 200), (255, 0, 0), 5)
img = cv2.line(img, (0, 0), (200, 0), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (0, 0), (200, 200), (255, 255, 0), 5)

pts = np.array([[0, H-1], [W-1, H-1], [W-1, 0]], np.int32)
img = cv2.polylines(img, pts, True, (0, 255, 0), 5)


#affichage des images les commandes de matplotlib
plt.imshow(img[:,:,::-1])
plt.show()

