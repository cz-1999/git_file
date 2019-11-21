#include <iostream>
#include "Rectangle.h"
#include "Point.h"
#include <cmath>

using namespace std;

Rectangle::Rectangle(Point& point1, Point& point2, Point& point3,Point& point4)//constructor function
{
    setRectangle(point1,point2,point3,point4);
}

//set function
void Rectangle::setRectangle(Point& point1, Point& point2,Point& point3, Point& point4)
{
    //Determine whether the distance from the center of the rectangle to the four points is equal
    if(point1.getX()>=0&&point1.getX()<=20&&point1.getY()>=0&&point1.getY()<=20
     &&point2.getX()>=0&&point2.getX()<=20&&point2.getY()>=0&&point2.getY()<=20
     &&point3.getX()>=0&&point3.getX()<=20&&point3.getY()>=0&&point3.getY()<=20
     &&point4.getX()>=0&&point4.getX()<=20&&point4.getY()>=0&&point4.getY()<=20)
        {
        double x=0,y=0,d1=0,d2=0,d3=0,d4=0,d5=0,d6=0,d7=0;
        x = (point1.getX()+point2.getX()+point3.getX()+point4.getX())/4;
        y = (point1.getY()+point2.getY()+point3.getY()+point4.getY())/4;
        d1 = sqrt(pow(point1.getX()-x,2)+pow(point1.getY()-y,2));
        d2 = sqrt(pow(point2.getX()-x,2)+pow(point2.getY()-y,2));
        d3 = sqrt(pow(point3.getX()-x,2)+pow(point3.getY()-y,2));
        d4 = sqrt(pow(point4.getX()-x,2)+pow(point4.getY()-y,2));

        //Eliminate the effects of loss of precision
        cout<<"\nThe distance from the center of the rectangle to 4 points is: \n"<<d1<<" "<<d2<<" "<<d3<<" "<<d4<<endl<<endl;
        if(d1==d2&&d1==d3&&d1==d4)
        {
           //Select the first point, calculate its distance to the other three points,
           //remove the longest distance and judge the length and width.
           cout<<"Yes,It is a rectangle";
           double maxsize=0;
           d5 = sqrt(pow(point1.getX()-point2.getX(),2)+pow(point1.getY()-point2.getY(),2));
           d6 = sqrt(pow(point1.getX()-point3.getX(),2)+pow(point1.getY()-point3.getY(),2));
           d7 = sqrt(pow(point1.getX()-point4.getX(),2)+pow(point1.getY()-point4.getY(),2));
           maxsize = d5>=maxsize?d5:maxsize;
           maxsize = d6>=maxsize?d6:maxsize;
           maxsize = d7>=maxsize?d7:maxsize;
           if(maxsize == d5)
           {
               length = d6>=d7?d6:d7;
               width = d6>=d7?d7:d6;
           }
           else if(maxsize == d6)
           {
               length = d5>=d7?d5:d7;
               width = d5>=d7?d7:d5;
           }
           else if(maxsize == d7)
           {
               length = d6>=d5?d6:d5;
               width = d6>=d5?d5:d6;
           }
        }
        else
        {
            cout<<"No,It is not a rectangle";
        }

        }
    else
        {
        cout<<"The coordinate must be in 0-20";
        }

}

//get function
double Rectangle::getLength()
{
    return length;
}
double Rectangle::getWidth()
{
    return width;
}
double Rectangle::getPerimeter()
{
    return width*length;
}
double Rectangle::getArea()
{
    return 2*(width+length);
}
bool Rectangle::getSquare()
{
    return length == width ? true :false;
}
