#The engine used for this game is Pygame: https://www.pygame.org/docs/
#All the assets used in this game were created by me, Ze1598.

import pygame
from random import shuffle, choice

#Class to create a card (then 1 deck contains 52 Card objects)
class Card():
    '''Creates games cards.
    
    Attributes:
        rank (str): Rank of the card in the Ace-10 scale.
        value (int): Numerical value of the card in Black Jack.
        name (str): Full name of the card.
    '''
    def __init__(self, rank, value, suit):
        '''The initial method to be called upon instantiation of the Card class.
        
        Args:
            rank (str): Rank of the card in the Ace-10 scale.
            value (int): Numerical value of the card in Black Jack.
            name (str): Full name of the card.
        '''
        self.rank = rank
        self.value = value
        #The card's name is written in the Rank_of_Suit format to simplify the search for the corresponding sprite
        self.name = rank + '_of_' + suit

def create_deck():
    '''Creates a 52-card deck: a list that holds 52 Card objects.
    
    Args:
        None

    Returns: 
        deck (list): a list containing 52 Card objects.
    '''
    deck = []
    #Card = [rank, value, suit, name]
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    figures = ['Jack', 'Queen', 'King']
    #Create the 52 cards: first the numerical ones, then the figure cards
    deck = [Card(rank[i2-1],i2,i) for i in suits for i2 in range(1,11)] + [Card(i2,10,i) for i in suits for i2 in figures]
    return deck

#Call the 'create_deck' function to create a 52-card deck
deck = create_deck()
shuffle(deck)
#Only a maximum of 8 decks can be used
deck_count = 0

class Rectangle():
    '''Creates rectangle figures to be drawn on the screen.

    Attributes:
        card_object (__main__.Card): A game card; an object from the Card class.
        x_coord (int): Initial x coordinate for the object.
        y_coord (int): Initial y coordinate for the object.
        width (int): The object's width.
        height (int): The object's height.
        color (tuple): The object's color
    '''

    def __init__(self, card_obj, x_coord, y_coord, width, height, color):
        '''The initial method to be called upon instantiation of the Rectangle class.
        
        Args:
            card_obj (__main__.Card): A game card; an object from the Card class.
            x_coord (int): Initial x coordinate for the object.
            y_coord (int): Initial y coordinate for the object.
            width (int): The object's width.
            height (int): The object's height.
            color (tuple): The object's color.
        '''
        self.card_obj = card_obj
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.color = color
    
    def get_dimensions(self):
        '''Returns a list with the initial values for a rectangle's coordinates and dimensions.
        
        Args:
            None
        
        Returns:
            list: A list containing the initial coordinates and dimensions of the rectangle.
        '''
        return [self.x_coord, self.y_coord, self.width, self.height]
    
    def top_right(self):
        '''Returns the coordinates for the top-right vertice of the rectangle.
        
        Args:
            None
        
        Returns:
            tuple: A tuple containing the x and y values of the rectangle's top-right vertice.
        '''
        return (self.x_coord + self.width, self.y_coord)
    
    def bottom_left(self):
        '''Returns the coordinates for the bottom-left vertice of the rectangle.
        
        Args:
            None
        
        Returns:
            tuple: A tuple containing the x and y values of the rectangle's bottom-left vertice.
        '''
        return (self.x_coord, self.y_coord + self.height)

    def bottom_right(self):
        '''Returns the coordinates for the bottom-right vertice of the rectangle.
        
        Args:
            None
        
        Returns:
            tuple: A tuple containing the x and y values of the rectangle's bottom-right vertice.
        '''
        return (self.x_coord + self.width, self.y_coord + self.height)

class Participant():
    '''Creates game participants, more precisely, the player and the CPU.

    Attributes:
        name (str): The participant's name.
        hand (list): The cards the participant currently has; a list containing __main__.Card objects.
        part_turn (bool): True if it's the participant's turn, else False. Defaults to True.
        now_score (int): The current player's hand score.
        display_score (str): The version of the player's score to be displayed in the screen.
    '''
    def __init__(self, name, hand):
        '''The initial method to be called upon instantiation of the Rectangle class.
        
        Args:
            name (str): The participant's name.
            hand (list): The cards the participant currently has.
        '''
        self.name = name
        self.hand = hand
        self.part_turn = True

    def draw_card(self, card):
        '''Method to draw a card for the participant

        Args:
            card (obj): a Rectangle object
        '''
        self.hand.append(card)

    def updt_score(self):
        '''Calculates the score of the current participant's hand and the score to be displayed on the screen.

        Args:
            None
        '''
        self.now_score = sum(self.hand[i].card_obj.value for i in range(len(self.hand)))
        self.display_score = 'You blew up.' if (self.now_score > 21 and self.name == 'Player') else 'The CPU blew up.' if (self.now_score > 21 and self.name == 'CPU') else str(self.now_score)

    def change_turn(self):
        '''Method to be called to denote when a participant's turn has finished or started
        Args:
            None
        '''
        self.part_turn = not self.part_turn

def insta_blackjack(part):
    '''Returns a Boolean value about whether the player has an Ace and a Figure cards: a score of 11 
    where the first card's value is 1 or 10 (we only want the 1+10 and 10+1 cases to return True), which
    is a Blackjack. If it does have this pair, modify the value of the Ace card to 11 so the score sums
    add up in the end, update the participants's scores and return True; If it does not have a pair 
    like this, just return False.

    Args:
        part (__main__.Participant): A Participant object

    Returns:
        bool: True if the person's score is 11 and the first card's value is 1 or 10; else False
    '''
    #If the 2 cards on the participant's hand add up to 11 and the first card's value is either 1 or 10
    #Then adjust the Ace card's value in the participant's hand to 11 to facilitate future score comparisons
    if (part.hand[0].card_obj.value + part.hand[1].card_obj.value == 11) and (part.hand[0].card_obj.value == 1 or part.hand[0].card_obj.value == 10):
        if part.hand[0].card_obj.value == 1:
            part.hand[0].card_obj.value = 11
            part.now_score = 21
            part.display_score = 'BLACKJACK'
            return True
        elif part.hand[1].card_obj.value == 1:
            part.hand[1].card_obj.value = 11
            part.now_score = 21
            part.display_score = 'BLACKJACK'
            return True
    else:
        return False

def new_deck():
    deck = create_deck()
    shuffle(deck)
    return deck

#Start the engine
pygame.init()

#Color definition
BLACK = (0, 0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255,0)
GREEN_DARKER = (10, 132, 67)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (221, 224, 33)

#Window size
size = (700, 500)
#Window title
pygame.display.set_caption("Blackjack")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Font format to be used
font = pygame.font.SysFont('Consolas', 14, False, False)

#Player initialization
#A temporary list to hold a hand of cards which will be passed to one of the participants
first_hand = []
first_hand.append(Rectangle(deck.pop(), size[0]+3, size[1]-150, 37, 65, WHITE))
first_hand.append(Rectangle(deck.pop(), size[0]+409, size[1]-150, 37, 65, WHITE))
#Initialize a Participant object for the Player
player = Participant('Player', first_hand)
#self.part_turn is True while it's that participant's Turn, else False
player.part_turn = True
#Variable to make sure the cards are separated with equivalent spacing
#It is the average between the width of the screen and the resulting value of alocating each card to a vertical section of\
#the screen, given that the screen has screen_width/cards_in_player_hand sections
p_whitespace = (size[0] - ((size[0]//len(player.hand))*(len(player.hand)-1) + size[0]//player.hand[-1].width + player.hand[-1].width))//2
#For each card in the player's hand, create data attributes, 'x_stop' for the x value where it needs to stop and 'x_move', which\
#is how many horizontal units the card moves per frame when it moves
for i in range(len(player.hand)):
    player.hand[i].x_stop = (size[0]//len(player.hand))*(i) + p_whitespace
    player.hand[i].x_move = 7
    player.hand[i].sprite = pygame.image.load("assets\\" + player.hand[i].card_obj.name + ".png").convert()
#Update the score of the hands in the Player's hand
player.updt_score()
#Because this is the beginning, test if the Player got Blackjack (Ace+Figure). If it did 'display_score' is now 'BLACKJACK'\
#else remains the same
insta_blackjack(player)
#New data attribute to hold the number of rounds won by the Player
player.rounds_won = 0

#CPU initialization
#A temporary list to hold a hand of cards which will be passed to one of the participants
first_hand = []
first_hand.append(Rectangle(deck.pop(), size[0]+3, 100, 37, 65, WHITE))
first_hand.append(Rectangle(deck.pop(), size[0]+409, 100, 37, 65, WHITE))
#Initialize a Participant object for the CPU
cpu = Participant('CPU', first_hand)
#self.part_turn is True while it's that participant's Turn, else False
cpu.part_turn = False
#Variable to make sure the cards are separated with equivalent spacing
#It is the average between the width of the screen and the resulting value of alocating each card to a vertical section of\
#the screen, given that the screen has screen_width/cards_in_cpu_hand sections
c_whitespace = (size[0] - ((size[0]//len(cpu.hand))*(len(cpu.hand)-1) + size[0]//cpu.hand[-1].width + cpu.hand[-1].width))//2
#For each card in the CPU's hand, create data attributes, 'x_stop' for the x value where it needs to stop and 'x_move', which\
#is how many horizontal units the card moves per frame when it moves
for i in range(len(cpu.hand)):
    cpu.hand[i].x_stop = size[0]//len(cpu.hand)*(i) + c_whitespace
    cpu.hand[i].x_move = 7
#The first card has a normal sprite, but the second one is the Hole Card, so it has a special sprite until the CPU's turn
cpu.hand[0].sprite = pygame.image.load("assets\\" + cpu.hand[0].card_obj.name + ".png").convert()
cpu.hand[1].sprite = pygame.image.load("assets\\Hole_Card.png").convert()
#At first, the CPU's score is only the value of the card turned up, the Hole Card's value is not counted
cpu.updt_score()
cpu.now_score -= cpu.hand[1].card_obj.value
cpu.display_score = str(cpu.now_score)
#New data attribute to hold the number of rounds won by the CPU
cpu.rounds_won = 0

#Create the boxes for the player to click (Hit, Stand, Continue and Quit)
#HIT
hit_box = Rectangle(None, size[0]//2-75, size[1]-37, 65, 37, BLACK)
hit_box.sprite = pygame.image.load("assets\\hit_box.png").convert()
#STAND
stand_box = Rectangle(None, size[0]//2+17, size[1]-37, 65, 37, BLACK)
stand_box.sprite = pygame.image.load("assets\\stand_box.png").convert()
#CONTINUE
continue_box = Rectangle(None, size[0]//2-75, size[1]//2, 65, 37, BLACK)
continue_box.sprite = pygame.image.load("assets\\continue_box.png").convert()
#QUIT
quit_box = Rectangle(None, size[0]//2+17, size[1]//2, 65, 37, BLACK)
quit_box.sprite = pygame.image.load("assets\\quit_box.png").convert()

#Winner of each round
round_result = None

#Main Loop
while not done:
    #Mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    #Check for user events
    for event in pygame.event.get():
        
        #If the player clicked Close: close the game window and exit the engine
        if event.type == pygame.QUIT:
            #Flag that the main loop needs to be terminated
            done = True
        
        #If the player clicked with the mouse
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            #Player clicked the HIT box during its turn and it doesn't have a Blackjack
            #Then draw a card and update its score
            if (hit_box.x_coord <= mouse_pos[0] <= hit_box.top_right()[0]) and (hit_box.y_coord <= mouse_pos[1] <= hit_box.bottom_right()[1]) and player.part_turn and (player.display_score != 'BLACKJACK' and player.display_score != 'You blew up.') and (not cpu.part_turn):
                #Draw a card for the player
                #Each card the Player draws is initially drawn 200 horizontal units away from the previous one
                player.hand.append(Rectangle(deck.pop(), size[0]+200, size[1]-150, 37, 65, WHITE))
                #Load the sprite for the drawn card
                player.hand[-1].sprite = pygame.image.load("assets\\" + player.hand[-1].card_obj.name + ".png").convert()
                #If the current deck ran out of cards then create a new one and increment the used decks counter
                if len(deck) == 0:
                    deck = new_deck()
                    deck_count += 1
                    if deck_count == 8:
                        done = True
                #Readjust the spacing between cards and move the already existing ones on the screen
                p_whitespace = (size[0] - ((size[0]//len(player.hand))*(len(player.hand)-1) + size[0]//player.hand[-1].width + player.hand[-1].width))//2
                #Adjust the coordinates for each card the player is holding
                for i in range(len(player.hand)):
                    player.hand[i].x_stop = (size[0]//len(player.hand))*(i) + p_whitespace
                    player.hand[i].x_move = 5
                #Update the Player's score
                player.updt_score()
                #If the player went over 21 then it blew up
                # if player.now_score > 21:
                #     player.updt_score()
                #If Player's score is 21, then it got a Blackjack
                if player.now_score == 21: player.display_score = 'BLACKJACK'

            #Player clicked the STAND box to finish its turn
            #Then finish the Player's turn and start CPU's
            elif (stand_box.x_coord <= mouse_pos[0] <= stand_box.top_right()[0]) and (stand_box.y_coord <= mouse_pos[1] <= stand_box.bottom_right()[1]) and player.part_turn and (not cpu.part_turn):
                #Finish the player's turn
                player.change_turn()
                #Start CPU's turn
                cpu.change_turn()
                #Reveal the hole card
                cpu.hand[1].sprite = pygame.image.load("assets\\" + cpu.hand[1].card_obj.name + ".png").convert()
                #Update CPU's score with the hole card value
                cpu.updt_score()
                #Now that both cards of the CPU are shown, it may have an instant Blackjack
                insta_blackjack(cpu)
                #If it did have a Blackjack then finish the CPU's turn
                if cpu.now_score == 21: cpu.change_turn()
            
            #Player clicked the CONTINUE box
            #Reset the Player's hand and score, and the CPU's hand and score
            elif (continue_box.x_coord <= mouse_pos[0] <= continue_box.top_right()[0]) and (continue_box.y_coord <= mouse_pos[1] <= continue_box.bottom_right()[1]) and player.part_turn and cpu.part_turn:
                #Reset Player aspects
                player.hand = []
                #Draw a card and check if there's cards left in the deck
                player.hand.append(Rectangle(deck.pop(), size[0]+3, size[1]-150, 37, 65, WHITE))
                if len(deck) == 0:
                    deck = new_deck()
                    deck_count += 1
                    if deck_count == 8:
                        done = True
                #Draw a second card and check if there's cards left in the deck
                player.hand.append(Rectangle(deck.pop(), size[0]+409, size[1]-150, 37, 65, WHITE))
                if len(deck) == 0:
                    deck = new_deck()
                    deck_count += 1
                    if deck_count == 8:
                        done = True
                #It will be the Player's turn
                player.part_turn = True
                #Spacing for the cards in the screen
                p_whitespace = (size[0] - ((size[0]//len(player.hand))*(len(player.hand)-1) + size[0]//player.hand[-1].width + player.hand[-1].width))//2
                #Adjust where to put the cards in the screen and load its sprites
                for i in range(len(player.hand)):
                    player.hand[i].x_stop = (size[0]//len(player.hand))*(i) + p_whitespace
                    player.hand[i].x_move = 7
                    player.hand[i].sprite = pygame.image.load("assets\\" + player.hand[i].card_obj.name + ".png").convert()
                #Update the player's score
                player.updt_score()
                #Test if the player got a Ace+Figure pair (Blackjack)
                insta_blackjack(player)

                #Reset CPU aspects
                cpu.hand = []
                #Draw a card and check if there's cards left in the deck
                cpu.hand.append(Rectangle(deck.pop(), size[0]+3, 100, 37, 65, WHITE))
                if len(deck) == 0:
                    deck = new_deck()
                    deck_count += 1
                    if deck_count == 8:
                        done = True
                #Draw a card and check if there's cards left in the deck
                cpu.hand.append(Rectangle(deck.pop(), size[0]+409, 100, 37, 65, WHITE))
                if len(deck) == 0:
                    deck = new_deck()
                    deck_count += 1
                    if deck_count == 8:
                        done = True
                #It won't be the CPU's turn
                cpu.part_turn = False
                #Spacing for the cards in the screen
                c_whitespace = (size[0] - ((size[0]//len(cpu.hand))*(len(cpu.hand)-1) + size[0]//cpu.hand[-1].width + cpu.hand[-1].width))//2
                #Adjust where to put the cards in the screen
                for i in range(len(cpu.hand)):
                    cpu.hand[i].x_stop = size[0]//len(cpu.hand)*(i) + c_whitespace
                    cpu.hand[i].x_move = 7
                #Load the first card's sprite
                cpu.hand[0].sprite = pygame.image.load("assets\\" + cpu.hand[0].card_obj.name + ".png").convert()
                #The second card's sprite will be the Hole Card's sprite at first
                cpu.hand[1].sprite = pygame.image.load("assets\\Hole_Card.png").convert()
                #Update the CPU's score, with only the value of the first card
                cpu.updt_score()
                cpu.now_score -= cpu.hand[1].card_obj.value
                cpu.display_score = str(cpu.now_score)

            #Player clicked the QUIT box
            #Simply close the game window
            elif (quit_box.x_coord <= mouse_pos[0] <= quit_box.top_right()[0]) and (quit_box.y_coord <= mouse_pos[1] <= quit_box.bottom_right()[1]) and player.part_turn and cpu.part_turn:
                done = True
 
    #Fill the screen with black
    '''This comes before any drawings'''
    screen.fill(BLACK)

    #CPU's turn
    if cpu.part_turn and (not player.part_turn):
        #If the CPU's score is below 17 draw a card
        if cpu.now_score < 17:
            #Draw a new card
            #Each card the CPU draws is initially drawn 200 horizontal units away from the previous one
            cpu.hand.append(Rectangle(deck.pop(), size[0]+(200*(len(cpu.hand)-1)), 100, 37, 65, WHITE))
            cpu.hand[-1].sprite = pygame.image.load("assets\\" + cpu.hand[-1].card_obj.name + ".png").convert()
            #If the current deck ran out of cards then create a new one and increment the used decks counter
            if len(deck) == 0:
                deck = new_deck()
                deck_count += 1
                if deck_count == 8:
                    done = True
            #Readjust the spacing between cards and move the already existing ones on the screen
            c_whitespace = (size[0] - ((size[0]//len(cpu.hand))*(len(cpu.hand)-1) + size[0]//cpu.hand[-1].width + cpu.hand[-1].width))//2
            for i in range(len(cpu.hand)):
                cpu.hand[i].x_stop = (size[0]//len(cpu.hand))*(i) + c_whitespace
                cpu.hand[i].x_move = 5
            cpu.updt_score()
        
        #Elif the CPU is over the threshold of 17 but below 21 just end its turn and announce the round winner
        elif 17 <= cpu.now_score < 21:
            cpu.change_turn()
        
        #Elif the CPU has a score of 21, then it got a Blackjack
        elif cpu.now_score == 21:
            cpu.display_score = 'BLACKJACK'
            cpu.change_turn()
        
        #Elif the CPU blew up
        #Update the CPU's score and end its turn
        elif cpu.now_score > 21:
            cpu.updt_score()
            cpu.change_turn()

    #Decide the winner of the round
    elif not (player.part_turn or cpu.part_turn):
        print('score:',player.now_score, 'display:',player.display_score)
        print('score:',cpu.now_score, 'display:',cpu.display_score)
        print()
        #If nobody blew up it's a direct points comparison
        if int(player.now_score) <= 21 and int(cpu.now_score) <= 21:
            #Player wins
            if int(player.now_score) > int(cpu.now_score):
                round_result = 'P'
                player.rounds_won += 1
                player.change_turn()
                cpu.change_turn()
            #CPU wins
            elif int(player.now_score) < int(cpu.now_score):
                round_result = 'C'
                cpu.rounds_won += 1
                player.change_turn()
                cpu.change_turn()
            #Tie
            else:
                round_result = 'T'
                player.change_turn()
                cpu.change_turn()
        #If one of the participants blew up the winner is the one that didn't blow up
        else:
            #CPU wins
            if int(player.now_score) > 21 and int(cpu.now_score) <= 21:
                round_result = 'C'
                cpu.rounds_won += 1
                player.change_turn()
                cpu.change_turn()
            #Player wins
            elif int(player.now_score) <= 21 and int(cpu.now_score) > 21:
                round_result = 'P'
                player.rounds_won += 1
                player.change_turn()
                cpu.change_turn()
            #Tie
            else:
                round_result = 'T'
                player.change_turn()
                cpu.change_turn()

    #After deciding the winner, draw two boxes for the player to continue playing or to quit
    #Note: this is the only time both participant's turn is True
    elif player.part_turn and cpu.part_turn:
        if round_result == 'P':
            screen.blit(font.render('You win this round.', True, WHITE), (size[0]//2-70,size[1]//2-32))
        elif round_result == 'C':
            screen.blit(font.render('The CPU wins this round.', True, WHITE), (size[0]//2-88,size[1]//2-32))
        else:
            screen.blit(font.render('This round ends in a tie.', True, WHITE), (size[0]//2-95,size[1]//2-32))
        screen.blit(continue_box.sprite, (continue_box.x_coord, continue_box.y_coord))
        screen.blit(quit_box.sprite, (quit_box.x_coord, quit_box.y_coord))

    #Output in the top left corner the number of this deck and how many cards are left in it
    screen.blit(font.render('Deck ' + str(deck_count+1), True, WHITE), (10,25))
    screen.blit(font.render('Cards left in this deck: ' + str(len(deck)), True, WHITE), (10,40))
    #Output in the top right corner the number of rounds won by each participant
    screen.blit(font.render('Rounds won', True, WHITE), (615,25))
    screen.blit(font.render('CPU: ' + str(cpu.rounds_won), True, WHITE), (640,40))
    screen.blit(font.render('You: ' + str(player.rounds_won), True, WHITE), (640,55))

    #Draw the Player and CPU hands
    for i in range(len(player.hand)):
        screen.blit(player.hand[i].sprite, [player.hand[i].x_coord, player.hand[i].y_coord])
    for i in range(len(cpu.hand)):
        screen.blit(cpu.hand[i].sprite, [cpu.hand[i].x_coord, cpu.hand[i].y_coord])
    
    #Only move the cards horizontally until they reach the target coordinates
    for card in player.hand:
        if card.x_coord >= card.x_stop:
            card.x_coord -= card.x_move
    for card in cpu.hand:
        if card.x_coord >= card.x_stop:
            card.x_coord -= card.x_move

    #Output the current Player score above its cards
    screen.blit(font.render('SCORE: ' + player.display_score, True, WHITE), (73, 325))
    #Output the current CPU score below its cards (don't include the hole card value)
    screen.blit(font.render('SCORE: ' + cpu.display_score, True, WHITE), (73, 190))
    #Draw 2 boxes at the bottom of the screen for the player to HIT and/or STAND
    screen.blit(hit_box.sprite, [hit_box.x_coord, hit_box.y_coord])
    screen.blit(stand_box.sprite, [stand_box.x_coord, stand_box.y_coord])
    
    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)

#Quit the program properly
pygame.quit()