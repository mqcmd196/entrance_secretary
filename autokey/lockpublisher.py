import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool

from autokey import Autokey

face_detect = None

def face_detect_cb(self, msg):
    global face_detect
    face_detect = msg


if __name__ == '__main__':
    try:
        rospy.init_node('door')
        pub = rospy.Publisher('/door/key', String, queue_size = 1)
        door_key = Autokey()
        rate = rospy.Rate(2)

        while not rospy.is_shutdown():
            pub.publish(door_key.state)
            rate.sleep()

    except:
        pass