#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>


// finds the mean value of the side_length of the box from arc file for PBC and volume purposes 
// how to run:
// ./compiled_binary file.arc 

float Mean(std::vector<float> array) {
    double sum=0;
    for (int i = 0; i < array.size(); i++)  {
        sum += array[i];
    }
    return sum /array.size();
    }

float stdDev(std::vector<float> array){
    double sum=0;
    for (int i=0;i <array.size();++i){
        sum += pow(array[i]-Mean(array),2);
    }
    return sqrt(sum/array.size());
}


int main(int agrc, char* argv[]){

//  argv[1] is your arc file
    std::ifstream file(argv[1]);

    std::vector <float> side_lengths;
    
// natoms = number of atoms, line = coordinates + atom index/type + atom connections
    std::string line,natoms;

    std::getline(file,natoms);

    while (std::getline(file,line)){
          if (line.length() > 60 && line.compare(40,9,"90.000000") == 0){
              float side = std::stof(line.substr(4,13));
              side_lengths.push_back(side);
          }
    }
//    for (int i=0;i<side_lengths.size();i++){
//        std::cout << side_lengths[i] << std::endl;
//    }
//    std::cout << "   Mean:    " << Mean(side_lengths)   << std::setprecision(3) << std::endl;
//    std::cout << "   STD Dev: " << stdDev(side_lengths) << std::setprecision(3) << std::endl;

      printf("   Mean:       %6.3f \n",Mean(side_lengths));
      printf("   STD Dev:    %6.3f \n",stdDev(side_lengths));

}
