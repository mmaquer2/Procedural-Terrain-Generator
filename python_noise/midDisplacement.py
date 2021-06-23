import random
from math import floor
from collections import deque

def main():
    size = 512
    heightmap = [[0]*size for i in range(size)]

    heightmap[0][0] = random.randint(0, 256)
    heightmap[size - 1][0] = random.randint(0, 256)
    heightmap[0][size - 1] = random.randint(0, 256)
    heightmap[size - 1][size - 1] = random.randint(0, 256)

    q = deque()
    q.append((0, 0, size - 1, size - 1, 200))

    while len(q) != 0:
        top, left, bottom, right, randomness = q.popleft()

        centerX = (left + right) // 2
        centerY = (top + bottom) // 2

        heightmap[centerX][top] = (heightmap[left][top] + heightmap[right][top]) // 2 + random.randint(-randomness, randomness)
        heightmap[centerX][bottom] = (heightmap[left][bottom] + heightmap[right][bottom]) // 2 + random.randint(-randomness, randomness)
        heightmap[left][centerY] = (heightmap[left][top] + heightmap[left][bottom]) // 2 + random.randint(-randomness, randomness)
        heightmap[right][centerY] = (heightmap[right][top] + heightmap[right][bottom]) // 2 + random.randint(-randomness, randomness)

        heightmap[centerX][centerY] = (heightmap[left][top] +
                                       heightmap[right][top] +
                                       heightmap[left][bottom] +
                                       heightmap[right][bottom]) // 4 + \
                                      random.randint(-randomness, randomness)

        if right - left > 2:
            q.append((top, left, centerY, centerX, randomness // 2))
            q.append((top, centerX, centerY, right, randomness // 2))
            q.append((centerY, left, bottom, centerX, randomness // 2))
            q.append((centerY, centerX, bottom, right, randomness // 2))

main()