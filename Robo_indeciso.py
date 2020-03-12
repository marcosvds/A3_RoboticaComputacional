:
#! /usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

#Velocidade linear
v = 0.1  

#Definindo distância
dist = None 

def scaneou(dado):
    global dist #Definindo distância como uma variável global
    dist = np.array(dado.ranges).round(decimals=2)[0]

if __name__=="__main__":
    rospy.init_node("etapa_6")
    velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
    recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)

    try:
        while not rospy.is_shutdown():
            print(dist)
            if dist < 1.02:
                velocidade = Twist(Vector3(-0.1, 0, 0), Vector3(0, 0, 0))
                velocidade_saida.publish(velocidade)
                rospy.sleep(2)
            else:
                velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0))
                velocidade_saida.publish(velocidade)
                rospy.sleep(2)
                    
    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")