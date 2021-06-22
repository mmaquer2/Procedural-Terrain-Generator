## Three js Perlin Noise Terrain Viewer

* this program demonstrates a random perlin noise generator with WebGL (three.js) and c++.

## How it works: 
*First, a 3D graphics context is created with the WebGL framework three.js, then a flat plane is created to be textured over to demonstarte the perlin noise generator. Once the blank mesh plane is created a randomly perlin noise height map created with a c++ algorhtim will add heigh to the plane mesh.

# running the program:
*first ensure you have node.js and the node package manager installed on your computer,
* To run the code, download the repo, cd into the the file directory and run "npm install" to install the web dependencies then run "npm run dev" to load the program into a local host web server. You can zoom in and out of the file 

# Changing height map and color texture
* to change the heightmaps or create a height map edit line script.js line 26 variable heightMap, to the heightmap png file of your choosing. You can run the Perlin Noise Genreator function to create a random height map or otherwise add one to the static directory and load it there. To change the color texture, add the file to the static file and change the filename under TextureImage varaible on script.js line 28.


# Credits and Resources:
Thanks to Daniel Shiffman of Coding train for its perlin noise tutorials and Gary Simon of Creative academy for its three.js begineer tutorials. 

* https://mrl.cs.nyu.edu/~perlin/paper445.pdf
* https://mrl.cs.nyu.edu/~perlin/noise/
* https://threejs.org/
* Creating Terrain in Three JS, https://www.youtube.com/watch?v=2AQLMZwQpDo&t=1113s
* Perlin Noise Intro, https://rtouti.github.io/graphics/perlin-noise-algorithm*
* Perlin Noise Demo by Coding Train, https://www.youtube.com/watch?v=8ZEMLCnn8v0