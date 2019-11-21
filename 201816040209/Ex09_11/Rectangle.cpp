#include<iostream>
#include "Rectangle.h"
using namespace std;

Rectangle::Rectangle(double lh = 1,double w = 1)//Constructor function
{
    setLength(lh);
    setWidth(w);
}

//set function
void Rectangle::setLength(double lh)
{
    if(lh >= 0&&lh <= 20)
        Length = lh;
    else
    {
        Length = 1;
        cout<<"The length must be in 0-20,the length is assigned a value of 1"<<endl;
    }

}
void Rectangle::setWidth(double w)
{
    if( w>=0 && w<=20)
        Width = w;
    else
    {
        Width = 1;
        cout<<"The width must be in 0-20,the width is assigned a value of 1"<<endl<<endl;
    }

}
//get function
double Rectangle::getLength()
{
    return Length;
}

double Rectangle::getWidth()
{
    return Width;
}

double Rectangle::getPerimeter()
{
    return 2 * (Length+Width);
}
double Rectangle::getArea()
{
    return Length*Width;
}
