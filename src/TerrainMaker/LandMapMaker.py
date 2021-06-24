import noise
import numpy as np
from PIL import Image
from scipy.misc import toimage

blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]
shape = shape = (1024,1024)

def add_color(world):
    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            #color parts of the land map based on the values of the array
            if world[i][j] < -0.05:
                color_world[i][j] = blue
            elif world[i][j] < 0:
                color_world[i][j] = beach
            elif world[i][j] < 1.0:
                color_world[i][j] = green
            elif world[i][j] < 0.35:
                color_world[i][j] = mountain
            elif world[i][j] < 1.0:
                color_world[i][j] = snow
    
    toimage(color_world).show()

    return color_world


def createWorld():
    #set the dimensions of our height map image
    shape = (1024,1024)
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
                                        repeatx=1024, 
                                        repeaty=1024, 
                                        base=0)
            
    
    color_world = add_color(world)
    

def main():
    createWorld()

main()