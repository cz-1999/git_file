#include <iostream>
#include "Card.h"
#include "DeckOfCards.h"
#include <string>
using namespace std;

int main()
{
    DeckOfCards deckofcard;//Create and initialize decks
    deckofcard.shuffle();//Shuffle
    deckofcard.displayCards();//Deal all of cards

    deckofcard.shuffle();//Shuffle
    deckofcard.displayFiveCards();//Deal five cards

    deckofcard.onePair();//Determine if there is a pair
    deckofcard.twoPairs();//Determine if there are two pairs
    deckofcard.threeSameFace();//Determine if there are 3 cards with the same face value
    deckofcard.fourSameFace();//Determine if there are 4 cards with the same face value
    deckofcard.sameSuit();//Determine if the card's suit are the same
    deckofcard.serialFace();//Determine if the card's face are serial
}
