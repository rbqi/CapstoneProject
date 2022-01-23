#   Import the time module
import time


#   Define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

#   Input time in seconds
t = 5

#   Function call
countdown(int(t))
print("Good Luck!")
