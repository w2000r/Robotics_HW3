cmake_minimum_required(VERSION 3.0.2)
project(service_common_messages)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
)


# Generate messages in the 'msg' folder
 add_message_files(
    FILES
    Timevector.msg 
 )

 add_service_files(
   FILES
   String.srv
 )

# Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   geometry_msgs
   std_msgs
 )

catkin_package(

  CATKIN_DEPENDS geometry_msgs rospy std_msgs
)

