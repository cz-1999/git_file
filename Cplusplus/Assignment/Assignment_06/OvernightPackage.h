#ifndef OVERNIGHTPACKAGE_H_INCLUDED
#define OVERNIGHTPACKAGE_H_INCLUDED
#include "Package.h"
#include <string>
using namespace std;

class OvernightPackage : public Package
{
public:
    OvernightPackage(const string &,const string &,const string &,const string &,const string &,double=0,double=0,double=0);
    virtual ~OvernightPackage();

    virtual void print();
    virtual double calculateCost();

private:
    double AdditionalFee;
};
#endif // OVERNIGHTPACKAGE_H_INCLUDED
