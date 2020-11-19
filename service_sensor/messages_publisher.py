#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_messages.msg import Timevector

rospy.init_node('messages_publisher')
pub = rospy.Publisher('messages_msg', Timevector, queue_size=1)
msg = Timevector()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.vector = Vector3(x=second%4, y=second%5, z=second%6)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.vector.x, msg.vector.y, msg.vector.z
    rate.sleep()
