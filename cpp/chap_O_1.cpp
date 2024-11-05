#include<iostream>
#include<bitset>

int main()
{
	std::bitset<8> bits{0b000'0001};
	std::cin >> bits;
	std::cout << bits << '\n';
	bits.set(3);
	std::cout << bits << '\n';
}
