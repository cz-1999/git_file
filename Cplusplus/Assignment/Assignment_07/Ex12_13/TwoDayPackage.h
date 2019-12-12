
#ifndef TWODAYPACKAGE_H_INCLUDED
#define TWODAYPACKAGE_H_INCLUDED

#include "Package.h"
class TwoDayPackage : public Package
{
public:
    TwoDayPackage(double=0,double=0,double=0);
    virtual ~TwoDayPackage();

    virtual void print();
    virtual double calculateCost();

private:
    double FlatShippingFee;
};

#endif // TWODAYPACKAGE_H_INCLUDED
