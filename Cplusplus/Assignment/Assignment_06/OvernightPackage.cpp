
#include <iostream>
#include "OvernightPackage.h"
using namespace std;

OvernightPackage::OvernightPackage(const string &namesend,const string &addresssend,const string &namereceive,const string &addressreceive,
                 const string &postalcode,double ounce,double costperounce,double additionalfee)
:Package(namesend,addresssend,namereceive,addressreceive,postalcode,ounce,costperounce)                //һ��Ҫ�ó�ʼ����Ա�б��ʼ�������򷵻صļ���ֵ����
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
