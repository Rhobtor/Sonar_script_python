
import rospy
from std_msgs.msg import Float32
from brping import Ping1D


# myPing = Ping1D()
# myPing.connect_serial("/dev/ttyUSB0", 115200)
# if myPing.initialize() is False:
#     print("Failed to initialize Ping!")
#     exit(1)
# data = myPing.get_distance()


# data2=data["distance"]
# falta meterlo en un bucle porque solo coje un valor 
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 115200)
def data_pub():
    rospy.init_node("sonar_pub_node")
    pub = rospy.Publisher("data",Float32, queue_size=10)
    rate=rospy.Rate(5)
    while not rospy.is_shutdown():

        if myPing.initialize() is False:
            print("Failed to initialize Ping!")
            exit(1)
        data = myPing.get_distance()
        data2=data["distance"]
        pub.publish(data2)

        rate.sleep()

if __name__ == '__main__':
    try:
        data_pub()

    except rospy.ROSInterruptException:
        pass

while True:
    data = myPing.get_distance()
    if data:
            data2=data["distance"]
    time.sleep(0.1)
