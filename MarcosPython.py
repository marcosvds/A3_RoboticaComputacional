# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:23:48 2020

@author: Marcos Vinícius da Silva
"""
# Importando bibliotecas
import cv2

# Abrindo arquivos
#cap = cv2.VideoCapture('VID_20200302_063445951.mp4')
cap = cv2.VideoCapture('VID_20200302_063554327.mp4')
#cap = cv2.VideoCapture('VID_20200302_063719050.mp4')

# Abrindo janela
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == False:
        print("Codigo de retorno FALSO - problema para capturar o frame")

    # Our operations on the frame come here
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',frame) # imshow já inverte BGR para RGB
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fechando janela
cap.release()
cv2.destroyAllWindows()
