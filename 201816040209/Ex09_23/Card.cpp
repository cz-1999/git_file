#include <iostream>
#include "Card.h"
using namespace std;

Card::Card(int f,int s)//Initialize function
{
    face = f;//Initialize face and suit
    suit = s;
}

Card &Card::toString()
{
  return *this;//Return object
}

int Card::getFace()//get function
{
    return face;
}

int Card::getSuit()
{
    return suit;
}
