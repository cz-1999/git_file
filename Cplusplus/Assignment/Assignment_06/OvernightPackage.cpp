
#include <iostream>
#include "OvernightPackage.h"
using namespace std;

OvernightPackage::OvernightPackage(const string &namesend,const string &addresssend,const string &namereceive,const string &addressreceive,
                 const string &postalcode,double ounce,double costperounce,double additionalfee)
:Package(namesend,addresssend,namereceive,addressreceive,postalcode,ounce,costperounce)                //一定要用初始化成员列表初始化，否则返回的计算值错误
{
AdditionalFee = additionalfee>=0?additionalfee:1;
}

OvernightPackage::~OvernightPackage()
{

}

double OvernightPackage::calculateCost()
{
    return  getOunce()*(getCostPerOunce()+AdditionalFee);
}

void OvernightPackage::print()
{
Package::print();
}
