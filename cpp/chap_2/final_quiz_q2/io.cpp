#include "io.h"
#include<iostream>

int readNumber()
{
    std::cout << " Enter your number:";
    int x{};
    std::cin >> x;
    return x;
}
int writeAnswer(int x)
{
    std::cout << "The answer is " << x << '\n';
    return 0;
}