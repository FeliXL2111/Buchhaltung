#include <iostream>
#include <stdlib.h>

int main(){
    std::cout << "backend läuft" << std::endl;
    std::cout << system("curl https://198.168.2.119:8008") << std::endl;
    try
    {
        int m;
        m = system("curl https://198.168.2.119:8008");
        std::cout << m << std::endl;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }

    
    // std::cout << i << std::endl;
}