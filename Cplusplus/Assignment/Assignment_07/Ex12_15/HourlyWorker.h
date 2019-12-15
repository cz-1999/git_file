#ifndef HOURLYWORKER_H_INCLUDED
#define HOURLYWORKER_H_INCLUDED
#include <iostream>
#include <string>
#include "Employee.h"
using namespace std;

class HourlyWorker : public Employee
{
public:
HourlyWorker(const string &,const string &,const string &,double =0.0,double =0.0);
virtual ~HourlyWorker(){}

void setHours(double);
double getHours() const;

void setWage(double);
double getWage() const;

virtual double earnings() const override;
virtual void print() const override;

private:
    double wage;
    double hours;
};


#endif // HOURLYWORKER_H_INCLUDED
