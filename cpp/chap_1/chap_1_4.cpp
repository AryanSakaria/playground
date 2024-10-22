#include <iostream>

int main()
{
    [[maybe_unused]] int a; //default
    [[maybe_unused]] int b = 5; //copy init
    [[maybe_unused]] int c(6); // direct -> not good, because confuse with function
    // direct list strict on data type
    int d {7}; // direct list init
    int e {}; //value - init
    // int f {7.5};// gives error
    // std::cout << a << std::endl;
    std::cout << d << "\n"; // faster than endl which flushes the buffer
    std::cout << e << std::endl;
}