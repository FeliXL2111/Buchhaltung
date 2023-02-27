#include <iostream>
#include <stdlib.h>
#include <string>

int main(){
    std::cout << "backend läuft" << std::endl;
    std::cout << system("curl http://198.168.2.119:8008/books") << std::endl;
    try
    {
        std::string m;
        m = system("curl http://198.168.2.119:8008/books");
        std::cout << m << std::endl;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }

    
    // std::cout << i << std::endl;
}