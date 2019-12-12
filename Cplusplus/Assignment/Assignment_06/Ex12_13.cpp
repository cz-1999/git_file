#include <iostream>
#include "Package.h"
#include "TwoDayPackage.h"
#include "OvernightPackage.h"
#include <vector>
using namespace std;

int main()
{
    double ounce=0,costperounce=0,additionalfee=0,flatshippingfee=0;
   
    cout<<"The Ounce and CostPerOunce must be bigger than 0"<<endl<<"Otherwise it will be reset to 1"<<endl<<endl;
    cout<<"Please input the value of the Ounce and CostPerOunce"<<endl;
    cin>>ounce>>costperounce;
    Package package("Jude","Sacramento, California","Tom","St. Paul, Minnesota","35666",ounce,costperounce);
    cout<<"The money of package is: "<<package.calculateCost()<<endl<<endl;

    cout<<"The Ounce,CostPerOunce and FlatShippingFee must be bigger than 0"<<endl<<"Otherwise it will be reset to 1"<<endl<<endl;
    cout<<"Please input the value of the Ounce,CostPerOunce and FlatShippingFee"<<endl<<endl;
    cin>>ounce>>costperounce>>flatshippingfee;
    TwoDayPackage twodaypackage("Alex","Mississippi Jackson","Tom","Jefferson, Missouri","88888",ounce,costperounce,flatshippingfee);
    cout<<"The money of twodaypackage is: "<<twodaypackage.calculateCost()<<endl<<endl;


    cout<<"The Ounce,CostPerOunce and AdditionalFee must be bigger than 0"<<endl<<"Otherwise it will be reset to 1"<<endl<<endl;
    cout<<"Please input the value of the Ounce,CostPerOunce and AdditionalFee"<<endl;
    cin>>ounce>>costperounce>>additionalfee;
    OvernightPackage overnightpackage("Ben","Montana Helena","Tom","Columbia, South Carolina","00000",ounce,costperounce,additionalfee);
    cout<<"The money of overnightpackage is: "<<overnightpackage.calculateCost()<<endl;


}
