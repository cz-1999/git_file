//Fig. 12.9: Employee.h
// Employee abstract base class.
#ifndef EMPLOYEE_H_INCLUDED
#define EMPLOYEE_H_INCLUDED

#include <string> //C++ standard string class
using namespace std;

class Employee
{
public:
    Employee(const string &,const string &,const string &);
    virtual ~Employee(){};//virtual destructor

    void setFirstName(const string &);//set first name
    string getFirstName() const;//return first name

    void setLastName(const string &);//set last name
    string getLastName() const;//return last name

    void setSocialSecurityNumber(const string &);//set SSN
    string getSocialSecurityNumber() const;//return SSN

    //pure virtual function make Employee an abstract bass class
    virtual double earnings() const = 0 ;//pure virtual
    virtual void print()const;//virtual，如果基类的虚函数只声明而为创建对象，会有错误
private:
    string firstName;
    string lastName;
    string socialSecurityNumber;

};//end class Employee


#endif // EMPLOYEE_H_INCLUDED
