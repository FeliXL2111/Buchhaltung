#include <iostream>

std::string toBinary(int n){
    std::string r;
    while (n != 0)
    {
        r += (n%2 == 0 ? "0" : "1");
        n /= 2;
    }
    return r;
};

int main(){
    char t = 'A';
    bool m = 0;
    int i = int(t);
    std::cout << i;
    std::string r = toBinary(i);
    std::cout << r;
    std::cout << r.length();
    std::string r_new = '0' + r;
    std::cout << r_new;
}