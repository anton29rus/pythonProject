from time import sleep

class TrafficLight:
    __color = 'NOTHING'

    def running(self):
        print("RED")
        sleep(8)
        print("YEALOW")
        sleep(2)
        print("GREEN")
        sleep(8)

TrafficLight = TrafficLight()
TrafficLight.running()