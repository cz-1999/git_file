/*
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <cstdlib>
#include "ClientData.h"
using namespace std;
void outputLine(ostream&,const ClientData &);

int main()
{
    int accountNumber;
    string lastName;
    string firstName;
    double balance;


    fstream inoutCredit("credit.txt",ios::in|ios::out|ios::binary);

    if(!inoutCredit)
    {
        cerr<<"File could not be opened."<<endl;
        exit(EXIT_FAILURE);
    }
    ClientData client;


    //read
    cout<<left<<setw(10)<<"Acount"<<setw(16)<<"Last Name"<<setw(11)
    <<"First Name"<<left<<setw(10)<<right<<"Balance"<<endl;

    inoutCredit.read(reinterpret_cast<char *>(&client),sizeof(ClientData));

    while(inoutCredit&&!inoutCredit.eof())
    {
        //if(client.getAccountNumber()!=0)
            outputLine(cout,client);

        inoutCredit.read(reinterpret_cast<char *>(&client),sizeof(ClientData));


    }



//write
    cout<<"Enter account number (1 to 100,0 to end input)\n?";
    cin>>accountNumber;

    while(accountNumber>0&&accountNumber<=3)
    {
        cout<<"Enter lastname,firstname,balance\n?";
        cin>>lastName;
        cin>>firstName;
        cin>>balance;

        client.setAccountNumber(accountNumber);
        client.setFirstName(firstName);
        client.setLastName(lastName);
        client.setBalance(balance);

        inoutCredit.seekp((client.getAccountNumber()-1)*sizeof(ClientData));
        inoutCredit.write(reinterpret_cast<const char *>(&client),sizeof(ClientData));


        cout<<"Enter account number\n";
        cin>>accountNumber;

    }

    cout<<left<<setw(10)<<"Acount"<<setw(16)<<"Last Name"<<setw(11)
    <<"First Name"<<left<<setw(10)<<right<<"Balance"<<endl;


//read
    inoutCredit.seekg(0);

    inoutCredit.read(reinterpret_cast<char *>(&client),sizeof(ClientData));


    while(inoutCredit&&!inoutCredit.eof())
    {
        //if(client.getAccountNumber()!=0)
            outputLine(cout,client);

        inoutCredit.read(reinterpret_cast<char *>(&client),sizeof(ClientData));

    }



}

void outputLine(ostream &output,const ClientData &record)
{
    output<<left<<setw(10)<<record.getAccountNumber()
    <<setw(16)<<record.getLastName()
    <<setw(11)<<record.getFirstName()
    <<setw(10)<<setprecision(2)<<right<<fixed
    <<showpoint<<record.getBalance()<<endl;
}


*/
