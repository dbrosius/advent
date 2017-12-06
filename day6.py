INPUT = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'

import numpy as np

data = [int(thenum) for thenum in INPUT.split()]
tried = []
while data not in tried:
    tried.append(data[:])
    maxidx = np.argmax(data)
    maxval = data[maxidx]
    data[maxidx] = 0
    for idx in range(maxidx + 1, maxidx + maxval + 1):
        midx = idx % len(data)
        data[midx] = data[midx] + 1

print('Had to go through {} iterations.'.format(len(tried)))

firsttime = tried.index(data)
print('Cycle length: {}'.format(len(tried) - firsttime))
