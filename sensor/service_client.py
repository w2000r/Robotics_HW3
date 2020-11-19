#!/usr/bin/env python
import rospy
import time
from common_messages.srv import AddTwoNum, AddTwoNumRequest

rospy.init_node('srv_client')
rospy.wait_for_service('add_two_number')
requester = rospy.ServiceProxy('add_two_number', AddTwoNum)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(1)
time = 0
now = rospy.get_rostime()
while time < 180:
    if time % 10 == 0:
        req = AddTwoNumRequest(a=time, b=now.secs)
        res = requester(req)
        print time, "request:", req.a, req.b, "response:", res.sum
    rate.sleep()
    count += 1

