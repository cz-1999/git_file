#ifndef PACKAGE_H_INCLUDED
#define PACKAGE_H_INCLUDED
#include <string>
using namespace std;

class Package
{
public:
Package(double=0,double=0);
virtual ~Package();

virtual void print();
virtual double calculateCost();

double getOunce();
double getCostPerOunce();


private:
double Ounce;
double CostPerOunce;


};



#endif // PACKAGE_H_INCLUDED
