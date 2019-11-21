#ifndef DECKOFCARDS_H_INCLUDED
#define DECKOFCARDS_H_INCLUDED
#include "Card.h"
#include <vector>
using namespace std;


class DeckOfCards
{
public:
    DeckOfCards();//Initialize function
    void shuffle();//Shuffle function

    Card &dealCard();//return the next card
    bool moreCards();//Determine if there is a card to deal with

    //display function
    void displayCards();
    void displayFiveCards();

    //Judgment function
    bool onePair();
    bool twoPairs();
    bool threeSameFace();
    bool fourSameFace();
    bool sameSuit();
    bool serialFace();

private:
    vector<Card> deck;//Data member: Card group,currentCard
    int currentCard;

};



#endif // DECKOFCARDS_H_INCLUDED
