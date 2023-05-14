import time

class Clock:
    @staticmethod
    def say_time():
        print(time.strftime("%H:%M:%S"))
Clock.say_time()