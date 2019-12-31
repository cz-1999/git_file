#ifndef BANKDATA_H_INCLUDED
#define BANKDATA_H_INCLUDED
#include <string>
using namespace std;

class BankData
{
public:
    BankData(int = 0,const string & = "",const string & = "",const string & = "",const string & = "",double=0.0,
             const string & = "",const string & = "",const string & = "",const string & = "",double=0.0);

    void setSerialNumber(int);
    int getSerialNumber()const;

    void setAccountNumber(const string &);
    string getAccountNumber()const;

    void setPhoneNumber(const string &);
    string getPhoneNumber()const;

    void setLastName(const string &);
    string getLastName()const;

    void setFirstName(const string &);
    string getFirstName()const;

    void setLoginPassWord(const string &);
    string getLoginPassWord()const;

    void setPinCode(const string &);
    string getPinCode()const;

    void setTime(const string &);
    string getTime()const;

    void setSignBit(const string &);
    string getSignBit()const;

    void setBalance(double);
    double getBalance()const;

    void setBalanceChanges(double);
    double getBalanceChanges()const;

private:
    int serialNumber;
    string accountNumber;
    string phoneNumber;

    char firstName[10];//string类型使用不了copy()函数，需要使用字符数组
    char lastName[15];
    double balance;

    string loginPassWord;//登录密码
    string pinCode;//取款密码

    string signBit;
    double balanceChanges;
    string time;

    //string ID;
    //string ;
   // string ;
};

#endif // BANKDATA_H_INCLUDED
