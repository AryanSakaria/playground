#include <iostream>

int main()
{
    int a{};
    std::cout << "Enter a number :";
    std::cin >> a;
    std::cout << "The number you have entered is : " << a << '\n';
    //cout and cin both are buffered

    int x{};
    int y{};
    int z{};
    std::cout << "Enter 2 numbers :";
    // if you enter 3 numbers here without newline
    // the second cin statement wont wait as buffer has an extra variable
    std::cin >> x >> y;
    std::cout << "Enter 1 more number:";
    std::cin >> z;
    std::cout << "Your numbers are " << x << " " << y << " " << z;
    std::cout << "The size of int " << sizeof(int) << '\n';
    return 0;
}