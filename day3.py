import numpy as np

# Max number in each spiral:
# 1 9 25 49
# x[n] = max num in spiral
# n = spiral num
# x[0] = 1
# x[n] = x[n-1] + n * 8
#

FINAL = 312051


def themethod():
    x = 0
    y = 0
    mov = 1
    amt = 1
    while True:
        for _ in range(0, mov):
            amt = amt + 1
            x = x + 1
            if amt == FINAL:
                return x, y
        for _ in range(0, mov):
            amt = amt + 1
            y = y + 1
            if amt == FINAL:
                return x, y
        mov = mov + 1
        for _ in range(0, mov):
            amt = amt + 1
            x = x -1
            if amt == FINAL:
                return x, y
        for _ in range(0, mov):
            amt = amt + 1
            y = y -1
            if amt == FINAL:
                return x, y
        mov = mov + 1

x, y = themethod()
print("position: ({}, {}), sum: {}".format(x, y, x + y))


def themethod2():
    x = 300
    y = 300
    mov = 1
    arr = np.zeros((600, 600))
    arr[x, y] = 1
    while True:
        for _ in range(0, mov):
            x = x + 1
            amt = np.sum(arr[x-1:x+2, y-1:y+2])
            arr[x,y] = amt
            if amt > FINAL:
                return amt
        for _ in range(0, mov):
            y = y + 1
            amt = np.sum(arr[x - 1:x + 2, y - 1:y + 2])
            arr[x,y] = amt
            if amt > FINAL:
                return amt
        mov = mov + 1
        for _ in range(0, mov):
            x = x - 1
            amt = np.sum(arr[x - 1:x + 2, y - 1:y + 2])
            arr[x,y] = amt
            if amt > FINAL:
                return amt
        for _ in range(0, mov):
            y = y - 1
            amt = np.sum(arr[x - 1:x + 2, y - 1:y + 2])
            arr[x, y] = amt
            if amt > FINAL:
                return amt
        mov = mov + 1

amt = themethod2()
print('the amount is {}'.format(amt))
