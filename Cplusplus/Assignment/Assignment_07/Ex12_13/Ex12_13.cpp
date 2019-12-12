#include <iostream>
#include "Package.h"
#include "TwoDayPackage.h"
#include "OvernightPackage.h"
#include <vector>
using namespace std;

int main()
{
    double ounce=0,costperounce=0,additionalfee=0,flatshippingfee=0;
    double sum = 0;
    vector<Package *> packages(3);

    packages[0] = new Package(1,2);
    packages[1] = new OvernightPackage(1,2,3);
    packages[2] = new TwoDayPackage(1,2,3);

    for(Package *packagePtr : packages)
    {
        packagePtr->print();
        cout<<packagePtr->calculateCost()<<endl;
        sum+=packagePtr->calculateCost();
    }

    cout<<sum<<endl;

    cout<<"The Ounce and CostPerOunce must be bigger than 0,Otherwise it will be reset to 1"<<endl;
    cout<<"Please input the value of the Ounce and CostPerOunce"<<endl;
    cin>>ounce>>costperounce;
    Package package(ounce,costperounce);
    cout<<"The money of package is: "<<package.calculateCost()<<endl<<endl;

    cout<<"The Ounce,CostPerOunce and FlatShippingFee must be bigger than 0,Otherwise it will be reset to 1"<<endl;
    cout<<"Please input the value of the Ounce,CostPerOunce and FlatShippingFee"<<endl<<endl;
    cin>>ounce>>costperounce>>flatshippingfee;
    TwoDayPackage twodaypackage(ounce,costperounce,flatshippingfee);
    cout<<"The money of twodaypackage is: "<<twodaypackage.calculateCost()<<endl<<endl;


    cout<<"The Ounce,CostPerOunce and AdditionalFee must be bigger than 0,Otherwise it will be reset to 1"<<endl;
    cout<<"Please input the value of the Ounce,CostPerOunce and AdditionalFee"<<endl;
    cin>>ounce>>costperounce>>additionalfee;
    OvernightPackage overnightpackage(ounce,costperounce,additionalfee);
    cout<<"The money of overnightpackage is: "<<overnightpackage.calculateCost()<<endl;


}
