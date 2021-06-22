#include<iostream>
#include <vector>
#include <string>
#include<fstream>


using namespace std;

void CreateRandomHeightMap(int width, int height) {



    ofstream myfile;
    myfile.open ("test.ppm");

    int r = 0;
    int g = 0;
    int b = 0;

    myfile << "P3" << endl;
    myfile << width << " " << height << endl;
    myfile << "255" << endl;

    for (int i = 0; i < width; ++i) {
        for (int j = 0; j < height ; ++j) {
            int randomColor = rand() % 255;
            r = randomColor;
            g = randomColor;
            b = randomColor;
            myfile << r << " " << g << " " << b << endl;
       

        }
     
    };

    myfile.close();

    cout << "create new image file" << endl;


}

int main() {

    CreateRandomHeightMap(512,512);

    return 0;


}