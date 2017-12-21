#A simple blacjack card game (text-based)

#Imports
from random import shuffle
from random import choice
from sys import exit
from time import sleep

#Function to create a shuffled 52-card deck
def createDeck():
    #Each card is written as: ['rank', 'value', 'suit', 'cardName'], which means each card is a list
    #List to contain the full deck (52 cards)
    deck = []
    #List to hold the name of each Suit
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    #List to hold the names of each card from Ace to 10
    rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    #List to hold the names of Jack, Queen and King cards
    royal = ['Jack', 'Queen', 'King']

    #Loop through each Suit
    for i in suits:
        #Then for each Suit create its 12 cards
        for i2 in range(1, 11):
            #Create a new 'card' (an empty list to be filled with the card's rank, value, suit and name)
            card = []
            #Get the card's rank from the 'rank' list: the first value for a 'card'
            card.append(rank[i2-1])
            #Then append the second value for the 'card': its value
            card.append(i2)
            #Append the suit it belongs too
            card.append(i)
            #Before finishing the card, create its name
            card.append(card[0] + ' of ' + i)
            #After the 'card' is "created", add it to the 'deck'
            deck.append(card)
        #A second nested loop to create only the cards for Jack, Queen and King for each suit
        for i2 in royal:
            #Each of these cards have a value of 10 and belong to suit currently being used in the loop
            card = [10, i]
            #Because the card's rank is the first value, insert the card's rank in the beginning of the list
            card.insert(0,i2)
            #Before finishing the card, create its name
            card.append(card[0] + ' of ' + i)
            #Finally append the card to the 'deck'
            deck.append(card)
        # deck.append([])
    #Shuffle 'deck'
    shuffle(deck)
    return deck

#Function to sum the values of the cards in the player or cpu's hand
def countHand(party_hand):
    party_count = 0
    for i in party_hand:
        #to 'party_count' add the value of each card in 'party_hand'
        party_count += i[1]
    return party_count

#Function to contain the whole gameplay, from creating the deck to the end of each round
def gameplay():
    #Call the createDeck() function to create the deck
    play_deck = createDeck()

    #Total number of rounds played
    rounds_played = 1

    player_continue = True

    while player_continue:
        #Create the initial hand for the player
        #List to contain the player's hand
        player_hand = []
        #Give the player its first two cards
        player_hand.append(play_deck.pop(0))
        player_hand.append(play_deck.pop(0))
        #Then get the count of players's card values
        player_count = countHand(player_hand)
        #List to hold only the names of the cards in 'player_hand'
        show_player_hand = []
        for card in player_hand:
            show_player_hand.append(card[3])
        
        #Create the initial hand for the cpu/computer
        #List to contain the cpu's hand
        cpu_hand = []
        #Give the cpu its first two cards
        cpu_hand.append(play_deck.pop(0))
        cpu_hand.append(play_deck.pop(0))
        #Then get the count of cpu's card values
        cpu_count = countHand(cpu_hand)
        #List to hold only the names of the cards in the cpu's hand to be shown to the player
        show_cpu_hand = []
        for card in cpu_hand:
            show_cpu_hand.append(card[3])
        
        #variables to keep track if the player or the cpu got blackjack
        player_blackjack = False
        cpu_blackjack = False
        #variables to keep track if the player or the cpu got busted (hand count bigger than 21)
        player_busted = False
        cpu_busted = False
        #Variable to keep track if the player has chosen Stand
        player_stand = False
        #Variable to keep track if the round has been decided or not
        round_decided = False

        print('Round', rounds_played)
        print('Your hand is:', show_player_hand)
        print('Your count is:', player_count)
        print()
        # print('CPU hand:', cpu_hand)
        #We only want the player to see the CPU's first card, that is, its hole card
        print('CPU\'s hand is: \'{}\' plus an unknown card'.format(show_cpu_hand[0]))
        # print('CPU count:', cpu_count)
        print()
        print()

    #Test insta-BJ  
        #Test if the player or the cpu have an exceptional Ace and 10-point blackjack hand for instant blackjack
        if player_hand[0][0] == 'Ace' or player_hand[1][0] == 'Ace':
            if player_hand[0][2] == 10 or player_hand[1][2] == 10:
                print('You already got Blackjack!')
                player_blackjack = True
                
        if cpu_hand[0][0] == 'Ace' or cpu_hand[1][0] == 'Ace':
            if cpu_hand[0][2] == 10 or cpu_hand[1][2] == 10:
                cpu_blackjack = True

    #Player_while

        #Keep the round going while the player has not busted and the player hasn't chosen to Stand
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
                print('Your card is:', player_hand[-1][3])
                player_count = countHand(player_hand)
                show_player_hand.append(player_hand[-1][3])

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

    #Player_Quit        
            #If the player has chosen to Quit then print a statement and terminate the program    
            elif player_action == 'q':
                print('You chose to quit the game. Thanks for playing!')
                player_continue = False
                print()
                exit(0)
            
    #CPU phase
        
        #After the player has chosen to Stand, if it's not busted, and while the CPU hasn't busted or the round hasn't been decided let the CPU play
        while (not player_busted) and (not cpu_busted) and (not round_decided):
    
    #CPU Hit
            #If CPU count is below or equal to 16 choose to Hit the CPU, else compare counts to decide the round
            if cpu_count <= 16:
                print('CPU Hits...')
                cpu_hand.append(play_deck.pop(0))
                cpu_count = countHand(cpu_hand)
                show_cpu_hand.append(cpu_hand[-1][3])
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
                    print('Player count is {} and CPU count is {}'.format(player_count, cpu_count))
                    print('CPU won this round.')
                    print()
                    round_decided = True
                
                #If player's count is bigger than the player wins the round
                elif cpu_count < player_count:
                    print('Player count is {} and CPU count is {}'.format(player_count, cpu_count))
                    print('You win this round.')
                    print()
                    round_decided =  True
                
                #If player and CPU count are equal the round ends in a tie
                else:
                    print('Player count is {} and CPU count is {}'.format(player_count, cpu_count))
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