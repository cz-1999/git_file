#ifndef EMPLOYEE_H_INCLUDED
#define EMPLOYEE_H_INCLUDED
#include <string> //C++ standard string class
using namespace std;

class Employee
{
public:
    Employee(const string &,const string &,const string &);
    virtual ~Employee(){ }//virtual destructor

    void setFirstName(const string &);//set first name
    string getFirstNmae( const);//return first name

    void setLastNmae(const string &);//set last name
    string getLastName()






};


#endif // EMPLOYEE_H_INCLUDED
