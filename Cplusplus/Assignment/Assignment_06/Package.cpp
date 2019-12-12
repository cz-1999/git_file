#include <iostream>
#include "Package.h"
using namespace std;

Package::Package(const string &namesend,const string &addresssend,const string &namereceive,
                 const string &addressreceive,const string &postalcode,double ounce,double costperounce)
:nameSend(namesend),addressSend(addresssend),nameReceive(namereceive),addressReceive(addressreceive),PostalCode(postalcode)
{
    Ounce = ounce>0?ounce:1;
    CostPerOunce = costperounce>=0?costperounce:1;
}

Package::~Package()
{

}

double Package::getCostPerOunce()
{
return CostPerOunce;
}

double Package::getOunce()
{
return Ounce;
}

void Package::print()
{
cout<<"The Sender is: "<<nameSend<<endl<<"The Sender's address is: "<<addressSend<<endl<<endl;
cout<<"The Recipient is: "<<nameReceive<<endl<<"The Recipient's address is: "<<addressReceive<<endl<<endl;
cout<<"The cost of courier is: "<<endl;
}

double Package::calculateCost()
{
    return  Ounce*CostPerOunce;
}
