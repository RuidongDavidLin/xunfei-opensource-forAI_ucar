#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 劫持cmd_vel修改算法在转弯时的问题

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from dynamic_reconfigure.msg import DoubleParameter,Config
from dynamic_reconfigure.srv import Reconfigure,ReconfigureRequest


def callback_vel(msg):
    global n 
    global k_x
    global k_z

    msg_amplify=Twist()
    if n < 23:
        msg_amplify.linear.x = msg.linear.x * 1000
        # msg_amplify.linear.y = 0 
        # msg_amplify.linear.z = 0
        # msg_amplify.angular.x = 0
        # msg_amplify.angular.y = 0
        msg_amplify.angular.z = msg.angular.z
        #print("times :   "+str(n))
        n=n+1
    else:
        msg_amplify.linear.x = msg.linear.x * k_x
        # msg_amplify.linear.y = 0 
        # msg_amplify.linear.z = 0
        # msg_amplify.angular.x = 0
        # msg_amplify.angular.y = 0
        msg_amplify.angular.z = msg.angular.z *k_z

    pub.publish(msg_amplify)
    


def callback_odom(msg):
    global flag
    global k_x
    global k_z
    
    if msg.pose.pose.position.y < -2.5 and flag==0:
        flag = 1
        k_x = 1.6
        k_z = 3.2
    elif msg.pose.pose.position.x >2 and flag==1:
        flag = 2
        k_x = 2#
        k_z = 5 # 
        
    elif msg.pose.pose.position.x < 5 and flag==2 and msg.pose.pose.position.y < -5:
        # setparam.set_parameters()
        flag = 3
        k_x = 2.7
        k_z = 5
        
    elif msg.pose.pose.position.x < 1.5 and flag==3:
        flag = 4
        k_x = 3.5
        k_z = 1
    elif msg.pose.pose.position.x < 0.8 and flag==4:
        flag = 5
        k_x = 0
        k_z = 0
    else:
        pass


class SetVelocityScaling(object):
    def __init__(self):
        self.request = ReconfigureRequest()
        self.set_parameters_client = rospy.ServiceProxy('/move_base/global_costmap/inflation_layer/set_parameters', Reconfigure)
    
    # 只写了3个参数，其他参数也一样，不过需要看看数据类型是什么
    def set_parameters(self):
        config_empty = Config()
        
        set_params_temp = DoubleParameter()
        set_params_temp.name = 'cost_scaling_factor'
        set_params_temp.value = 6
        self.request.config.doubles.append(set_params_temp)

        set_params_temp = DoubleParameter()
        set_params_temp.name = 'inflation_radius'
        set_params_temp.value = 1
        self.request.config.doubles.append(set_params_temp)
        
        print(self.request.config)
        self.set_parameters_client.call(self.request)
        self.request.config = config_empty




if __name__=="__main__":
    n = 1
    flag = 0

    k_x = 1.55
    k_z = 3.2
    
    rospy.init_node('hijack_vel')
    sub_vel=rospy.Subscriber('/cmd_vel2',Twist,callback=callback_vel)
    sub_odom=rospy.Subscriber('/odom',Odometry,callback=callback_odom)
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    setparam = SetVelocityScaling()

    rospy.spin()
