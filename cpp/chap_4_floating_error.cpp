#include <iomanip>
#include <iostream>

int main()
{
	std::cout << std::setprecision(17);
	double d1{1.0};
	std::cout << d1 << '\n';

	double d2{ 0.1 * 10};
	std::cout << d2 << '\n';

	double d3{ 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1};
	std::cout << d3 << '\n';
	return 0;
}
