
  
# PPM header
width = 256
height = 128
maxval = 255

tempWidth = str(width)
tempHeight = str(height)
tempMax = str(maxval)


f = open("myPPM.ppm", "w")


f.write("P3\n")
f.write(tempWidth + " ")
f.write(tempHeight + "\n")
f.write(tempMax+ "\n")

f.close()


