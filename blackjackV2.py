#A simple blacjack card game (text-based)

#Imports
from random import shuffle
from random import choice
from sys import exit
from time import sleep

#Class to create each of card of a deck. 
#Each card will use a 'rank', 'value' and 'name' properties throughout the program
class Card():
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.name = rank + ' of ' + suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

#Function to create a shuffled 52-card deck
def createDeck():
    deck = []
    #Card = [rank, value, suit, name]
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    royal = ['Jack', 'Queen', 'King']
    #Create the deck by using list comprehension for the numbered cards and the "royal" cards
    deck = [Card(rank[i2-1],i2,i) for i in suits for i2 in range(1,11)]
    royal_cards = [Card(i2,10,i) for i in suits for i2 in royal]
    deck += royal_cards
    shuffle(deck)
    return deck

#Function to contain the whole gameplay, from creating the deck to the end of each round
def gameplay():
    #Call the createDeck() function to create the deck
    play_deck = createDeck()
    #Total number of rounds played
    rounds_played = 1
    #Only False if the player chooses to Quit the game
    player_continue = True

    while player_continue:
    #Create the initial hand for the player
        #Each round, the player begins with the top two cards from the deck
        player_hand = [play_deck.pop(0), play_deck.pop(0)]
        #Get the total count from the player hand
        player_count = sum(card.get_value() for card in player_hand)
        #List to hold only the names of the player's cards
        show_player_hand = [card.get_name() for card in player_hand]
        
    #Create the initial hand for the CPU
        #Each round, the CPU begins with the top two cards from the deck, after the play has its hand
        cpu_hand = [play_deck.pop(0), play_deck.pop(0)]
        #Get the total count from the CPU hand
        cpu_count = sum(card.get_value() for card in cpu_hand)
        #List to hold only the names of CPU's cards
        show_cpu_hand = [card.get_name() for card in cpu_hand]
        
        #Variables to keep track if the player or CPU have Blackjack
        player_blackjack = False
        cpu_blackjack = False
        #Variables to keep track if the player or the CPU got busted (hand count bigger than 21)
        player_busted = False
        cpu_busted = False
        #Variable to keep track if the player has chosen to Stand
        player_stand = False
        #Variable to keep track if the round has been decided or not
        round_decided = False

        print('Round', rounds_played)
        print('Your hand is:', show_player_hand)
        print('Your count is:', player_count)
        print()
        #We only want the player to see the CPU's first card, that is, its hole card
        print('CPU\'s hand is: \'{}\' plus an unknown card'.format(show_cpu_hand[0]))
        print()
        print()

    #Test insta-BJ  
        #Test if the player or the cpu have an exceptional Ace and 10-point blackjack hand for instant blackjack
        if player_hand[0].get_rank() == 'Ace' or player_hand[1].get_rank() == 'Ace':
            if player_hand[0].get_value() == 10 or player_hand[1].get_value() == 10:
                print('You already got Blackjack!')
                player_blackjack = True
                player_count = 21
                
        if cpu_hand[0].get_rank() == 'Ace' or cpu_hand[1].get_rank() == 'Ace':
            if cpu_hand[0].get_value() == 10 or cpu_hand[1].get_value() == 10:
                cpu_blackjack = True
                cpu_count = 21

    #Player_while

        #Keep the round going while the player has not busted, the player hasn't chosen to Stand \
        #the player doesn't have blackjack and the player chooses to continue
        while (not player_busted) and (not player_stand) and (not player_blackjack) and player_continue:
            #Prompt the player for an action:
            #Hit: ask for another card, the top card from 'play_deck'
            #Stand: the player won't ask for more cards this round, and it's the CPU turn for action
            #Quit: end the game
            player_action = input('What are you gonna do: (H)it, (S)tand or (Q)uit?').lower()
        
    #Player_Hit
            #If the player has chosen Hit then draw the top card from the deck
            if player_action == 'h':
                sleep(1)
                #Draw a card for the player and print it
                player_hand.append(play_deck.pop(0))
                print('Your card is:', player_hand[-1].get_name())
                player_count += player_hand[-1].get_value()
                show_player_hand.append(player_hand[-1].get_name())

                #If the deck is out of cards, create a new one
                if len(play_deck) == 0:
                    print('This deck has been completely used. Time to shuffle a new one.')
                    print()
                    play_deck = createDeck()
                    sleep(3)
                            
                #Test if the player has busted: if true change the 'player_busted' variable to True and print a statment
                if player_count > 21:
                    player_busted = True
                    print('Your count is:', player_count)
                    print('You busted. This means you lose this round.')
                    print()
                
                #If player count is 21 then the player got BlackJack
                elif player_count == 21:
                    print('You got BlackJack!')
                    print('Now let\'s see the CPU\'s hand...')
                    print()
                    player_blackjack = True
                    
                #Else print the player hand and the player count
                else:
                    print('Your hand is:', show_player_hand)
                    print('Your count is:', player_count)
                    print()
    #Player_Stand
            #If the player has chosen to Stand then...
            elif player_action == 's':
                print('You chose to Stand.')
                player_stand = True
                print()
                print()
                sleep(1)

    #Player_Quit        
            #If the player has chosen to Quit then print a statement and terminate the program    
            elif player_action == 'q':
                print('You chose to quit the game. Thanks for playing!')
                player_continue = False
                print()
                exit(0)
            
    #CPU phase
        #After the player has chosen to Stand, if it's not busted, \
        #and while the CPU hasn't busted or the round hasn't been decided let the CPU play
        while (not player_busted) and (not cpu_busted) and (not round_decided):
    #CPU Hit
            #If CPU count is below or equal to 16 choose to Hit the CPU, else compare counts to decide the round
            if cpu_count <= 16:
                print('CPU Hits...')
                cpu_hand.append(play_deck.pop(0))
                cpu_count += cpu_hand[-1].get_value()
                show_cpu_hand.append(cpu_hand[-1].get_name())
                sleep(1)
                
                #If the deck is out of cards, create a new one
                if len(play_deck) == 0:
                    print('This deck has been completely used. Time to shuffle a new one.')
                    print()
                    play_deck = createDeck()
                    sleep(3)

                #If cpu count is bigger than 21 than the CPU busted
                if cpu_count > 21:
                    cpu_busted = True
                    print('CPU\'s hand is:', show_cpu_hand)
                    print('CPU\'s count is:', cpu_count)
                    print('The CPU busted. This means you win this round.')
                    round_decided = True
                    print()
                
                #If the CPU count is 21 then the CPU got Blackjack
                elif cpu_count == 21:
                    round_decided = True
                    print('The CPU got a Blackjack!')

                    #If the player also got Blackjack then it's a tie
                    if player_blackjack == True:
                        print('Both you and the CPU got Blackjack! Then this is round ends in a tie.')
                        print()

                    #Else the CPU wins the round
                    else:
                        print('Because your count is lower the CPU wins this round.')
                        print()
                    
                    #If the deck is out of cards, create a new one
                    if len(play_deck) == 0:
                        print('This deck has been completely used. Time to shuffle a new one.')
                        print()
                        play_deck = createDeck()
                else:
                    cpu_stand = True
                    print('CPU\'s hand is:', show_cpu_hand)
                    print('CPU\'s count is:', cpu_count)
                    print()
        
        #CPU final hand: final count

            #CPU count is bigger than 16
            else:
                print('CPU\'s final hand is:', show_cpu_hand)
                print('CPU\'s count is:', cpu_count)
                print()
                sleep(2)
            
            #When the CPU is done getting new cards, compare player and cpu counts
                #If CPU's count is bigger then CPU wins the round
                if cpu_count > player_count:
                    print(f'Player count is {player_count} and CPU count is {cpu_count}')
                    print('CPU won this round.')
                    print()
                    round_decided = True
                
                #If player's count is bigger than the player wins the round
                elif cpu_count < player_count:
                    print(f'Player count is {player_count} and CPU count is {cpu_count}')
                    print('You win this round.')
                    print()
                    round_decided =  True
                
                #If player and CPU count are equal the round ends in a tie
                else:
                    print(f'Player count is {player_count} and CPU count is {cpu_count}')
                    print('This round ends in a tie.')
                    print()
                    round_decided = True
        
        #After finishing the round, prompt the player to keep playing or quit the game
        prompt_continue = input('Do you wish to keep playing? (Y)es or (N)o')
        if prompt_continue.lower() == 'y':
            print('You chose to keep playing.')
            print()
            rounds_played += 1
            sleep(1)
            print('----------------------------------------------------------')
        else:
            print('After playing', rounds_played, 'rounds, you chose to quit the game.')
            print()
            player_continue = False


#Begin the game
print('Let\'s start the game!')
print('~Draws two cards for you and two cards for the Computer~')
print()
sleep(2)

#Call the main function to play the game
gameplay()
#After the player chooses to Quit aka before ending the program
print('Thanks for playing!')