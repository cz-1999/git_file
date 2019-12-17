
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include "ClientData.h"
using namespace std;
void outputLine(ostream&,const ClientData &);

int main()
{
    ifstream inCredit("credit.txt",ios::in|ios::binary);
    ifstream inCredit2("credit.txt",ios::in|ios::binary);
    if(!inCredit)
    {
        cerr<<"File could not be opened."<<endl;
        exit(EXIT_FAILURE);
    }

    cout<<left<<setw(10)<<"Acount"<<setw(16)<<"Last Name"<<setw(11)
    <<"First Name"<<left<<setw(10)<<right<<"Balance"<<endl;

    ClientData client;

    inCredit.seekg(0*sizeof(ClientData));

    inCredit.read(reinterpret_cast<char *>(&client),sizeof(ClientData));

    while(inCredit&&!inCredit.eof())
    {
        //if(client.getAccountNumber()!=0)
            outputLine(cout,client);

        inCredit.read(reinterpret_cast<char *>(&client),sizeof(ClientData));

    }

    cout<<"--------------------------------------------------------------"<<endl;

    inCredit2.seekg(0*sizeof(ClientData));

    inCredit2.read(reinterpret_cast<char *>(&client),sizeof(ClientData));

    while(inCredit2&&!inCredit2.eof())
    {
        if(client.getAccountNumber()!=0)
            outputLine(cout,client);

        inCredit2.read(reinterpret_cast<char *>(&client),sizeof(ClientData));

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

