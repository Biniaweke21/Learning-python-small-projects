import time

def countdown(t):
    stop_mid = str(input(" "))
    while t > 0:
        mins, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, seconds)

        print(timer, end='\r')

        if stop_mid == "e":
            break
        time.sleep(1)
        t -= 1
    
    print("times up!")

seconds_from_user = int(input("Enter seconds for countdown: "))

countdown(seconds_from_user)