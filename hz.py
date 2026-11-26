import time

ages = [20, 21, 19]
x = 0

while True:
    try:
        print(ages[x])
        x += 1
    except IndexError:
        break
    time.sleep(0.5)