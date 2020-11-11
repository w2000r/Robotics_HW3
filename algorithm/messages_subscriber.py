#!/usr/bin/env python
import rospy
from common_messages.msg import Timevector

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.vector.x, msg.vector.y, msg.vector.z

rospy.init_node('messages_subscriber')
sub = rospy.Subscriber('messages_msg', Timevector, callback)
rospy.spin()
