import cv2

img = cv2.imread('solar-system.jpg')
cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )
cv2.putText(img,
            "Mercurio",
            (115,180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,255,0)
            )
cv2.putText(img,
            "Venus",
            (190,180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,0,0)
            )
cv2.putText(img,
            "Terra",
            (290,260),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,0)
            )
cv2.putText(img,
            "Marte",
            (380,260),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,255,255)
            )
cv2.putText(img,
            "Jupiter",
            (490,70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Saturno",
            (790,120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (210,105,30)
            )
cv2.putText(img,
            "Urano",
            (970,130),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (75,0,130)
            )
cv2.putText(img,
            "Netuno",
            (1120,140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (216,191,216)
            )
cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.imshow('resultado',img)







cv2.waitKey(0)

