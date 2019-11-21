#include <iostream>
#include <ctime>
#include "time.h"
using namespace std;

int main()
{

Time time2(23,59,55);//Initialization object

for(int i=0;i<10;++i)
{
time2.tick();//Increase by one second
time2.displayTime();//display time

}

return 0;
}
