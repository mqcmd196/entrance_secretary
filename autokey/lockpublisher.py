import subprocess
import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import Bool

from autokey import Autokey

publish_rate = 2
face_detect = None

class ROSKey:
    def __init__(self, rate=publish_rate):
        rospy.init_node('door')
        self.pub = rospy.Publisher('/door/key', String, queue_size = 1)
        rospy.Subscriber('/faceclassifier/string', String, face_detect_cb)
        self.door_key = Autokey()
        self.rate = rospy.Rate(rate)
    
    def face_detect_cb(self, msg):
        global face_detect
        face_detect = msg


if __name__ == '__main__':
    try:
        key_obj = ROSKey()

        while not rospy.is_shutdown():
            key_obj.pub.publish(key_obj.door_key.state)

            if face_detect == 'owner':
                key_obj.door_key.open()
                subprocess.check_call('python3 ../google_assistant/texttotalk.py --device-id "Pi" --device-model-id "RaspberryPi4" --lang "ja-JP"', shell=True)
                time.sleep(30)

            elif face_detect == 'face':
                key_obj.door_key.open()
                time.sleep(30)
            
            key_obj.door_key.lock()
            time.sleep(2)

    except rospy.ROSInterruptException:
        pass