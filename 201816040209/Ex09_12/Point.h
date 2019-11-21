#ifndef POINT_H_INCLUDED
#define POINT_H_INCLUDED

class Point
{
public:
    Point(double,double);//constructor function
    //set function
    void setX(double);
    void setY(double);
    //get function
    double getX();
    double getY();

private:
    double x;//Data member
    double y;
};


#endif // POINT_H_INCLUDED
