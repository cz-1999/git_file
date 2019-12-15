#include <iostream>
#include <string>
#include "PieceWorker.h"

using namespace std;

PieceWorker::PieceWorker(const string &first,const string &last,const string &ssn,double w,double p)
    :Employee(first,last,ssn)
{
    setPieces(p);
    setWage(w);
}

void PieceWorker::setPieces(double p)
{
    if(p >= 0.0)
        pieces = p;
    else
        throw invalid_argument("pieces must be >= 0.0");
}
double PieceWorker::getPieces() const
{
    return pieces;
}

void PieceWorker::setWage(double w)
{
    if(w>=0.0)
        wage = w;
    else
        throw invalid_argument("hours must be >= 0.0");

}
double PieceWorker::getWage() const
{
    return wage;
}

double PieceWorker::earnings() const
{
    return getPieces()*getWage();
}

void PieceWorker::print() const
{
    cout<< "Piece worker: ";
    Employee::print();
    cout<<"\nwage: "<<getWage()
    <<"; pieces: "<<getPieces();
}
