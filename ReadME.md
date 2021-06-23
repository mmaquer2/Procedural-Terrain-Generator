# Procedural Terrain Generator 

* this repo demonstrates procedrual terrain with a randomly created height map, the graphics pipeline is WebGL (three.js) and python.

## How it works: 
* First, a 3D graphics context is created with the WebGL framework three.js, then a flat plane is created to be textured over to demonstarte the perlin noise generator. Once the blank mesh plane is created a randomly mid point displacement height map created with a python algorhtim will add heigh to the plane mesh.

# running the program:
* Note, ensure you have node.js and the node package manager installed on your computer,
* To run the code, download the repo, cd into the the file directory and run "npm install" to install the web dependencies then run "npm run dev" to load the program into a local host web server. You can zoom in and out of the file 

# Changing height map and color texture on the mesh plane
* To change the heightmaps or create a height map edit line script.js line 26 variable heightMap, to the heightmap png file of your choosing. You can run the Perlin Noise Genreator function to create a random height map or otherwise add one to the static directory and load it there. To change the color texture, add the file to the static file and change the filename under TextureImage varaible on script.js line 28.

# Creating a new height map
* To generate a new height map, under the TerrainMapMaker file, run the python program that will create a new ppm height map based on your height and width specifcations. 


# Credits and Resources:
Thanks to Daniel Shiffman of Coding train for its perlin noise tutorials and Gary Simon of Creative academy for its three.js begineer tutorials. 


* https://learn.64bitdragon.com/articles/computer-science/procedural-generation/the-diamond-square-algorithm
* https://mrl.cs.nyu.edu/~perlin/paper445.pdf
* https://mrl.cs.nyu.edu/~perlin/noise/
* https://threejs.org/
* Creating Terrain in Three JS, https://www.youtube.com/watch?v=2AQLMZwQpDo&t=1113s
* Perlin Noise Intro, https://rtouti.github.io/graphics/perlin-noise-algorithm*
* Perlin Noise Demo by Coding Train, https://www.youtube.com/watch?v=8ZEMLCnn8v0