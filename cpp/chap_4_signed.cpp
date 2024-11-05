#include<iostream>

int main()
{
    unsigned int s{2};
    int v{-1};
    if(v < s)
    {
        std::cout << "This wont happen because signed converts to unsigned\n";
    }
    else
    {
        std::cout << "C++ kinda wonky \n";
    }
    return 0;
}