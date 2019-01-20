#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

# [field_mapper] maps and contains information on the row 
# locations, lengths, and distances apart using data from 
# (crop_location) access through (field_information)

# This node is a TEMPLATE

def crop_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def field_mapper():
    # Publisher to topic crop_lcation
    pub_field = rospy.Publisher('field_information', String, queue_size=10)

    # Subscribes to topic lidar
    sub_crop = rospy.Subscriber('crop_location', String, crop_callback)

    rospy.init_node('field_mapper')
    rate = rospy.Rate(1) # 1hz
    
    while not rospy.is_shutdown():
        # Publishes "TEST" to course_correct
        message = "TEST"
        pub_field.publish(message)
        #rospy.spin_once()
        rate.sleep()
        

if __name__ == '__main__':
    try:
        field_mapper()
    except rospy.ROSInterruptException:
        pass