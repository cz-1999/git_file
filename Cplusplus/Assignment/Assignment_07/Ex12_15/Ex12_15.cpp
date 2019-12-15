#include <iostream>
#include <iomanip>
#include <vector>
#include "Employee.h"
#include "SalariedEmployee.h"
#include "CommissionEmployee.h"
#include "BasePlusCommissionEmployee.h"
#include "HourlyWorker.h"
#include "PieceWorker.h"
using namespace std;

void virtualViaPointer(const Employee * const);
void virtualViaReference(const Employee &);

int main()
{
//Employee employee("Jude","Lily","000000") 抽象基类不能初始化实列，抽象基类应至少包含一个纯虚函数
    cout<<fixed<<setprecision(2);//如果setprecision(n)与setiosflags(ios::fixed)合用，可以控制小数点右边的数字个数

    SalariedEmployee salariedEmployee("John","Smith","111-11-1111",800);
    CommissionEmployee commissionEmployee("Sue","Jones","333-33-3333",10000,.06);
    BasePlusCommissionEmployee basePlusCommissionEmployee("Bob","Lewis","444-44-4444",5000,.04,300);
    HourlyWorker hourlyWorker("Alex","Li","555-55-5555",12,8);
    PieceWorker pieceWorker("Carl","Wang","666-66-6666",.5,200);

    cout<< "Employee processed individually using static binding:\n\n";

    salariedEmployee.print();
    cout<< "\nearned $"<<salariedEmployee.earnings()<<"\n\n";
    commissionEmployee.print();
    cout<< "\nearned $"<<commissionEmployee.earnings()<<"\n\n";
    basePlusCommissionEmployee.print();
    cout<< "\nearned $"<<basePlusCommissionEmployee.earnings()<<"\n\n";
    hourlyWorker.print();
    cout<< "\nearned $"<<hourlyWorker.earnings()<<"\n\n";
    pieceWorker.print();
    cout<< "\nearned $"<<pieceWorker.earnings()<<"\n\n";

    vector< Employee * > employee(5);

    //initialize vector with pointers to Employees
    employee[0] = &salariedEmployee;
    employee[1] = &commissionEmployee;
    employee[2] = &basePlusCommissionEmployee;
    employee[3] = &hourlyWorker;
    employee[4] = &pieceWorker;

    cout<< "Employee processed polymorphically via dynamic binding:\n\n";
    cout<< "Virtual function calls made off base-class pointers:\n\n";

    for(const Employee *employeePtr : employee)
        virtualViaPointer(employeePtr);

    for(const Employee *employeePtr : employee)
        virtualViaReference(*employeePtr);

    return 0;
}

    void virtualViaPointer(const Employee * const baseClassPtr)
    {
        baseClassPtr->print();
        cout<<"\n earned $"<<baseClassPtr->earnings()<<"\n\n";
    }
    void virtualViaReference(const Employee &baseClassRef)
    {
        baseClassRef.print();
        cout<<"\nearned $"<<baseClassRef.earnings()<<"\n\n";
    }

