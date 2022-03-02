#include <iostream>
#include <fstream>
#include <string>

// generates vmd-readable txyz/tinker files
//
// how to run:
// ./compiled_binary file.arc new_file.arc

int main(int agrc, char* argv[]){

//  argv[1] is your arc file, argv[2] is the new arc file
    std::ifstream file(argv[1]);
    std::ofstream out_file(argv[2]);
    
// natoms = number of atoms, line = coordinates + atom index/type + atom connections
    std::string line,natoms;

    std::getline(file,natoms);
//    std::cout << natoms << "\n";

    while (std::getline(file,line)){
          if (line.compare(natoms) == 0){
//              out_file << line << "\n";
          }
          else if (line.length() > 60 && line.compare(40,9,"90.000000") == 0){
              out_file << natoms << "      " << line << std::endl;
          }
          else{
              out_file << line << "\n";
          }
    }
 out_file.close(); 
}
