#include <iostream>
#include "Rectangle.h"
using namespace std;

int main()
{
    Rectangle rectangle(4,5);//Create and initialize an object
    cout<<"The perimeter is "<<rectangle.getPerimeter()<<"\n"<<"The area is "<<rectangle.getArea()<<endl;//return perimeter and area
}
