#include <iostream>
#include "Package.h"
#include "TwoDayPackage.h"
#include "OvernightPackage.h"
#include <vector>
using namespace std;

int main()
{
    double sum = 0;
    vector<Package *> packages(3);

    packages[0] = new Package("Jude","Sacramento, California","Tom","St. Paul, Minnesota","35666",1,2);
    packages[1] = new OvernightPackage("Alex","Mississippi Jackson","Tom","Jefferson, Missouri","88888",1,2,3);
    packages[2] = new TwoDayPackage("Ben","Montana Helena","Tom","Columbia, South Carolina","00000",1,2,3);

    for(Package *packagePtr : packages)
    {
        packagePtr->print();
        cout<<packagePtr->calculateCost()<<endl<<endl;
        sum+=packagePtr->calculateCost();
    }

    cout<<"The cost of all courier is: "<<sum<<endl;

return 0;

}
