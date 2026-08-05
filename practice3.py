import time

def count_down(start, end = 0):
    
    for x in reversed(range(end, start + 1)):
        print(x)
        time.sleep(1)
    print("Finished!")

count = int(input("Enter the countdown time in seconds: "))

count_down(count)