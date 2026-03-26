import cv2
import matplotlib.pyplot as plt


#Voici une liste de méthodes que nous allons utiliser pour faire du template matching
METHODS = [
    "TM_SQDIFF" ,
    "TM_SQDIFF_NORMED",
    "TM_CCORR"  ,
    "TM_CCORR_NORMED"  ,
    "TM_CCOEFF"  ,
    "TM_CCOEFF_NORMED"
]

def draw_matches(matches, img):
    draw_img = img.copy()
    for match in matches:
        x1, y1, x2, y2 = match["bbox"]
        draw_img = cv2.rectangle(draw_img, (x1, y1), (x2, y2), (0,0,0), 3)
        draw_img = cv2.putText(
            img=draw_img,
            text=f"{match['template']}:{match['score']:.2f}",
            org=(x1-5, y1-10),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(0,0,0),
            thickness=3     
        )
    return draw_img

def detect_piece():

    #Chargé les images
    
    #image d'ensemble
    img = cv2.imread("img/chess table.jpg")
    #conversion en gris
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #IMAGE A REPERER
    piece = "white Tower"
    template = cv2.imread("img/Tower chess.jpg", cv2.IMREAD_GRAYSCALE)

    #enregistrer les dimension de la templates 
    h, w = template.shape

    #On va parcourrir la liste de méthode pour appliquer chaque technique:
    for method in METHODS:
        cv2_method = getattr(cv2, method)
        matches = []
        res = cv2.matchTemplate(img_gray, template, cv2_method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if cv2_method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            point = min_loc
            score = min_val
        else:
            point = max_loc
            score = max_val

        matches.append({
            "template": piece,
            "score": score,
            "bbox": (point[0], point[1], point[0]+w, point[1]+h)
        })

        img_display = draw_matches(matches, img)

        plt.figure(figsize=(10, 8))
        plt.subplot(121)
        plt.imshow(cv2.cvtColor(img_display, cv2.COLOR_BGR2GRAY))
        plt.title(f"Template Matching Result : {method}")

        plt.subplot(122)
        plt.imshow(res, cmap="gray")
        plt.title(f"Match Scores {method}")
        plt.show()

if __name__== "__main__":
    detect_piece()


