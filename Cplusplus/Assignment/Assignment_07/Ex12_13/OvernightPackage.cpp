
#include <iostream>
#include "OvernightPackage.h"
using namespace std;

OvernightPackage::OvernightPackage(double ounce,double costperounce,double additionalfee)
:Package(ounce,costperounce)                //һ��Ҫ�ó�ʼ����Ա�б��ʼ�������򷵻صļ���ֵ����
{
AdditionalFee = additionalfee>0?additionalfee:1;
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
cout<<2<<endl;
}
