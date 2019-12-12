
#include <iostream>
#include "TwoDayPackage.h"
using namespace std;

TwoDayPackage::TwoDayPackage(double ounce,double costperounce,double flatshippingfee)
:Package(ounce,costperounce)
{
FlatShippingFee = flatshippingfee>0?flatshippingfee:1;
}

TwoDayPackage::~TwoDayPackage()
{

}


double TwoDayPackage::calculateCost()
{

    return Package::calculateCost()+FlatShippingFee;
}

void TwoDayPackage::print()
{
cout<<3<<endl;
}
