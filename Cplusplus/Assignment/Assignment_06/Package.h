#ifndef PACKAGE_H_INCLUDED
#define PACKAGE_H_INCLUDED
#include <string>
using namespace std;

class Package
{
public:
Package(const string &,const string &,const string &,const string &,const string &,double=0,double=0);
virtual ~Package();

virtual void print();
virtual double calculateCost();

double getOunce();
double getCostPerOunce();


private:
double Ounce;
double CostPerOunce;
string nameSend;
string addressSend;
string nameReceive;
string addressReceive;
string PostalCode;


};



#endif // PACKAGE_H_INCLUDED
