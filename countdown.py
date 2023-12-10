# import the time module
import time


def countdown(t):

    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '\t {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print(timer)


# input time in seconds
t = int(input("Enter the time (seconds): "))

countdown(t)
