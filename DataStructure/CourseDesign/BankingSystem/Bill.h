#ifndef BILL_H_INCLUDED
#define BILL_H_INCLUDED
#include <string>
using namespace std;

class Bill
{
public:
    Bill(const string & = "",const string & = "",double=0.0,double=0.0,const string & = "",const string & = "");

    void setAccountNumber(const string &);
    string getAccountNumber()const;

    void setPhoneNumber(const string &);
    string getPhoneNumber()const;

    void setLastName(const string &);
    string getLastName()const;

    void setFirstName(const string &);
    string getFirstName()const;

    void setTimeHour(const string &);
    string getTimeHour()const;

    void setTimeDay(const string &);
    string getTimeDay()const;

    void setSignBit(const string &);
    string getSignBit()const;

    void setBalance(double);
    double getBalance()const;

    void setBalanceChanges(double);
    double getBalanceChanges()const;

private:
    string accountNumber;
    string signBit;
    double balanceChanges;
    double balance;
    string timeday;
    string timehour;

};


#endif // BILL_H_INCLUDED
