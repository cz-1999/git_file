#include <bits/stdc++.h>
#include <conio.h>
#include "BankData.h"
#include "Bill.h"
using namespace std;

vector<BankData>& LoadBankData();
void SaveBankData(vector<BankData>& bankdatas);

vector<string>& LoadAccount(vector<string>& accounts);
void SaveAccount(vector<string>& accounts);

void SaveBill(vector<Bill> &bills);

string Login(vector<BankData>& bankdatas);
void   Login();

void MainMenu(vector<BankData> &bankdatas,vector<Bill> &bills,vector<string>& accounts);

void BankForegroundSubMenu(vector<BankData> &bankdatas,vector<string>& accounts);
void openAnAccount(vector<BankData> &bankdatas,vector<string>& accounts);
void closeAnAccount(vector<BankData> &bankdatas,vector<string>& accounts);
void Search(vector<BankData> &bankdatas);
void BrowseUserInformation(vector<BankData> &bankdatas);
void ModifyPhoneNumber(vector<BankData> &bankdatas);

void AccountProcessSubMenu(vector<BankData>& bankdatas,vector<Bill> &bills);
void saveWithdrawMonkey(vector<BankData>& bankdatas,string,vector<Bill> &bills);

void CustomerSelfHelpSubMenu(vector<BankData>& bankdatas,vector<Bill> &bills);
void ChangePassword(vector<BankData>& bankdatas,string);
void CheckBalance(vector<BankData>& bankdatas,string);
void BrowseStatements(vector<Bill> &bills,string account);


int main()
{
int serialNumber=0;
string accountNumber;
string phoneNumber;
char firstName[10];//string����ʹ�ò���copy()��������Ҫʹ���ַ�����
char lastName[15];
string loginPassWord;
string pinCode;
string signBit;
string timeday;
string timehour;
double balance=0;
double balanceChanges;
vector<BankData> bankdatas;
vector<Bill> bills;
vector<string> accounts;
ifstream inFromFile;
ofstream outFromFile;
BankData bankdata;
Bill bill;

if(!inFromFile||!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}


    //cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
    //<<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;
inFromFile.open("bankData.txt",ios::in);
while(inFromFile>>serialNumber>>accountNumber>>lastName>>firstName>>phoneNumber>>balance>>loginPassWord>>pinCode)
{
    //cout<<left<<setw(20)<<serialNumber<<setw(20)<<accountNumber<<setw(20)<<lastName<<setw(20)<<firstName<<setw(20)
   // <<phoneNumber<<setw(20)<<balance<<setw(20)<<loginPassWord<<right<<setw(15)<<pinCode<<endl;
    bankdata.setAccountNumber(accountNumber);
    bankdata.setSerialNumber(serialNumber);
    bankdata.setLastName(lastName);
    bankdata.setFirstName(firstName);
    bankdata.setPhoneNumber(phoneNumber);
    bankdata.setBalance(balance);
    bankdata.setLoginPassWord(loginPassWord);
    bankdata.setPinCode(pinCode);

    bankdatas.push_back(bankdata);
}
inFromFile.close();

inFromFile.open("bill.txt",ios::in);
while(inFromFile>>accountNumber>>signBit>>balanceChanges>>balance>>timeday>>timehour)
{
    bill.setAccountNumber(accountNumber);
    bill.setSignBit(signBit);
    bill.setBalanceChanges(balanceChanges);
    bill.setBalance(balance);
    bill.setTimeDay(timeday);
    bill.setTimeHour(timehour);

    bills.push_back(bill);
}
inFromFile.close();
LoadAccount(accounts);
MainMenu(bankdatas,bills,accounts);

outFromFile.open("bankData.txt",ios::out);//��дios::in bankdatas�����֮ǰ�ᱻ���
for(BankData bankdata:bankdatas)
{
    outFromFile<<bankdata.getSerialNumber()<<" "<<bankdata.getAccountNumber()<<" "
    <<bankdata.getLastName()<<" "<<bankdata.getFirstName()<<" "<<bankdata.getPhoneNumber()<<" "
    <<bankdata.getBalance()<<" "<<bankdata.getLoginPassWord()<<" "<<bankdata.getPinCode()<<endl;
}
outFromFile.close();
return 0;
}

vector<BankData>& LoadBankData()
{
int serialNumber=0;
string accountNumber;
string phoneNumber;
char firstName[10];//string����ʹ�ò���copy()��������Ҫʹ���ַ�����
char lastName[15];
string loginPassWord;
string pinCode;
string signBit;
string time;
double balance=0;
vector<BankData> bankdatas;

fstream inoutFromFile;
BankData bankdata;

if(!inoutFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

inoutFromFile.open("bankData.txt",ios::in);
while(inoutFromFile>>serialNumber>>accountNumber>>lastName>>firstName>>phoneNumber>>balance>>loginPassWord>>pinCode)
{
   // cout<<serialNumber<<" "<<accountNumber<<" "<<lastName<<" "<<firstName<<" "
    //<<phoneNumber<<" "<<balance<<" "<<loginPassWord<<" "<<pinCode<<endl;
    bankdata.setAccountNumber(accountNumber);
    bankdata.setSerialNumber(serialNumber);
    bankdata.setLastName(lastName);
    bankdata.setFirstName(firstName);
    bankdata.setPhoneNumber(phoneNumber);
    bankdata.setBalance(balance);
    bankdata.setLoginPassWord(loginPassWord);
    bankdata.setPinCode(pinCode);
    bankdatas.push_back(bankdata);
}
inoutFromFile.close();

vector<BankData> &bankdatase = bankdatas;

return bankdatase;
}

vector<string>& LoadAccount(vector<string>& accounts)
{
string account;
ifstream inFromFile;

inFromFile.open("account.txt",ios::in);
if(!inFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

while(inFromFile>>account)
{
    accounts.push_back(account);
}
inFromFile.close();

for(string account:accounts)
    cout<<account<<endl;

return accounts;
}

void SaveAccount(vector<string>& accounts)
{
ofstream outFromFile;
outFromFile.open("account.txt",ios::out);//��дios::in bankdatas�����֮ǰ�ᱻ���
if(!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

for(string account:accounts)
{
    outFromFile<<account<<endl;
}
outFromFile.close();
}


void SaveBill(vector<Bill> &bills)
{

ofstream outFromFile;
if(!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

outFromFile.open("bill.txt",ios::out);//��дios::in bankdatas�����֮ǰ�ᱻ���
for(Bill bill:bills)
{
    outFromFile<<bill.getAccountNumber()<<" "<<bill.getSignBit()<<" "<<bill.getBalanceChanges()<<" "
    <<bill.getBalance()<<" "<<bill.getTimeDay()<<" "<<bill.getTimeHour()<<endl;
}
outFromFile.close();
}

void SaveBankData(vector<BankData> &bankdatas)
{

ofstream outFromFile;
if(!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

outFromFile.open("bankData.txt",ios::out);//��дios::in bankdatas�����֮ǰ�ᱻ���

for(BankData bankdata:bankdatas)
{
    outFromFile<<bankdata.getSerialNumber()<<" "<<bankdata.getAccountNumber()<<" "
    <<bankdata.getLastName()<<" "<<bankdata.getFirstName()<<" "<<bankdata.getPhoneNumber()<<" "
    <<bankdata.getBalance()<<" "<<bankdata.getLoginPassWord()<<" "<<bankdata.getPinCode()<<endl;
}
outFromFile.close();
}

void Login()
{
ifstream inFromFile;
ofstream outFromFile;
string accountNumber;
string loginPassWord;
string accountcopy;
bool f=false,faccount=false;
vector<string> accounts;
vector<string> passWords;

if(!inFromFile||!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

inFromFile.open("admin.txt",ios::in);
while(inFromFile>>accountNumber>>loginPassWord)
{
    accounts.push_back(accountNumber);
    passWords.push_back(loginPassWord);
}
inFromFile.close();

label2: cout<<"Please use your account to login:\n";
cin>>accountcopy;
for(string account:accounts)
{
    if(account==accountcopy)
    {
        faccount=true;
        label: cout<<"Please input your login password:\n";
        int i=0;
        char d,code[20]="\0";
        while((d=getch()) != '\r')
        {
            code[i] = d;
            i++;
            if(d!='\b')    //�������ݲ����˸�ʱ����ʾ ��*����
            {
            printf("*");
            }
            else     //�����������˸�ʱ ɾ��ǰһ�� ��*����
            {
            printf("\b \b");
            }
        }

        for(string passWord:passWords)
        {
            if(passWord==code&&account==accountcopy)
                {
                    f=true;
                    system("cls");
                    break;
                }
        }
        if(f)
            break;
        else
            goto label;

    }

}
if(!faccount)
    goto label2;
}

string Login(vector<BankData>& bankdatas)
{
BankData bankdata;
string account;
string code;
bool f=false,faccount=false;

loop: cout<<"Please use your bank card number or mobile phone number to login:\n";
cin>>account;
for(BankData bankdata:bankdatas)
{

    if(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account)
    {
        faccount=true;
        label: cout<<"Please input your login password:\n";

        int i=0;
        char d,code[20]="\0";
        while((d=getch()) != '\r')
        {
            code[i] = d;
            i++;
            if(d!='\b')    //�������ݲ����˸�ʱ����ʾ ��*����
            {
            printf("*");
            }
            else     //�����������˸�ʱ ɾ��ǰһ�� ��*����
            {
            printf("\b \b");
            }
        }

        for(BankData bankdata:bankdatas)
        {
            if(bankdata.getLoginPassWord()==code
               &&(bankdata.getAccountNumber()==account
               ||bankdata.getPhoneNumber()==account))
                {
                    f=true;
                    system("cls");
                    break;
                }
        }
        if(f)
            break;
        else
            goto label;

    }

}
if(!faccount)
    goto loop;
return account;
}

void MainMenu(vector<BankData> &bankdatas,vector<Bill> &bills,vector<string>& accounts)
{
while(true)
{
cout<<"-------------------------------------------------\n"
    <<"-------Banking Business Processing System--------\n\n"
    <<"1.Banking Foreground Processing System-----------\n"
    <<"2.Account Processing Subsystem-------------------\n"
    <<"3.Bank Customer Self-Help System-----------------\n"
    <<"4.exit-------------------------------------------\n";
int choice=0;
loop: cout<<"Please input your choices\n";
cin>>choice;
switch(choice)
    {
    case 1:BankForegroundSubMenu(bankdatas,accounts);break;
    case 2:AccountProcessSubMenu(bankdatas,bills);break;
    case 3:CustomerSelfHelpSubMenu(bankdatas,bills);break;
    case 4:exit(0);
    default:goto loop;
    }
}

}

void BankForegroundSubMenu(vector<BankData> &bankdatas,vector<string>& accounts)
{
Login();
while(true)
{
bool f=false;
cout<<"------Banking Foreground Processing System-------\n\n"
    <<"1.Open An Account--------------------------------\n"
    <<"2.Close An Account-------------------------------\n"
    <<"3.Search for user information--------------------\n"
    <<"4.Browse user information------------------------\n"
    <<"5.Modify bank reserved mobile phone number-------\n"
    <<"6.Return To The Previous Level-------------------\n"
    <<"7.Exit-------------------------------------------\n";
int choice=0;
loop: cout<<"Please input your choices\n";
cin>>choice;
switch(choice)
    {
    case 1:openAnAccount(bankdatas,accounts);break;
    case 2:closeAnAccount(bankdatas,accounts);break;
    case 3:Search(bankdatas);break;
    case 4:BrowseUserInformation(bankdatas);break;
    case 5:ModifyPhoneNumber(bankdatas);break;
    case 6:system("cls");f=true;break;
    case 7:exit(0);
    default:goto loop;
    }
if(f)
    break;

}
}

void openAnAccount(vector<BankData> &bankdatas,vector<string>& accounts)
{
    int serialNumber=0;
    string accountNumber;
    string phoneNumber;
    char firstName[10];//string����ʹ�ò���copy()��������Ҫʹ���ַ�����
    char lastName[15];
    string loginPassWord;
    string pinCode;
    string signBit;
    string time;
    double balance=0;
    ifstream inFromFile;
    BankData bankdata;
    int number;
    number=rand()%accounts.size();

    loop: cout<<"Please input the account of account number,last name,first name,"
        <<"phone number,balance,login password,pin code\n";
    cin>>serialNumber>>accountNumber>>lastName>>firstName>>phoneNumber>>balance>>loginPassWord>>pinCode;


    for(BankData bankdata:bankdatas)
    {
        if(bankdata.getAccountNumber()==accountNumber)
        {
            cout<<"The account already exists\n";
            goto loop;
        }
    }
    accountNumber=accounts[number];

    bankdata.setAccountNumber(accountNumber);
    bankdata.setSerialNumber(serialNumber);
    bankdata.setLastName(lastName);
    bankdata.setFirstName(firstName);
    bankdata.setPhoneNumber(phoneNumber);
    bankdata.setBalance(balance);
    bankdata.setLoginPassWord(loginPassWord);
    bankdata.setPinCode(pinCode);
    bankdatas.push_back(bankdata);
    cout<<"Account has been created\nCurrent accounts are: \n";
    cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
    <<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;

    for(BankData bankdata:bankdatas)
    {
        cout<<left<<setw(20)<<bankdata.getSerialNumber()<<setw(20)<<bankdata.getAccountNumber()<<setw(20)
        <<bankdata.getLastName()<<setw(20)<<bankdata.getFirstName()<<setw(20)<<bankdata.getPhoneNumber()<<setw(20)
        <<bankdata.getBalance()<<setw(20)<<bankdata.getLoginPassWord()<<right<<setw(15)<<bankdata.getPinCode()<<endl;
    }
    system("pause");
    system("cls");

    vector<string>::iterator it;
    for(it=accounts.begin();it!=accounts.end();)
    {
        if(*it==accountNumber)
        {
            it=accounts.erase(it);
        }
        else
            ++it;
    }

    SaveAccount(accounts);
    SaveBankData(bankdatas);
}

void closeAnAccount(vector<BankData> &bankdatas,vector<string>& accounts)
{

string account;
bool faccount = false;

loop: cout<<"Please enter the account or mobile number to delete\n";
cin>>account;

vector<BankData>::iterator it;
for(it=bankdatas.begin();it!=bankdatas.end();)
{
    if(it->getAccountNumber()==account||it->getPhoneNumber()==account)
    {
        faccount=true;
        it=bankdatas.erase(it);
        break;
    }
    else
        ++it;
}
if(!faccount)
{
cout<<"The account does not exist\n";
goto loop;
}

for(BankData bankdata:bankdatas)
{
   if(bankdata.getPhoneNumber()==account)
   {
        account==bankdata.getAccountNumber();
        break;
   }
}
accounts.push_back(account);

cout<<"Account has been deleted\nCurrent accounts are: \n";
cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
<<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;

for(BankData bankdata:bankdatas)
{
    cout<<left<<setw(20)<<bankdata.getSerialNumber()<<setw(20)<<bankdata.getAccountNumber()<<setw(20)
    <<bankdata.getLastName()<<setw(20)<<bankdata.getFirstName()<<setw(20)<<bankdata.getPhoneNumber()<<setw(20)
    <<bankdata.getBalance()<<setw(20)<<bankdata.getLoginPassWord()<<right<<setw(15)<<bankdata.getPinCode()<<endl;
}


system("pause");
system("cls");
SaveAccount(accounts);
SaveBankData(bankdatas);
}

void Search(vector<BankData> &bankdatas)
{
string account;
bool f=false;
cout<<"Please enter the account number or mobile phone number of the user to inquire"<<endl;
cin>>account;

cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
<<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;
for(BankData bankdata:bankdatas)
{
    if(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account)
    {
        cout<<left<<setw(20)<<bankdata.getSerialNumber()<<setw(20)<<bankdata.getAccountNumber()<<setw(20)
        <<bankdata.getLastName()<<setw(20)<<bankdata.getFirstName()<<setw(20)<<bankdata.getPhoneNumber()<<setw(20)
        <<bankdata.getBalance()<<setw(20)<<bankdata.getLoginPassWord()<<right<<setw(15)<<bankdata.getPinCode()<<endl;
        f=true;
        break;
    }
}
if(!f)
    cout<<"this user does not exist\n";
system("pause");
system("cls");
}
void BrowseUserInformation(vector<BankData> &bankdatas)
{
cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
<<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;

for(BankData bankdata:bankdatas)
{
    cout<<left<<setw(20)<<bankdata.getSerialNumber()<<setw(20)<<bankdata.getAccountNumber()<<setw(20)
    <<bankdata.getLastName()<<setw(20)<<bankdata.getFirstName()<<setw(20)<<bankdata.getPhoneNumber()<<setw(20)
    <<bankdata.getBalance()<<setw(20)<<bankdata.getLoginPassWord()<<right<<setw(15)<<bankdata.getPinCode()<<endl;
}
system("pause");
system("cls");
}

void ModifyPhoneNumber(vector<BankData> &bankdatas)
{
    string account;
    string phone;
    bool f=false;
    cout<<"Please enter the account number or mobile phone number of the user to be modified\n";
    cin>>account;
    for(BankData &bankdata:bankdatas)
{
    if(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account)
    {
        cout<<"Please enter a new phone number\n";
        cin>>phone;
        bankdata.setPhoneNumber(phone);
        cout<<"The modification is completed.\n The modified mobile phone number is: \n";
        cout<<bankdata.getPhoneNumber()<<endl;
        f=true;
        SaveBankData(bankdatas);
        break;
    }

}

if(!f)
    cout<<"this user does not exist\n";
system("pause");
system("cls");

}
void AccountProcessSubMenu(vector<BankData>& bankdatas,vector<Bill> &bills)
{
string account;
account=Login(bankdatas);
while(true)
{
bool f=false;
cout<<"------Account processing subsystem-------\n\n"
    <<"1.Save Withdraw Money----------------------------\n"
    <<"2.Transfer Money---------------------------------------\n"
    <<"3.Return To The Previous Level-------------------\n"
    <<"4.Exit-------------------------------------------\n";
int choice=0;
loop: cout<<"Please input your choices\n";
cin>>choice;
switch(choice)
    {
    case 1:saveWithdrawMonkey(bankdatas,account,bills);break;
    case 2:break;
    case 3:system("cls");f=true;break;
    case 4:exit(0);
    default:goto loop;
    }
if(f)
    break;

}
}

void saveWithdrawMonkey(vector<BankData>& bankdatas,string account,vector<Bill> &bills)
{
string signBit;
string code;
string timeday,timehour;
double change=0;
bool f=false;
Bill bill;

for(BankData &bankdata:bankdatas)
{
    if(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account)
    {

        loop: cout<<"Please input a signBit + or - and your change\n";
        cin>>signBit>>change;
        if(signBit=="+")
        {
            cout<<"Previous balance is: "<<endl;
            cout<<bankdata.getBalance()<<endl;

            bankdata.setBalance(bankdata.getBalance()+change);
            cout<<"Now balance is: "<<endl;
            cout<<bankdata.getBalance()<<endl;
            bill.setAccountNumber(bankdata.getAccountNumber());
            bill.setSignBit(signBit);
            bill.setBalanceChanges(change);
            bill.setBalance(bankdata.getBalance());

            time_t tt = time(NULL);//��䷵�ص�ֻ��һ��ʱ��cuo
            tm* t= localtime(&tt);
            timeday = to_string(t->tm_year + 1900)+"-"+to_string(t->tm_mon + 1)+"-"+to_string(t->tm_mday);
            timehour = to_string(t->tm_hour)+":"+to_string(t->tm_min)+":"+to_string(t->tm_sec);

            bill.setTimeDay(timeday);
            bill.setTimeHour(timehour);
            bills.push_back(bill);

            cout<<"The balance has increased: "<<change<<endl;
            system("pause");
            system("cls");
            SaveBankData(bankdatas);
            SaveBill(bills);
            f=true;
            break;
        }
        else if(signBit=="-")
        {
        label: cout<<"Please input your pin code:\n";
        cin>>code;
        if(bankdata.getPinCode()==code&&(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account))
           {
            cout<<"Previous balance is: "<<endl;
            cout<<bankdata.getBalance()<<endl;

            bankdata.setBalance(bankdata.getBalance()-change);
            cout<<"Now balance is: "<<endl;
            cout<<bankdata.getBalance()<<endl;
            bill.setAccountNumber(bankdata.getAccountNumber());
            bill.setSignBit(signBit);
            bill.setBalanceChanges(change);
            bill.setBalance(bankdata.getBalance());

            time_t tt = time(NULL);//��䷵�ص�ֻ��һ��ʱ��cuo
            tm* t= localtime(&tt);
            timeday = to_string(t->tm_year + 1900)+"-"+to_string(t->tm_mon + 1)+"-"+to_string(t->tm_mday);
            timehour = to_string(t->tm_hour)+":"+to_string(t->tm_min)+":"+to_string(t->tm_sec);

            bill.setTimeDay(timeday);
            bill.setTimeHour(timehour);
            bills.push_back(bill);

            SaveBankData(bankdatas);
            SaveBill(bills);

            cout<<"The balance has reduced: "<<change<<endl;
            system("pause");
            system("cls");

            f=true;
            break;
           }
        if(f)
            break;
        else
            goto label;
        }
        else
            goto loop;
    }
if(f)
    break;
}

}

void CustomerSelfHelpSubMenu(vector<BankData>& bankdatas,vector<Bill> &bills)
{
string account=Login(bankdatas);
while(true)
{
bool f=false;
cout<<"------Bank Customer Self-Service System-------\n\n"
    <<"1.Change Password--------------------------------\n"
    <<"2.Check Balances-------------------------------\n"
    <<"3.Browse Statements-------------------------------\n"
    <<"4.Return To The Previous Level-------------------\n"
    <<"5.Exit-------------------------------------------\n";
int choice;
loop: cout<<"Please input your choices\n";
cin>>choice;
switch(choice)
    {
    case 1:ChangePassword(bankdatas,account);break;
    case 2:CheckBalance(bankdatas,account);break;
    case 3:BrowseStatements(bills,account);break;
    case 4:system("cls");f=true;break;
    case 5:exit(0);
    default:goto loop;
    }
if(f)
    break;

}

}

void ChangePassword(vector<BankData>& bankdatas,string account)
{
string choice;
string passWordFirst,passWordSecond;

label: cout<<"1.Change Login Password----------\n"
    <<"2.Change Pin Code----------------\n"
    <<"Please input your choice: \n";
cin>>choice;
if(choice=="1")
{
loop: cout<<"Please input your new login password"<<endl;
cin>>passWordFirst;
cout<<"Please confirm your login password"<<endl;
cin>>passWordSecond;
if(passWordFirst==passWordSecond)
{
    cout<<"Login Password reset complete"<<endl;
    system("pause");
    system("cls");
    for(BankData &bankdata:bankdatas)
    {
        if(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account)
        {
            bankdata.setLoginPassWord(passWordSecond);
            SaveBankData(bankdatas);
            break;
        }
    }
}
else
{
    cout<<"Different passwords entered twice"<<endl;
    goto loop;
}
}
else if(choice=="2")
{
label2: cout<<"Please input your new pin code"<<endl;
cin>>passWordFirst;
cout<<"Please confirm your pin code"<<endl;
cin>>passWordSecond;
if(passWordFirst==passWordSecond)
{
    cout<<"Pin Code reset complete"<<endl;
    system("pause");
    system("cls");
    for(BankData &bankdata:bankdatas)
    {
        if(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account)
        {
            bankdata.setPinCode(passWordSecond);
            SaveBankData(bankdatas);
            break;
        }
    }
}
else
{
    cout<<"Different passwords entered twice"<<endl;
    goto label2;
}
}

else
    goto label;
}

void CheckBalance(vector<BankData>& bankdatas,string account)
{
    cout<<"The balance in the account is now: "<<endl;
    for(BankData &bankdata:bankdatas)
    {
        if(bankdata.getAccountNumber()==account||bankdata.getPhoneNumber()==account)
        {
            cout<<bankdata.getBalance()<<endl;
            system("pause");
            system("cls");
            break;
        }
    }

}

void BrowseStatements(vector<Bill> &bills,string account)
{

cout<<left<<setw(20)<<"account"<<setw(20)<<"sign bit"<<setw(20)<<"balance change"<<setw(20)<<"balance"<<right<<setw(15)<<"time"<<endl;
for(Bill bill:bills)
{
    if(bill.getAccountNumber()==account)
    {
        cout<<left<<setw(20)<<bill.getAccountNumber()<<setw(20)<<bill.getSignBit()<<setw(20)<<bill.getBalanceChanges()<<setw(20)
        <<bill.getBalance()<<right<<setw(15)<<bill.getTimeDay()<<" "<<bill.getTimeHour()<<endl;
    }
}
system("pause");
system("cls");

}
