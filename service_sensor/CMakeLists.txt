cmake_minimum_required(VERSION 3.0.2)
project(service_sensor)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs  
  rospy
  std_msgs
  message_generation
)
# Generate messages in the 'msg' folder
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

