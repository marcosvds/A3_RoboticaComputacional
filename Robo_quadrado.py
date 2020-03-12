#! /usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan
from math import pi

if __name__=="__main__":

		rospy.init_node("roda_exemplo")

		velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )

		while not rospy.is_shutdown():
			vel_frente = Twist(Vector3(0.1,0,0), Vector3(0,0,0.01))
			vel_parado = Twist(Vector3(0,0,0), Vector3(0,0,0))
			vel_curva = Twist(Vector3(0,0,0), Vector3(0,0, pi/10))

			velocidade_saida.publish(vel_parado)
			print('stop')
			rospy.sleep(2)

			velocidade_saida.publish(vel_frente)
			print('forward')
			rospy.sleep(5.2)
			
			velocidade_saida.publish(vel_parado)
			print('stop')
			rospy.sleep(2)
			
			velocidade_saida.publish(vel_curva)
			print('curvation')
			rospy.sleep(5)
	