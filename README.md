# Blackjack-Text-only-
A blackjack text-based game, 1 player vs. CPU, written in Python 3

Straightforward logic: create the deck, then let the player play until it goes over 21 or chooses to Stand. After this the CPU \
plays by itself. 

The game will continue as long as the player chooses to continue. If a deck runs out of cards (decks of 52 cards), the game will \
print a message and "shuffle" a brand new deck, so that the game can continue.

For any other doubts you can read the source code, I wrote comments from beginning to end to make it simpler to understand.

About having 2 different versions for both the deck creation and for the deck creation script, it's because I first wrote the \
game without classes and objects, that is, I used lists and dictionaries. Though quickly I understood how dumb that was so I \
rewrote most of the code with a class for the cards, so the deck turned out as a list holding 52 different objects. The logic
itself remained mostly the same, it was more of a case of using different datatypes.

'createDeck_lists' and 'createDeck_class' are just scripts for creating the deck itself, while 'blackjack' and 'blackjackV2' \
are the full game.

Update logs:

-(feb. 9th 2018): Added a version of the game created using Pygame, a 2D Python game engine. All the assets, in this case only sprites, were created by me.

External references:

Pygame: https://www.pygame.org/docs/
