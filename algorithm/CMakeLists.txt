cmake_minimum_required(VERSION 3.0.2)
project(algorithm)

find_package(catkin REQUIRED COMPONENTS
  common_messages
  geometry_msgs
  rospy
  std_msgs
  message_generation
)

# Generate messages in the 'msg' folder
 add_message_files(
   FILES
   Timevector.msg
 )


# Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   common_messages
   geometry_msgs
   std_msgs
 )

catkin_package(
  CATKIN_DEPENDS common_messages geometry_msgs rospy std_msgs
)


