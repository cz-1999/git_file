#ifndef TWODAYPACKAGE_H_INCLUDED
#define TWODAYPACKAGE_H_INCLUDED

#include "Package.h"
#include <string>
using namespace std;

class TwoDayPackage : public Package
{
public:
    TwoDayPackage(const string &,const string &,const string &,const string &,const string &,double=0,double=0,double=0);
    virtual ~TwoDayPackage();

    virtual void print();
    virtual double calculateCost();

private:
    double FlatShippingFee;
};

#endif // TWODAYPACKAGE_H_INCLUDED
