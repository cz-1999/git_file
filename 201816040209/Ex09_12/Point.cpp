#include "Point.h"

Point::Point(double x,double y)//constructor function
{
    setX(x);
    setY(y);
}
//set function
void Point::setX(double x)
{
    Point::x = x;
}

void Point::setY(double y)
{
    Point::y = y;
}
//get function
double Point::getX()
{
    return x;
}

double Point::getY()
{
    return y;
}
