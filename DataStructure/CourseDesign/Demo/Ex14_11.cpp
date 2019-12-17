/*
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include "ClientData.h"
using namespace std;

int main()
{
    ofstream outCreadit("credit.txt",ios::out|ios::binary);
    if(!outCreadit)
    {
        cerr<<"File could not be opened."<<endl;
        exit(EXIT_FAILURE);
    }
    ClientData blankClient;

    for(int i=0;i<100;++i)
    {
        outCreadit.write(reinterpret_cast< const char *>( &blankClient),sizeof(ClientData));
    }

}


*/
