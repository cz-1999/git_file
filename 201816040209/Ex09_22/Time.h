
#ifndef TIME_H
#define TIME_H

class Time
{
public:
    Time(int,int,int);//Constructor function

    //set function
    Time &setTimeHour();
    Time &setTimeMinute();
    Time &setTimeSecond();

    //get function
    int getTimeHour() const;
    int getTimeMinute() const;
    int getTimeSecond() const;

    void tick();//Increase by one second

    void displayTime();//display time

private:
    int time;//Data member
    int hour;
    int minute;
    int second;
};

#endif // TIME_H_INCLUDED
