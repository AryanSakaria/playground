#include <string>
#include <iostream>

int main()
{
    std::cout << "Enter your full name: ";
    std::string name {};
    std::getline(std::cin >> std::ws, name);
    std::cout << "Enter your age : ";
    int age{};
    std::cin >> age;
    int total_length{static_cast<int>(name.length()) + age};
    std::cout << "Your age + length of name is: " << total_length << '\n';
    return 0;

}
