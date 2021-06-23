import array
 
 
width = 256
height = 128
maxVal = 256
image = array.array('B', [0, 0, 0] * width * height)

#counter array 



image = array.array('B', [0, 0, 235] * width * height)

f = open("test.ppm", "w")

f.write("P3\n")
f.write(str(width))
f.write(" ")
f.write(str(height) + "\n")

f.write(str(maxVal) + "\n")
        
image.tofile(f)

print(image)