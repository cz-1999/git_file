#include <bits/stdc++.h>
#include <conio.h>
using namespace std;

typedef struct BankData
{
    int serialNumber;
    string accountNumber;
    string phoneNumber;
    string firstName;
    string lastName;
    double balance;
    string loginPassWord;
    string pinCode;
    string signBit;
    double balanceChanges;
    string timeday;
    string timehour;

    struct BankData *next;

}*BankDataList,BankDataNode;


typedef struct Bill
{
    string accountNumber;
    string phoneNumber;
    double balance;
    string signBit;
    double balanceChanges;
    string timeday;
    string timehour;

    struct Bill *next;

}*BillList,BillNode;

typedef struct Admin
{
    string accountNumber;
    string loginPassWord;

    struct Admin *next;
}*AdminList;

void LoadBankData(BankDataList head,array<BankData,1000> *b);
void SaveBankData(BankDataList head);

void LoadBill(BillList head);
void SaveBill(BillList head);

void   Login();
string Login(BankDataList head);

void MainMenu(BankDataList headBankData,BillList headBill,array<BankData,1000> *b);

void BankForegroundSubMenu(BankDataList head,BillList headBill,array<BankData,1000> *b);
void openAnAccount(BankDataList head);
void closeAnAccount(BankDataList head);
void Search(BankDataList head,array<BankData,1000> *b);
void BrowseUserInformation(BankDataList head);
void ModifyPhoneNumber(BankDataList head,BillList headBill);

void AccountProcessSubMenu(BankDataList headBankData,BillList headBill);
void saveWithdrawMonkey(BankDataList headBankData,BillList headBill,string);

void CustomerSelfHelpSubMenu(BankDataList headBankData,BillList headBill);
void ChangePassword(BankDataList head,string);
void CheckBalance(BankDataList head,string);
void BrowseStatements(BillList head,string account);


int main()
{
array<BankData,1000> bankdatas;
for(BankData &bankdata:bankdatas)
{
    bankdata.accountNumber="0";
}
BankDataList headBank;
BillList headBill;
headBank = new BankData;
headBill = new Bill;
headBank->next=nullptr;
headBill->next=nullptr;

LoadBankData(headBank,&bankdatas);
SaveBankData(headBank);
LoadBill(headBill);
SaveBill(headBill);

MainMenu(headBank,headBill,&bankdatas);

return 0;
}

void LoadBankData(BankDataList head,array<BankData,1000> *b)
{
BankDataList p,rear=head;
int serialNumber;
string accountNumber;
string phoneNumber;
string firstName;
string lastName;
double balance;
string loginPassWord;
string pinCode;
string signBit;
string time;
ifstream inFromFile;

if(!inFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}
int i=0;
inFromFile.open("bankData.txt",ios::in);
while(inFromFile>>serialNumber>>accountNumber>>lastName>>firstName>>phoneNumber>>balance>>loginPassWord>>pinCode)
{
    p = new BankData;
    p->accountNumber=accountNumber;
    p->serialNumber=serialNumber;
    p->lastName=lastName;
    p->firstName=firstName;
    p->phoneNumber=phoneNumber;
    p->balance=balance;
    p->loginPassWord=loginPassWord;
    p->pinCode=pinCode;

    (*b)[i].accountNumber=accountNumber;
    (*b)[i].serialNumber=serialNumber;
    (*b)[i].lastName=lastName;
    (*b)[i].firstName=firstName;
    (*b)[i].phoneNumber=phoneNumber;
    (*b)[i].balance=balance;
    (*b)[i].loginPassWord=loginPassWord;
    (*b)[i].pinCode=pinCode;
    ++i;

    rear->next = p;
    rear = p;
}
rear->next=nullptr;
inFromFile.close();

p=head->next;

}
void SaveBankData(BankDataList head)
{
BankDataList p;
ofstream outFromFile;
if(!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

outFromFile.open("bankData.txt",ios::out);//不写ios::in bankdatas在输出之前会被清空

p=head->next;
while(p)
{
    outFromFile<<p->serialNumber<<" "<<p->accountNumber<<" "
    <<p->lastName<<" "<<p->firstName<<" "<<p->phoneNumber<<" "
    <<p->balance<<" "<<p->loginPassWord<<" "<<p->pinCode<<endl;
    p=p->next;
}
outFromFile.close();
}

void LoadBill(BillList head)
{
BillList p,rear=head;
string accountNumber;
string phoneNumber;
double balance;
string signBit;
double balanceChanges;
string timeday;
string timehour;

ifstream inFromFile;

if(!inFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

inFromFile.open("bill.txt",ios::in);
while(inFromFile>>accountNumber>>phoneNumber>>signBit>>balanceChanges>>balance>>timeday>>timehour)
{
    p = new Bill;
    p->accountNumber=accountNumber;
    p->phoneNumber=phoneNumber;
    p->signBit=signBit;
    p->balanceChanges=balanceChanges;
    p->balance=balance;
    p->timeday=timeday;
    p->timehour=timehour;

    rear->next = p;
    rear = p;
}
rear->next=nullptr;

inFromFile.close();
p=head->next;
}
void SaveBill(BillList head)
{
BillList p;
ofstream outFromFile;

outFromFile.open("bill.txt",ios::out);//不写ios::in bankdatas在输出之前会被清空
if(!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

p=head->next;
while(p)
{
    outFromFile<<p->accountNumber<<" "<<p->phoneNumber<<" "<<p->signBit<<" "<<p->balanceChanges<<" "
    <<p->balance<<" "<<p->timeday<<" "<<p->timehour<<endl;
    p=p->next;
}
outFromFile.close();
}

void Login()
{
AdminList head;
head = new Admin;
head->next=nullptr;
AdminList p,p2,rear=head;

ifstream inFromFile;
ofstream outFromFile;
string accountNumber;
string loginPassWord;
string accountcopy;
bool f=false,faccount=false;


inFromFile.open("admin.txt",ios::in);
if(!inFromFile||!outFromFile)
{
cerr<<"File could not be opened."<<endl;
exit(EXIT_FAILURE);
}

while(inFromFile>>accountNumber>>loginPassWord)
{
    p = new Admin;
    p->accountNumber=accountNumber;
    p->loginPassWord=loginPassWord;
    rear->next=p;
    rear=p;
}
rear->next=nullptr;
inFromFile.close();

label2: cout<<"Please use your account to login:\n";
cin>>accountcopy;

p=head->next;


while(p)
{
    if(p->accountNumber==accountcopy)
    {
        faccount=true;
        label: cout<<"Please input your login password:\n";
        int i=0;
        char d,code[20]="\0";
        while((d=getch()) != '\r')
        {
            code[i] = d;
            i++;
            if(d!='\b')    //输入内容不是退格时就显示 “*”号
            {
            printf("*");
            }
            else     //输入内容是退格时 删除前一个 “*”号
            {
            printf("\b \b");
            }
        }
        p2=head->next;
        while(p2)
        {
            if(p2->loginPassWord==code&&p2->accountNumber==accountcopy)
                {
                    f=true;
                    system("cls");
                    break;
                }
            p2=p2->next;
        }
        if(f)
            break;
        else
            cout<<"\nWrong password"<<endl;
            goto label;
    }
    p=p->next;

}
if(!faccount)
{
    cout<<"The account does not exist"<<endl;
    goto label2;
}
}


string Login(BankDataList head)
{
BankDataList p,pRepeat;
string account;
string code;
bool f=false,faccount=false;

loop: cout<<"Please use your bank card number or mobile phone number to login:\n";
cin>>account;

p=head->next;
while(p)
{
    if(p->accountNumber==account||p->phoneNumber==account)
    {
        faccount=true;
        label: cout<<"Please input your login password:\n";

        int i=0;
        char d,code[20]="\0";
        while((d=getch()) != '\r')
        {
            code[i] = d;
            i++;
            if(d!='\b')    //输入内容不是退格时就显示 “*”号
            {
            printf("*");
            }
            else     //输入内容是退格时 删除前一个 “*”号
            {
            printf("\b \b");
            }
        }

        pRepeat=head->next;
        while(pRepeat)
        {
            if(pRepeat->loginPassWord==code&&(pRepeat->accountNumber==account||pRepeat->phoneNumber==account))
                {
                    f=true;
                    system("cls");
                    break;
                }
            pRepeat=pRepeat->next;
        }
        if(f)
            break;
        else
        {
            cout<<"\nWrong Code\n";
             goto label;
        }
    }
p=p->next;
}
if(!faccount)
{
    cout<<"Account does not exist\n";
    goto loop;
}
return account;
}


void MainMenu(BankDataList headBankData,BillList headBill,array<BankData,1000> *b)
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
    case 1:BankForegroundSubMenu(headBankData,headBill,b);break;
    case 2:AccountProcessSubMenu(headBankData,headBill);break;
    case 3:CustomerSelfHelpSubMenu(headBankData,headBill);break;
    case 4:exit(0);
    default:goto loop;
    }
}

}

void BankForegroundSubMenu(BankDataList headBankData,BillList headBill,array<BankData,1000> *b)
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
    case 1:openAnAccount(headBankData);break;
    case 2:closeAnAccount(headBankData);break;
    case 3:Search(headBankData,b);break;
    case 4:BrowseUserInformation(headBankData);break;
    case 5:ModifyPhoneNumber(headBankData,headBill);break;
    case 6:system("cls");f=true;break;
    case 7:exit(0);
    default:goto loop;
    }
if(f)
    break;

}
}
void openAnAccount(BankDataList head)
{
BankDataList p,rear;
int serialNumber=1;
string accountNumber;
string phoneNumber;
char firstName[10];//string类型使用不了copy()函数，需要使用字符数组
char lastName[15];
string loginPassWord;
string pinCode;
string signBit;
string time;
double balance=0;
ifstream inFromFile;
BankData bankdata;

loop: cout<<"Please input the account of account number,last name,first name,"
    <<"phone number,balance,login password,pin code\n";
cin>>accountNumber>>lastName>>firstName>>phoneNumber>>balance>>loginPassWord>>pinCode;

p=head->next;
while(p)
{
    if(p->accountNumber==accountNumber)
    {
        cout<<"The account already exists\n";
        goto loop;
    }
    p=p->next;
    ++serialNumber;
}
rear=head->next;
while(rear->next)
{
    rear=rear->next;
}
    p=new BankData;
    p->accountNumber=accountNumber;
    p->serialNumber=serialNumber;
    p->lastName=lastName;
    p->firstName=firstName;
    p->phoneNumber=phoneNumber;
    p->balance=balance;
    p->loginPassWord=loginPassWord;
    p->pinCode=pinCode;

    rear->next=p;
    rear=p;
    rear->next=nullptr;

cout<<"Account has been created,it's: \n";
cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
<<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;

cout<<left<<setw(20)<<serialNumber<<setw(20)<<accountNumber<<setw(20)
<<lastName<<setw(20)<<firstName<<setw(20)<<phoneNumber<<setw(20)
<<balance<<setw(20)<<loginPassWord<<right<<setw(15)<<pinCode<<endl;


system("pause");
system("cls");
SaveBankData(head);
}

void closeAnAccount(BankDataList head)
{
BankDataList p,pre;
string account;
bool faccount = false;

loop: cout<<"Please enter the account or mobile number to delete\n";
cin>>account;

pre=head;
p=head->next;
while(p)
{
    if(p->accountNumber==account||p->phoneNumber==account)
    {
     pre->next=p->next;
     free(p);
     faccount=true;
     break;
    }
    p=p->next;
    pre=pre->next;
}
if(!faccount)
{
cout<<"The account does not exist\n";
goto loop;
}

cout<<"Account has been deleted\n";

system("pause");
system("cls");
SaveBankData(head);
}
void Search(BankDataList head,array<BankData,1000> *b)
{
string account;
int number,choice;
bool f=false;
     cout<<"Please enter the account number or mobile phone number or serial number of the user to inquire"<<endl;
loop:cout<<"Please input your choice: \n"
         <<"1.account number or mobile phone--------\n"
         <<"2.serial number-------------------------"<<endl;
cin>>choice;
if(choice==1)
{
    cout<<"Please enter the account number or mobile phone number\n";
    cin>>account;
    cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
    <<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;

    for(BankData bankdata:*b)
    {
        if(bankdata.accountNumber==account||bankdata.phoneNumber==account)
        {
            cout<<left<<setw(20)<<bankdata.serialNumber<<setw(20)<<bankdata.accountNumber<<setw(20)
            <<bankdata.lastName<<setw(20)<<bankdata.firstName<<setw(20)<<bankdata.phoneNumber<<setw(20)
            <<bankdata.balance<<setw(20)<<bankdata.loginPassWord<<right<<setw(15)<<bankdata.pinCode<<endl;
            f=true;
            break;
        }
    }
    if(!f)
        cout<<"this user does not exist\n";
    system("pause");
    system("cls");
}
else if(choice==2)
{
    cout<<"Please enter the serial number\n";
    cin>>number;
    int leftvalue=0,middle=0,rightvalue=999;
    while(leftvalue<rightvalue)
    {
        middle=(leftvalue+rightvalue)/2;
        if(number<middle)
        {
            rightvalue=middle-1;
        }
        else if(number>middle)
        {
            leftvalue=middle+1;
        }
        else
            break;

    }
    cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)//letf,right值与上面变量名不能重复
    <<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;
     cout<<left<<setw(20)<<(*b)[middle].serialNumber<<setw(20)<<(*b)[middle].accountNumber<<setw(20)
        <<(*b)[middle].lastName<<setw(20)<<(*b)[middle].firstName<<setw(20)<<(*b)[middle].phoneNumber<<setw(20)
        <<(*b)[middle].balance<<setw(20)<<(*b)[middle].loginPassWord<<right<<setw(15)<<(*b)[middle].pinCode<<endl;//*b要加个()才行，不然会报错


}
else
{
    cout<<"Wrong choice\n";
    goto loop;
}
}



void BrowseUserInformation(BankDataList head)
{
BankDataList p;
cout<<left<<setw(20)<<"serial number"<<setw(20)<<"account"<<setw(20)<<"lastname"<<setw(20)<<"firstname"<<setw(20)
<<"phone"<<setw(20)<<"balance"<<setw(20)<<"login password"<<right<<setw(15)<<"pin code"<<endl;

p=head->next;
while(p)
{
    cout<<left<<setw(20)<<p->serialNumber<<setw(20)<<p->accountNumber<<setw(20)
    <<p->lastName<<setw(20)<<p->firstName<<setw(20)<<p->phoneNumber<<setw(20)
    <<p->balance<<setw(20)<<p->loginPassWord<<right<<setw(15)<<p->pinCode<<endl;
    p=p->next;
}
system("pause");
system("cls");
}

void ModifyPhoneNumber(BankDataList head,BillList headBill)
{
    BankDataList p;
    BillList pbill;
    string account;
    string phone;
    bool f=false;
    cout<<"Please enter the account number or mobile phone number of the user to be modified\n";
    cin>>account;
p=head->next;
while(p)
{
    if(p->accountNumber==account||p->phoneNumber==account)
    {
        cout<<"Please enter a new phone number\n";
        cin>>phone;

        pbill=headBill->next;
        while(pbill)
        {
            if(pbill->accountNumber==account||pbill->phoneNumber==account)
            {
                pbill->phoneNumber=phone;
            }
            pbill=pbill->next;
        }

        p->phoneNumber=phone;
        cout<<"The modification is completed.\n The modified mobile phone number is: \n";
        cout<<p->phoneNumber<<endl;
        f=true;
        SaveBankData(head);
        break;
    }
    p=p->next;
}

if(!f)
    cout<<"this user does not exist\n";
system("pause");
system("cls");

}

void AccountProcessSubMenu(BankDataList headBankData,BillList headBill)
{
string account;
account=Login(headBankData);
while(true)
{
bool f=false;
cout<<"------Account processing subsystem-------\n\n"
    <<"1.Save Withdraw Money--------------------------------\n"
    <<"2.Return To The Previous Level-------------------\n"
    <<"3.Exit-------------------------------------------\n";
int choice=0;
loop: cout<<"Please input your choices\n";
cin>>choice;
switch(choice)
    {
    case 1:saveWithdrawMonkey(headBankData,headBill,account);break;
    case 2:system("cls");f=true;break;
    case 3:exit(0);
    default:goto loop;
    }
if(f)
    break;

}
}
void saveWithdrawMonkey(BankDataList headBankData,BillList headBill,string account)
{
cout<<"-------------\n";
BankDataList pbank;
BillList pbill,rearbill;
string signBit;
string code;
string timeday,timehour;
double change=0;
bool f=false;

rearbill=headBill->next;
while(rearbill->next)
{

    rearbill=rearbill->next;
}

pbank=headBankData->next;
while(pbank)
{
    if(pbank->accountNumber==account||pbank->phoneNumber==account)
    {

        loop: cout<<"Please input a signBit + or - and your change\n";
        cin>>signBit>>change;
        if(signBit=="+")
        {
            cout<<"Previous balance is: "<<endl;
            cout<<pbank->balance<<endl;

            pbank->balance=pbank->balance+change;
            cout<<"Now balance is: "<<endl;
            cout<<pbank->balance<<endl;

            pbill=new Bill;
            pbill->accountNumber=pbank->accountNumber;
            pbill->signBit=signBit;
            pbill->balanceChanges=change;
            pbill->balance=pbank->balance;
            pbill->phoneNumber=pbank->phoneNumber;

            time_t tt = time(NULL);//这句返回的只是一个时间cuo
            tm* t= localtime(&tt);
            timeday = to_string(t->tm_year + 1900)+"-"+to_string(t->tm_mon + 1)+"-"+to_string(t->tm_mday);
            timehour = to_string(t->tm_hour)+":"+to_string(t->tm_min)+":"+to_string(t->tm_sec);

            pbill->timeday=timeday;
            pbill->timehour=timehour;
            rearbill->next=pbill;
            rearbill=pbill;
            rearbill->next=nullptr;
            cout<<"The balance has increased: "<<change<<endl;
            system("pause");
            system("cls");
            SaveBankData(headBankData);
            SaveBill(headBill);
            f=true;
            break;
        }
        else if(signBit=="-")
        {
        label: cout<<"Please input your pin code:\n";
        cin>>code;
        if(pbank->pinCode==code&&(pbank->accountNumber==account||pbank->phoneNumber==account))
           {
            cout<<"Previous balance is: "<<endl;
            cout<<pbank->balance<<endl;

            pbank->balance=pbank->balance-change;
            cout<<"Now balance is: "<<endl;
            cout<<pbank->balance<<endl;

            pbill=new Bill;
            pbill->accountNumber=pbank->accountNumber;
            pbill->signBit=signBit;
            pbill->balanceChanges=change;
            pbill->balance=pbank->balance;
            pbill->phoneNumber=pbank->phoneNumber;

            time_t tt = time(NULL);//这句返回的只是一个时间cuo
            tm* t= localtime(&tt);
            timeday = to_string(t->tm_year + 1900)+"-"+to_string(t->tm_mon + 1)+"-"+to_string(t->tm_mday);
            timehour = to_string(t->tm_hour)+":"+to_string(t->tm_min)+":"+to_string(t->tm_sec);

            pbill->timeday=timeday;
            pbill->timehour=timehour;
            rearbill->next=pbill;
            rearbill=pbill;
            rearbill->next=nullptr;
            cout<<"The balance has increased: "<<change<<endl;
            system("pause");
            system("cls");
            SaveBankData(headBankData);
            SaveBill(headBill);
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
pbank=pbank->next;
}

}

void CustomerSelfHelpSubMenu(BankDataList headBankData,BillList headBill)
{
string account;
account=Login(headBankData);
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
    case 1:ChangePassword(headBankData,account);break;
    case 2:CheckBalance(headBankData,account);break;
    case 3:BrowseStatements(headBill,account);break;
    case 4:system("cls");f=true;break;
    case 5:exit(0);
    default:goto loop;
    }
if(f)
    break;

}

}
void ChangePassword(BankDataList head,string account)
{
BankDataList p;
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
    p=head->next;
    while(p)
    {
        if(p->accountNumber==account||p->phoneNumber==account)
        {
            p->loginPassWord=passWordSecond;
            SaveBankData(head);
            break;
        }
        p=p->next;
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
    p=head->next;
    while(p)
    {
        if(p->accountNumber==account||p->phoneNumber==account)
        {
            p->loginPassWord=passWordSecond;
            SaveBankData(head);
            break;
        }
        p=p->next;
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
void CheckBalance(BankDataList head,string account)
{
    BankDataList p;
    cout<<"The balance in the account is now: "<<endl;
    p=head->next;
    while(p)
    {
        if(p->accountNumber==account||p->phoneNumber==account)
        {
            cout<<p->balance<<endl;
            system("pause");
            system("cls");
            break;
        }
        p=p->next;
    }

}
void BrowseStatements(BillList head,string account)
{
BillList p;
cout<<left<<setw(20)<<"account"<<setw(20)<<"phone number"<<setw(20)<<"sign bit"<<setw(20)<<"balance change"<<setw(20)<<"balance"<<right<<setw(15)<<"time"<<endl;
p=head->next;
while(p)
{
    if(p->accountNumber==account||p->phoneNumber==account)
    {
        cout<<left<<setw(20)<<p->accountNumber<<setw(20)<<p->phoneNumber<<setw(20)<<p->signBit<<setw(20)<<p->balanceChanges<<setw(20)
        <<p->balance<<right<<setw(15)<<p->timeday<<" "<<p->timehour<<endl;
    }
    p=p->next;
}
system("pause");
system("cls");
}
