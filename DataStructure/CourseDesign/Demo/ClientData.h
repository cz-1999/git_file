#ifndef CLIENTDATA_H_INCLUDED
#define CLIENTDATA_H_INCLUDED

#include <string>
using namespace std;

class ClientData
{
public:
    ClientData(int = 0,const string & = "",const string & = "",double=0.0);

    void setAccountNumber(int);
    int getAccountNumber()const;

    void setLastName(const string &);
    string getLastName()const;

    void setFirstName(const string &);
    string getFirstName()const;

    void setBalance(double);
    double getBalance()const;

private:
    double accountNumber;
    string phoneNumber;

    char firstName[10];//string类型使用不了copy()函数，需要使用字符数组
    char lastName[15];
    double balance;

};


#endif // CLIENTDATA_H_INCLUDED
