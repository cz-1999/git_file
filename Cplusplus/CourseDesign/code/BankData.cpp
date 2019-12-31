#include <iostream>
#include <string>
#include "BankData.h"
using namespace std;

BankData::BankData(int serial,const string &a,const string &last,const string &first,const string &phone,double balanceValue,
                   const string &login,const string &pin,const string &sign,const string &t,double change)
    :accountNumber(a),balance(balanceValue),serialNumber(serial),phoneNumber(phone),
    loginPassWord(login),pinCode(pin),signBit(sign),time(t)
{
    setFirstName(first);
    setLastName(last);
}

void BankData::setSerialNumber(int serial)
{
    serialNumber = serial;
}
int BankData::getSerialNumber() const
{
    return serialNumber;
}

void BankData::setAccountNumber(const string &a)
{
    accountNumber = a;
}

string  BankData::getAccountNumber() const
{
    return accountNumber;
}

void BankData::setPhoneNumber(const string &phone)
{
    phoneNumber = phone;
}
string  BankData::getPhoneNumber() const
{
    return phoneNumber;
}

void BankData::setLastName(const string &last)
{
    int length = last.size();
    length = (length<15?length:14);
    last.copy(lastName,length);
    lastName[length] = '\0';
}
string BankData::getLastName()const
{
    return lastName;
}

void BankData::setFirstName(const string &first)
{
    int length = first.size();
    length = (length<10?length:9);
    first.copy(firstName,length);
    firstName[length] = '\0';
}
string BankData::getFirstName() const
{
    return firstName;
}

void BankData::setLoginPassWord(const string &login)
{
    loginPassWord = login;
}
string  BankData::getLoginPassWord() const
{
    return loginPassWord;
}

void BankData::setPinCode(const string &pin)
{
    pinCode = pin;
}
string  BankData::getPinCode() const
{
    return pinCode;
}

void BankData::setSignBit(const string &sign)
{
    signBit = sign;
}
string  BankData::getSignBit() const
{
    return signBit;
}

void BankData::setTime(const string &t)
{
    time = t;
}
string  BankData::getTime() const
{
    return time;
}

void BankData::setBalance(double balanceValue)
{
    balance = balanceValue;
}
double BankData::getBalance()const
{
    return balance;
}

void BankData::setBalanceChanges(double Changes)
{
    balanceChanges = Changes;
}
double BankData::getBalanceChanges()const
{
    return balanceChanges;
}
