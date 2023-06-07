import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_left = remaining_time // 60
        seconds_left = remaining_time % 60
        time_left = "{:02d}:{:02d}".format(minutes_left, seconds_left)
        
        print("Remaining time: {}".format(time_left), end="\r")
        time.sleep(1)
    
    print("\nTime's up! Stay focused!")
