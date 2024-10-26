#include<iomanip>
#include<iostream>

int main()
{
    std::cout << std::left;
    std::cout << std::setw(16) << "bool" << sizeof(bool) << " bytes\n";
    std::cout << std::setw(16) << "int"  << sizeof(int) << " bytes\n";
    std::cout << std::setw(16) << "long" << sizeof(long) << " bytes\n";


}