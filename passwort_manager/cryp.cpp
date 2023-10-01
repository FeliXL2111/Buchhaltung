#include <iostream>
#include <fstream>
#include <string>

std::string toBinary(int n){
    std::string r;
    int i;
    while (n != 0)
    {
        r += (n%2 == 0 ? "0" : "1");
        n /= 2;
    }
    i = 8-r.length();
    while (i > 0){
        r = '0' + r;
        i -= 1;
    }
    std::cout << r + '\n';
    return r;
};

std::string readFile(){
    std::string line;
    std::string t;
    std::ifstream myfile ("main.db");
    if (myfile.is_open()){
        while (getline(myfile, line)){
            t += line + '\n';
        }
        myfile.close();
    }
    else{
        std::cout << "Unable to open file";
    }
    std::cout << t;
    return t;
}


int main(){
    // char t = 'A';
    // bool m = 0;
    // int i = int(t);
    // std::cout << i + '\n';
    // std::string r = toBinary(i);
    // std::cout << r + '\n';
    // std::cout << r.length() + '\n';
    // std::string r_new = '0' + r;
    // std::cout << r_new + '\n';
    std::string ct;
    std::string intt;
    ct = readFile();
    for (int i = 0; i<ct.length();i++){
        intt += toBinary(int(ct[i]));
        // std::cout << int(ct[i]) << ct[i] << i << '\n';
    };
    std::cout << intt;
}