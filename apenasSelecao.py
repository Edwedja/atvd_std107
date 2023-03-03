import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Carregue o rastreador
tracker = cv2.TrackerCSRT_create()

# Leia o primeiro quadro do vídeo
returned, img = video.read()

# Selecione a caixa delimitadora na imagem
bbox = cv2.selectROI("Rastreando", img, False)

# Inicialize o rastreador em img e na caixa delimitadora
tracker.init(img, bbox)

print(bbox)

while True:
    check,img = video.read()   

    cv2.imshow("resultado",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido!")
        break


video.release()
cv2.destroyALLwindows()



