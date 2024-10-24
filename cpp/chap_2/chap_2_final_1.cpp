#include <iostream>

int readNumber();
int writeAnswer(int x);

int main()
{
    int x{readNumber()};
    int y{readNumber()};
    writeAnswer(x + y);
    return 0;
}
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