import random
import numpy as np
from math import floor
from PIL import Image
from collections import deque

class GraphicsGenerator:

    mapWidth = 0
    mapHeight = 0

    def __init__(self, width, height):
        self.mapWidth = width
        self.mapHeight = height
        self.finalHeightMap = []
        


    #create a height map with a perlin noise algorithim 
    def createPerlinHeightMap(self):
        
        #create a temp variable to hold the width of our noise map
        size = self.mapWidth

        heightMap = [[0]* size for i in range(size)] 

        heightMap[0][0] = random.randint(0, 256)
        heightMap[size - 1][0] = random.randint(0, 256)
        heightMap[0][size - 1] = random.randint(0, 256)
        heightMap[size - 1][size - 1] = random.randint(0, 256)

        q = deque()
        q.append((0, 0, size - 1, size - 1, 200))

        while len(q) != 0:
            top, left, bottom, right, randomness = q.popleft()

            centerX = (left + right) // 2
            centerY = (top + bottom) // 2

            heightMap[centerX][top] = (heightMap[left][top] + heightMap[right][top]) // 2 + random.randint(-randomness, randomness)
            heightMap[centerX][bottom] = (heightMap[left][bottom] + heightMap[right][bottom]) // 2 + random.randint(-randomness, randomness)
            heightMap[left][centerY] = (heightMap[left][top] + heightMap[left][bottom]) // 2 + random.randint(-randomness, randomness)
            heightMap[right][centerY] = (heightMap[right][top] + heightMap[right][bottom]) // 2 + random.randint(-randomness, randomness)

            heightMap[centerX][centerY] = (heightMap[left][top] +
                                        heightMap[right][top] +
                                        heightMap[left][bottom] +
                                        heightMap[right][bottom]) // 4 + \
                                        random.randint(-randomness, randomness)

            if right - left > 2:
                q.append((top, left, centerY, centerX, randomness // 2))
                q.append((top, centerX, centerY, right, randomness // 2))
                q.append((centerY, left, bottom, centerX, randomness // 2))
                q.append((centerY, centerX, bottom, right, randomness // 2))

        #pass our heightmap to our class variables
        self.finalHeightMap = heightMap
        print(self.finalHeightMap)
              

    def createHeightMapImage(self):
        # PPM header values
        maxval = 255
        #convert int header values to strings
        tempWidth = str(self.mapWidth)
        tempHeight = str(self.mapHeight)
        tempMax = str(maxval)

        #write the PPM file headers to the file
        f = open("PerlinPPM.ppm", "w")
        f.write("P3\n")
        f.write(tempWidth + " ")
        f.write(tempHeight + "\n")
        f.write(tempMax + "\n")
        
        #iterate through our height map
        for i in range(len(self.finalHeightMap)):
            for j in range(len(self.finalHeightMap[i])):
               tempIntPixel = self.finalHeightMap[i][j]
               tempStrPixel = str(tempIntPixel)
               f.write(tempStrPixel + "\n")
        
        
        #lastly, close our file once complete
        f.close()
        
    
def main():
    print("================= starting terrain generator program================")
    
    ##gather user input
    ##width = input("Enter a map Width ")
    ##height = input("Enter a map Height: ")
    
    ##create instance of our graphics generator class
    myTerrainMap = GraphicsGenerator(65,65)
    
    #create a perlin noise height map
    myTerrainMap.createPerlinHeightMap()

    #convert our noise map into a ppm image
    myTerrainMap.createHeightMapImage()

    ##gerneate a png file from our ppm file


main()