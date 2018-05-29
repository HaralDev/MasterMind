#============================================================#
#
#            MasterMind, can you beat my code?
#                     by HaralDev
#
#   lines 17-122:   Functions used in main program
#   lines 126-153:  Strings and text used in main program
#   lines 157-225:  Main program
#
#============================================================#

#------------------------------------------------------------#
#              Import random integer generator               #

from random import randint


#============================================================#
#                  Functions for main program                #
#============================================================#

#------------------------------------------------------------#
#         Random four number string generator                #

def gencode():
    """ Generate a secret code for the Mastermind game
    
    runs the random generator, returns four numbers 1-6 in a 
    string, numbers are unique and not repeating"""
    
    c0de = ""                               # Empty the c0de string.
    
    while len(c0de) < 4:                    # As long as c0de string is smaller than 4 ...
        r = str(randint(1,6))  ;            # generate random integer.   
        
        if r not in c0de:                   # If the generated int is not already in string ...
            c0de += r;                      # add it to the end of the c0de string.
            
    return c0de                             # When the loop is finished, return the random 4 number string.

#------------------------------------------------------------#



#------------------------------------------------------------#
# Function to check if number is guessed in the right place  #
   
def goodplace(code, guess):
    """ Return number of correctly placed pins
    
    code  - secret code, four numbers in a string
    guess - user's guess
    
    Returns the number of correctly placed numbers in the guess
    """
    
    right1 = 0;                             # Preset right amount to zero.
    
    for i in range(4):                      # Check with loop if the character at position i is the ...
        if code[i] == guess[i]:             # same for the code and guess.
            
            right1 += 1;                    # If the if condition holds, than add 1 to right.
    
    return right1                           # Return right amount of guessed numbers in right place.
#------------------------------------------------------------#
    


#------------------------------------------------------------#
#   Function to check if a number is in the string, but not  #
#                   guessed in the right place.              #

def goodnumber(code, guess):
    """ Return number of correct but incorrectly placed pins

    code  - secret code, four numbers in a string
    guess - user's guess
    """
    
    right2 = 0;                             # Preset right amount to zero.          
    
    for j in range(4):                      # Check with loop if code at position j is in guess, but not in that place
        if code[j] in guess and code[j] != guess[j]:
            
            right2 += 1;                    # If the if condition holds, than add 1 to right.
   
    return right2                           # Return right amount of guessed numbers in wrong place
#------------------------------------------------------------#
    

#------------------------------------------------------------#
#   Function that asks user if he/she want to keep playing   #
    
def cont():
    yes_no = False;                                            # Preset to False, the user has to input a right ...
    while yes_no == False:                                     # formatted answer to the question if they want to go again. 
        
        print()
        re = input("Play again? Type Yes/No or Y/N: ");        # Prompt user with question if they want to keep playing ... 
        print()                                                # and gives them options on how to answer
        
        if re.lower() == 'yes' or re.lower() == 'y':           # Set play variable to True if they answer yes or y
            play = True
            yes_no = True
            print("========================")
            print()
            print("Alright, I'll do my best")
            
            
        if re.lower() == 'no' or re.lower() == 'n':            # Set play variable to False if they answer no or n
            play = False
            yes_no = True
            print("Thanks for playing, it was my pleasure")
            print("======================================")
    
    
        if re.lower() not in ['yes','y','no','n']:             # Ask question again if the answer isn't clear 
            print()
            yes_no = False
            print("Please give proper answer, I am not that smart")
            
    return play;                                               # Returns either True or False  
#------------------------------------------------------------#


#============================================================#
#       Introduction and string used in main program         # 
#============================================================#


#------------------------------------------------------------#
#                      Introductory text                     #
   
title = "Welcome to MasterMind"
intro = "Do you think you can break my code within 10 tries?\n\n\
This is how it works: I will have a code of 4 numbers ranging \
from 1 to 6 (eg 1435). You can guess my code (1534). I will \
tell you how well you have guessed by telling how many numbers \
are right, but not in the right place and how many numbers are \
in the right place. In our example I would tell you 2 are in the \
right place, and 2 are the right numbers, but not in the right \
place. Got it? Let's try!"


#------------------------------------------------------------#
#              Long strings for main program                 #

guess_result = 'Score : {:d} number(s) in right position, {:d} \
are right, but in the wrong position'
success1 = 'The code is indeed {:s}.'
success2 = 'You had it right on guess number {:d}, give me a rematch?'
failure = "My code beat your brain, I won't tell you the code I made, take a walk"
falseguess = "You're guess does not meet my requirements, try again"



#============================================================#
#                        Main program                        # 
#============================================================#

#------------------------------------------------------------#
#                   Introduction and input print             #

print(title)
print()
print(intro)


#------------------------------------------------------------#
#                   Main loop of program                     #


play = True                                                    # Preset play ...
while play == True:                                            # when true this plays the loop
    
    win = False;                                               # Preset to false, the player hasn't won yet! 
    
    code = gencode();                                          # Generate random four number string
    
    
    for i in range(1,11):                                       # Loop 10 times, that is how many times the user has
        
        try_i = "Guess number {:d}: ".format(i)                # Preset the string which displays the amount of times ...
                                                               # the user has already guessed
        
        ans_format = False;                                    # Preset answer format to False
        
        while ans_format == False:                             # Open loop that runs until the format of ...
                                                               # guess/answer is right
            
            guess = input(try_i)                               # Let the user input their guess
            
            if guess.isdigit == True or len(guess) == 4:       # If the guess is digit only and of length four ..    
                ans_format = True;                             # then close the loop, the guess is of right formatting. 
                
            else:                                              # If the guess is not all digits or if 
                print(falseguess);                             # guess is not of length 4, let user input ...             
                ans_format == False;                           # their guess again.   
                
        place = goodplace(code,guess);                         # Check how many numbers the user guess in the right place 
        
        if place == 4:                                         # If the user has guessed all four numbers to the right ... 
            print(success1.format(code),success2.format(i));   # place, they have won.  
            win = True
            break;                                             # Break the for loop, the user doesn't need more guesses. 
        
        col = goodnumber(code, guess);                         # Check the amount of numbers are in the string ...
                                                               # but not guessed in right place.  
        
        result = guess_result.format(place,col);               # Prepare result string            
        print(result);                                         # and print this. 



    if win == False:                                           # If the for loop has ended and the user has
        print(failure)                                         # not guessed the code, make fun of them.
    


    play = cont()                                              # Let the continue function ask if the user wants ...
                                                               # to keep playing, returns either False or True 
                                                               

#                    End of program                          # 
#============================================================#                                                               
