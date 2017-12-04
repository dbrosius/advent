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
