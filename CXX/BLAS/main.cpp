#include <iostream>
#include <random>
#include <vector>



int main(int argc, char** argv)
{
    std::default_random_engine dre;
    std::uniform_int_distribution<int> di(10,20);
    for(int i=0; i<20; ++i) {
        std::cout<< di(dre) << " ";
    }
    std::cout<< std::endl;
}