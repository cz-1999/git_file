#include <iostream>
#include "Rectangle.h"
#include "Point.h"
#include <vector>
using namespace std;

int main()
{
    vector <int> sum;
    double a=0,b=0;

    //Enter and save the coordinates of the four points
    cout<<"Please input four point's coordinate"<<endl<<endl;
    for(int i=0;i<4;++i)
    {
    cout<<"Please input " <<i+1<<" point's coordinate"<<endl;
    cin>>a>>b;
    sum.push_back(a);
    sum.push_back(b);
    }
    //Create and initialize four objects
    Point point1(sum[0],sum[1]);
    Point point2(sum[2],sum[3]);
    Point point3(sum[4],sum[5]);
    Point point4(sum[6],sum[7]);

    Rectangle rectangle(point1,point2,point3,point4);// Create and initialize an object,Determine if it is a rectangle

    //Determine if it is a square
    cout<<(rectangle.getSquare()?"\nIt is also a square":"\nIt is not a square")<<endl;



    return 0;
}
