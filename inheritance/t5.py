from time import time, localtime
class Clock:
    @staticmethod
    def say_time():
        currentTime = localtime(time())
        print(f"{currentTime.tm_hour} : {currentTime.tm_min} : {currentTime.tm_sec}")
Clock.say_time()