#include <iostream>
#include <string>
#include "HourlyWorker.h"

using namespace std;

HourlyWorker::HourlyWorker(const string &first,const string &last,const string &ssn,double w,double h)
    :Employee(first,last,ssn)
{
    setHours(h);
    setWage(w);
}

void HourlyWorker::setHours(double h)
{
    if(h >= 0.0)
        hours = h;
    else
        throw invalid_argument("hours must be >= 0.0");
}
double HourlyWorker::getHours() const
{
    return hours;
}

void HourlyWorker::setWage(double w)
{
    if(w>=0.0)
        wage = w<=40?w:1.5*w;
    else
        throw invalid_argument("hours must be >= 0.0");

}
double HourlyWorker::getWage() const
{
    return wage;
}

double HourlyWorker::earnings() const
{
    return getHours()*getWage();
}

void HourlyWorker::print() const
{
    cout<< "Hourly worker: ";
    Employee::print();
    cout<<"\nwage: "<<getWage()
    <<"; hours: "<<getHours();
}
