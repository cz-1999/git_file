#ifndef RECTANGLE_H_INCLUDED
#define RECTANGLE_H_INCLUDED
#include "Point.h"

class Rectangle
{
public:
    Rectangle(Point&, Point&, Point&, Point&);//constructor function
    //set function
    void setRectangle( Point&, Point&, Point&, Point&);
    //get function
    double getLength();
    double getWidth();
    double getPerimeter();
    double getArea();
    bool getSquare();
private:
    double length=0;//Data member
    double width=1;
};

#endif // RECTANGLE_H_INCLUDED
