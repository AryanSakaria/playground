#include<iostream>

int getValueFromUser()
{
    std::cout << "Enter your number here :";
    int num{};
    std::cin >> num;
    return num;
}

void printHi()
{
    std::cout << "Hi"<< '\n';
}

int main()
{
    int num{getValueFromUser()};
    
    std::cout << num << " doubled is " << num * 2 << '\n';
    printHi();
    return 0;
}