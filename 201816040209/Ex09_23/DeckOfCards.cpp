#include "Card.h"
#include "DeckOfCards.h"
#include <string>
#include <iostream>
#include <vector>
#include <cstdlib>
#include <iomanip>
using namespace std;

DeckOfCards::DeckOfCards()
{
    for(int i=0;i<52;++i)
    {
        Card card(i%13,i%4);
        deck.push_back(card);
    }
}

void DeckOfCards::shuffle()
{
    for(int i=0;i<52;++i)
    {
        Card card;
        int number = rand()%13;

        card = deck[i];
        deck[i] = deck[number];
        deck[number] = card;
    }

}

void DeckOfCards::displayCards()
{
    cout<<"There are four sets of cards: "<<endl;
    for(int i=0;i<52;++i)
    {
        cout<<Suit[deck[i].toString().getSuit()]+" "+Face[deck[i].toString().getFace()]<<"  ";
        if((i+1)%13==0)
            cout<<endl<<endl;
    }
}

void DeckOfCards::displayFiveCards()//display five cards
{
    cout<<"\nThere are five cards: "<<endl;
    for(int i=0;i<5;++i)
    {
        cout<<Suit[deck[i].toString().getSuit()]+" "+Face[deck[i].toString().getFace()]<<"  ";
    }
    cout<<endl<<endl;
}

bool DeckOfCards::onePair()//Determine if there is a pair
{
    bool a=false;
    Card card;
    int sum=0;
    for(int i=0;i<5;++i)
    {
        sum=0;
        for(int j=0;j<5;++j)
        {
           if(deck[i].getFace()==deck[j].getFace())
           {
                ++sum;
           }
        }
        if(sum>=2)
        a=true;
    }
    if(a)
    cout<<"There is one pair"<<endl;
    else
    cout<<"There is not one pair"<<endl;
    return a;
}

bool DeckOfCards::twoPairs()//Determine if there are two pairs
{
    bool a=false;
    vector<int> cardface;
    Card card;
    int sum=0;
    for(int i=0;i<5;++i)
    {

        for(int j=0;j<5;++j)
        {
           if(deck[i].getFace()==deck[j].getFace())
           {
                ++sum;
           }
        }
        cardface.push_back(sum);
        sum = 0;

    }
    for(int i=0;i<5;++i)
    {
       if(cardface[i]==2)
        {
           ++sum;
           if(sum==4)
           {
               a=true;
               break;
           }
        }

    }

    if(a)
    cout<<"There is two pairs"<<endl;
    else
    cout<<"There is not two pairs"<<endl;
    return a;
}

bool DeckOfCards::threeSameFace()
{
    bool a=false;
    Card card;
    int sum=0;
    for(int i=0;i<5;++i)
    {
        sum=0;
        for(int j=0;j<5;++j)
        {
           if(deck[i].getFace()==deck[j].getFace())
           {
                ++sum;
           }
        }
        if(sum>=3)
        a=true;
    }
    if(a)
    cout<<"There are three same face cards"<<endl;
    else
    cout<<"There are not three same face cards"<<endl;
    return a;
}


bool DeckOfCards::fourSameFace()
{
    bool a=false;
    Card card;
    int sum=0;
    for(int i=0;i<5;++i)
    {
        sum=0;
        for(int j=0;j<5;++j)
        {
           if(deck[i].getFace()==deck[j].getFace())
           {
                ++sum;
           }
        }
        if(sum>=4)
        a=true;
    }
    if(a)
    cout<<"There are four same face cards"<<endl;
    else
    cout<<"There are not four same face cards"<<endl;
    return a;
}

bool DeckOfCards::sameSuit()
{
    bool a=true;
    a = (deck[0].getSuit()==deck[1].getSuit()&&deck[0].getSuit()==deck[2].getSuit()
       &&deck[0].getSuit()==deck[3].getSuit()&&deck[0].getSuit()==deck[4].getSuit())?true:false;
    if(a)
    cout<<"There are five same suit cards"<<endl;
    else
    cout<<"There are not five same suit cards"<<endl;

    return a;
}

bool DeckOfCards::serialFace()
{
    Card card;
    for(int i=0;i<4;++i)
    {
        for(int j=i+1;j<5;++j)
        {
           if(deck[i].getFace()>deck[j].getFace())
           {
               card = deck[i];
               deck[i] = deck[j];
               deck[j] = card;
           }
        }
    }
    bool a=true;
    a = (deck[0].getFace()-deck[1].getFace()==deck[1].getFace()-deck[2].getFace()
       &&deck[0].getFace()-deck[1].getFace()==deck[2].getFace()-deck[3].getFace()
       &&deck[0].getFace()-deck[1].getFace()==deck[3].getFace()-deck[4].getFace())?true:false;
    
    if(a)
        cout<<"There are five serial cards"<<endl;
    else
        cout<<"There are not five serial cards"<<endl;
    return a;
}
