#!/usr/bin/env python
import rospy
from service_common_messages.srv import String, StringResponse

def service_callback(request):
    response = StringResponse(c = "5 seconds elapsed")
    print("request data: {}, {} response: {}".format(request.a, request.b, response.c))
    return response


rospy.init_node('service_server')
service = rospy.Service('string', String, service_callback)
rospy.spin()
