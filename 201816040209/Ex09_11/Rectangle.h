#ifndef RECTANGLE_H_INCLUDED
#define RECTANGLE_H_INCLUDED

class Rectangle
{
public:
    Rectangle(double,double);//Constructor function
    //set function
    void setLength(double);
    void setWidth(double);
    //get function
    double getLength();
    double getWidth();

    double getPerimeter();//return Perimeter
    double getArea();//return Area
private:
    double Length;//Data member
    double Width;
};


#endif // RECTANGLE_H_INCLUDED
