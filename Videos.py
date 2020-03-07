# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:47:06 2020

@author: Enrico Damiani
"""

import cv2
import numpy as np
import sys
import math

def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged

def Calc_reta (P1, P2):
    Coef_ang = ((P2[1] - P1[1]) / (P2[0] - P1[0]))
    Coef_lin = (P1[1] - (Coef_ang * P1[0]))
    return (round(Coef_ang,2), round(Coef_lin,2))

def Encontra_ponto (reta1, reta2):
    X = int(((reta1[1] - reta2[1]) / (reta2[0] - reta1[0])))
    Y = int((reta1[0] * X) + reta1[1])
    return (X,Y)

cap = cv2.VideoCapture('VID_20200302_063445951.mp4')
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

hsv1_f = np.array([30,50,50], dtype=np.uint8)
hsv2_f = np.array([40, 255, 255], dtype=np.uint8)

while(True):

    ret, frame = cap.read()
    
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    maskf = cv2.inRange(img_gray, 210, 255)
    not_mask = cv2.bitwise_not(maskf)
    res = cv2.bitwise_and(img_gray,img_gray, mask = not_mask)
    res2 = cv2.bitwise_and(frame,frame, mask= maskf)
    img_mask = cv2.cvtColor(res, cv2.COLOR_GRAY2RGB)
    final = cv2.bitwise_or(res2, img_mask)

    blur = cv2.GaussianBlur(maskf,(5,5),0)
    bordas = auto_canny(blur) 


    lines_list = []
    lines_list = cv2.HoughLinesP(bordas, 8, math.pi/10.0, 40, np.array([]), 100, 5)
    if lines_list is not None:
        if len(lines_list) >= 2: 
            print(lines_list[0],lines_list[1] )
            for i in lines_list[0,:]:
                if maskf [i[1]] [i[0]] == 255:
                    cv2.line(final, (i[0], i[1]), (i[2],i[3]), (0, 255, 0), 5, cv2.LINE_AA)
                    reta1 = Calc_reta((i[0], i[1]), (i[2],i[3]))
                    reta2 = Calc_reta(((i+1)[0], (i+1)[1]), ((i+1)[2],(i+1)[3]))
                    Ponto = Encontra_ponto(reta1,reta2)
                    cv2.circle((final,Ponto[0],Ponto[1]),2,(0,255,0),3)
               # lista_X1.append(i[1])
                #lista_Y1.append(i[0])
                #lista_X2.append(i[3])
                #lista_Y2.append(i[2])
        #print(len(lista_X1))
        #if len(lista_X1) >=2:
         #   cv2.line(final, (lista_X1[0], lista_Y1[1]), (lista_X2[2],lista_Y2[3]), (0, 255, 0), 5, cv2.LINE_AA)
          #  reta1 = Calc_reta((lista_X1[0], lista_Y1[0]), (lista_X2[0],lista_Y2[0]))
           # reta2 = Calc_reta((lista_X1[1], lista_Y1[1]), (lista_X2[1],lista_Y2[1]))
            #Ponto = Encontra_ponto(reta1,reta2)
            #cv2.circle(final,(i[0],i[1]),2,(0,255,0),3)
                #lista_posix.append(int(i[0]))
                #lista_posiy.append(int(i[1]))
                #cv2.circle(final,(i[0],i[1]),i[2],(0,255,0),2)
                #cv2.circle(final,(i[0],i[1]),2,(0,255,0),3)
    

    # Display the resulting frame
    cv2.imshow('frame',final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
