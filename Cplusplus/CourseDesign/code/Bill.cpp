#include <iostream>
#include <string>
#include "Bill.h"
using namespace std;

Bill::Bill(const string &a,const string &sign,double change,double balanceValue,const string &d,const string &h)
    :accountNumber(a),signBit(sign),balanceChanges(balance),balance(balanceValue),timeday(d),timehour(h)
{

}

void Bill::setAccountNumber(const string &a)
{
    accountNumber = a;
}
string  Bill::getAccountNumber() const
{
    return accountNumber;
}

void Bill::setSignBit(const string &sign)
{
    signBit = sign;
}
string  Bill::getSignBit() const
{
    return signBit;
}

void Bill::setTimeHour(const string &t)
{
    timehour = t;
}
string  Bill::getTimeHour() const
{
    return timehour;
}

void Bill::setTimeDay(const string &t)
{
    timeday = t;
}
string  Bill::getTimeDay() const
{
    return timeday;
}

void Bill::setBalance(double balanceValue)
{
    balance = balanceValue;
}
double Bill::getBalance()const
{
    return balance;
}

void Bill::setBalanceChanges(double Changes)
{
    balanceChanges = Changes;
}
double Bill::getBalanceChanges()const
{
    return balanceChanges;
}
