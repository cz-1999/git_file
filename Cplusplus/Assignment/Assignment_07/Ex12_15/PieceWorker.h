#ifndef PIECEWORKER_H_INCLUDED
#define PIECEWORKER_H_INCLUDED
#include <iostream>
#include <string>
#include "Employee.h"
using namespace std;

class PieceWorker : public Employee
{
public:
PieceWorker(const string &,const string &,const string &,double =0.0,double =0.0);
virtual ~PieceWorker(){}

void setPieces(double);
double getPieces() const;

void setWage(double);
double getWage() const;

virtual double earnings() const override;
virtual void print() const override;

private:
    double wage;
    double pieces;
};



#endif // PIECEWORKER_H_INCLUDED
