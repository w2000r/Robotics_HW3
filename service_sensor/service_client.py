#!/usr/bin/env python
import rospy
from service_common_messages.srv import String, StringRequest

rospy.init_node('srv_client')
rospy.wait_for_service('string')
requester = rospy.ServiceProxy('string', String)
rate = rospy.Rate(1)
time = 0
count = 180
while count > 0:
    if count%10 == time%10:
        req = StringRequest(a=time, b=count)
        res = requester(req)
        print count, "request:", req.a, req.b, "response:", res.c
    rate.sleep()
    count -= 1
    time += 1
    

