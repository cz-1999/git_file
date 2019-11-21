#include "time.h"
#include <iostream>
#include <iomanip>
using namespace std;


Time::Time(int h,int m,int s)//Constructor function
{
    time = (h*3600+m*60+s)%86400;
}

//set function
Time &Time::setTimeHour()
{
    hour = time/3600;
    return *this;
}

Time &Time::setTimeMinute()
{
    minute = time%3600/60;
    return *this;
}

Time &Time::setTimeSecond()
{
    second = time%3600/60;
    return *this;
}

//get function
int Time::getTimeHour() const
{
    return time/3600;
}

int Time::getTimeMinute() const
{
    return time%3600/60;
}

int Time::getTimeSecond() const
{
    return time%3600%60;
}

void Time::tick()//Increase by one second
{
    time++;
    time = time%86400;
    setTimeHour().setTimeMinute().setTimeSecond();

}

void Time::displayTime()//display time
{
    cout<<((getTimeHour()==12||getTimeHour()==0)?12:getTimeHour()%12)<<"::"
    <<setfill('0')<<setw(2)<<getTimeMinute()<<"::"<<setw(2)<<getTimeSecond()<<(getTimeHour()<=12 ? " AM" :" PM")<<endl;
}



