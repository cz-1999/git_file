
#include <iostream>
#include "Package.h"
using namespace std;

Package::Package(double ounce,double costperounce)
{
    Ounce = ounce>0?ounce:1;
    CostPerOunce = costperounce>0?costperounce:1;

}

Package::~Package()
{

}

double Package::getCostPerOunce()
{
return CostPerOunce;
}

double Package::getOunce()
{
return Ounce;
}

void Package::print()
{
cout<<1<<endl;
}

double Package::calculateCost()
{
    return  Ounce*CostPerOunce;
}
