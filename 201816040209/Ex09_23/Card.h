#ifndef CARD_H_INCLUDED
#define CARD_H_INCLUDED
#include <string>
#include <array>
using namespace std;

static array<string,4> Suit = {"Heart","Spade","Diamond","Club"};//Initialize the Suit array
static array<string,13> Face = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"};//Initialize the Face array

class Card
{
public:
    Card(int=0,int=0);//Initialize function
    Card &toString();
    int getFace();//get function
    int getSuit();
    static array<string,4> Face;
    static array<string,13> Suit;

private:
    int face;//Data member: face of card and suit of card
    int suit;

};


#endif // CARD_H_INCLUDED
