#include <iostream>
#include "TwoDayPackage.h"
using namespace std;

TwoDayPackage::TwoDayPackage(const string &namesend,const string &addresssend,const string &namereceive, const string &addressreceive,
                             const string &postalcode,double ounce,double costperounce,double flatshippingfee)
:Package(namesend,addresssend,namereceive,addressreceive,postalcode,ounce,costperounce)
{
FlatShippingFee = flatshippingfee>=0?flatshippingfee:1;
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
Package::print();
}
