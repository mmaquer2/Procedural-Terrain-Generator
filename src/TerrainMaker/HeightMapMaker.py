import noise
import numpy as np
from scipy.misc import toimage

def createMap(width, height):
    #set the dimensions of our height map image
    shape = (width,height)
    #number determines at what distance to view the noisemap.
    scale = 40.0
    #the number of levels of detail
    octaves = 30
    #adjusts amplitude
    persistence = 0.5
    #Determines how much detail is added or removed at each octave
    lacunarity = 1.0

    #create an empty array of zeros
    world = np.zeros(shape)

    #create add noise to our image based on the scale we have provided 
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i/scale, 
                                        j/scale, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        repeatx=width, 
                                        repeaty=height, 
                                        base=0)
            
    toimage(world).show()

def main():
    print("==================== Creating a Radnom Height Map===================")
    width = input("Enter a Image Width: ")
    height = input("Enter a Image Height: ")
    createMap(width, height)

main()