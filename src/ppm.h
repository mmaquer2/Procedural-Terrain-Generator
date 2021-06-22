#include <iostream>
#include <vector> 

 class ppm {
  	
  
  public:
      //arrays for storing the R,G,B values
      std::vector<unsigned char> r;
      std::vector<unsigned char> g;
      std::vector<unsigned char> b;
  
     
 
     ppm();
     //create a PPM object and fill it with data stored in fname
     ppm(const std::string &fname);
     //create an "epmty" PPM image with a given width and height;the R,G,B arrays are filled with zeros
     ppm(const unsigned int _width, const unsigned int _height);
     //read the PPM image from fname
     void read(const std::string &fname);
     //write the PPM image in fname
     void write(const std::string &fname);
 };
