### This game is a basic imitation of BlackJack

import random

#start the game
def main():
    play_again = 'y'
    while play_again.lower()=='y':
        #display instructions
        instructions()
        #user plays game
        play_game()
        #ask user if want to play again
        play_again = input('Do you want to play again? (y/n)')
        
        

def instructions():
    print("'TWENTY ONE!!'")
    print('How to Play: The player plays against the computer.\n' +
          'Each round the player can choose to draw a card or freeze the game.\n'+
          'The goal is to have the total sum of your cards as close to 21 as possible(J,Q,and K are worth 10).')
    input('Press enter to start: ')
def display_menu():
    print()
    print('1. draw card')
    print('2. freeze')
    print('3. quit game')
    print()
def play_game():
    choice = 1
    running_total = 0
    while choice == 1 or choice == 2:
        display_menu()
        choice = get_choice(running_total)
                
        #figure out what to do based on users choice
        if choice == 1:     #user picks card and running total is displayed
            card = pick_card()
            print('You picked a ',card,'of',pick_suit())
            card_score = get_card_score(card)
            running_total += card_score
            print('Your running total is: ',running_total)

        elif choice == 2:      #user freezes game
            freeze(running_total)
            return()
        else :      #quit game
            return()
        
def get_choice(total): #get the users choice
    choice = int(input('Enter your choice: '))
    #validate choice
    while choice < 1 or choice > 3:
        choice = int(input('Your choice is invalid. Please enter your choice: '))
    #if users score is 21 make him/her freeze
    while total == 21 and choice == 1:
        print('Your running total is 21! Don\'t draw a card! Freeze to win the game!')
        choice = int(input('Enter 2 to freeze the game: '))
        #validate!
        while choice != 2:
            choice = int(input('Enter 2 to freeze the game: '))
    #if user picked card but total is greater than 21
    while total > 21 and choice == 1:
        print('Your running total is greater than 21.\n'+
              'If you want to freeze to see if the computer\'s score is also greater than 21 enter 2.\n'+
              'If you want to end the game press 3 to quit. ', end='')
        choice = int(input())
        while choice != 2 and choice != 3:
            choice = int(input('Enter choice 2 or 3: '))
        
    return choice

def pick_card():
    num = random.randint(1,13)
    return(num)

def get_card_score(card):
    if card > 10:
        card_score = 10
    else:
        card_score = card
    return(card_score)
    
def pick_suit():
    suit_num = random.randint(1,4)
    if suit_num == 1:
        suit= 'spades'
    elif suit_num == 2:
        suit= 'clubs'
    elif suit_num == 3:
        suit = 'hearts'
    else:
        suit = 'diamonds'
    return(suit)

def freeze(user_total):
    #run computers game- to see who will win
    computer_total = run_computer()
    if user_total > 21:
        print('Your total is greater than 21!')
        if computer_total > 21:
            print('The computers total was also over 21!\tBoth of you lost!')
        else:
            print('The computers score was under 21. You lost!\nGood Game!')

    elif computer_total < 21:
        print('Your total is',user_total,'and the computers total is',computer_total,'.')
        if user_total < computer_total:
              print('The computer won this game!')
        elif user_total > computer_total:
              print('You won this game!')
        else:
             print('This game was a tie!')
    else: 
        print('The computers total was greater than 21!')
        print('You won this game!')
        
    
def run_computer():
    total = 0
    while total < 15:
        computer_card = pick_card()
        card_score = get_card_score(computer_card)
        total += card_score
    return(total)
    
#run the program!
main()
    
