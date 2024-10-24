#include <iostream>

int add(int x, int y)
{
    return x + y;
}

void printValue(int x)
{
    std::cout << x << '\n';
}

int main()
{
    std::cout << "Enter 2 numbers: ";
    int num1{};
    int num2{};
    std::cin >> num1 >> num2;
    printValue(add(num1, num2));
    return 0;
}