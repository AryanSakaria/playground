#include <iostream>

int add(int x, int y);

int main()
{
    int x{};
    std::cin >> x;
    int y{};
    std::cin >> y;
    std::cout << add(x,y) << '\n';
    return 0;
}

int add(int x, int y)
{
    int sum{x + y};
    return sum;
}