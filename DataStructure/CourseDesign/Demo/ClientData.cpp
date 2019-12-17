#include <iostream>
#include <string>
#include "ClientData.h"
using namespace std;

ClientData::ClientData(int a,const string &last,const string &first,double balanceValue)
    :accountNumber(a),balance(balanceValue)
{
    setFirstName(first);
    setLastName(last);
}

void ClientData::setAccountNumber(int a)
{
    accountNumber = a;
}
int  ClientData::getAccountNumber() const
{
    return accountNumber;
}

void ClientData::setLastName(const string &last)
{
    int length = last.size();
    length = (length<15?length:14);
    last.copy(lastName,length);
    lastName[length] = '\0';
}
string ClientData::getLastName()const
{
    return lastName;
}

void ClientData::setFirstName(const string &first)
{
    int length = first.size();
    length = (length<10?length:9);
    first.copy(firstName,length);
    firstName[length] = '\0';
}
string ClientData::getFirstName() const
{
    return firstName;
}

void ClientData::setBalance(double balanceValue)
{
    balance = balanceValue;
}
double ClientData::getBalance()const
{
    return balance;
}
