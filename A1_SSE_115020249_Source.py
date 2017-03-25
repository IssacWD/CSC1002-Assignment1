import random
import re
import sys

class getNum:                                                         #A class for generating a number 
                                                                      
    def gen_int(a, b):                                                #A function for generating a four-digit integer wihout repeating digits
        while True:
            q = random.randint(a, b+1)                                #Range for random
            if len(set(re.findall(r'\d', str(q)))) == 4:              #Regex for checking the type and digits
                break
        return q
    
class testNum:                                                        #A class for testing the properties of a number
    
    def t_int(n):                                                     #A function for identifying a four-digit integer without repeating digits
        if len(set(re.findall(r'\d', n))) == 4:
            return True
        else:
            return False
    
    def t_cor(m, n):                                                  #A function for checking the number of correct values in correct positions
        count = 0
        M = str(m)
        N = str(n)
        for i in range(4):
            if list(M)[i] == list(N)[i]:
                count += 1
        return count

    def t_pos(m, n):                                                  #A function for checking the number of correct values in incorrect positions
        count = 0
        M = str(m)
        N = str(n)
        for i in list(M):
            for p in list(N):
                if p == i:
                    count += 1
        return count - testNum.t_cor(m, n)

class game:                                                            #A class for designing games
    
    def Number_Guessing(show_number, fix_number):                      #A function for the game of number guessing
        attempt = 1                                                    #To set a limitation of attempts
        history = []
        while True:
            
            if fix_number:                                             #To check if there is a fixed number to be used
                N = int(sys.argv[2])
            else:
                N = getNum.gen_int(1000, 10000)                        #Otherwise a random four-digit number is generated
            
            if show_number:                                            #To check if the number is to be showed
                print("Number: " + str(N))
            
            ans = input("I want to play a game. Join me? (yes/no) : ")     #Prompt the user to choose if the game is to be started
            if ans == 'yes':                                               #Game starts
                while True:
                    times = str(attempt) + '/' + '8'
                    num = input("Your Guess {} : ".format(times))          #Get a number from the user
                    if testNum.t_int(num) and int(num) == N:               #Test if the input is valid
                        print("Congratulations!! Number: " + str(N))
                        attempt = 1
                        break                                              #Win the game
                    elif testNum.t_int(num):
                        g = int(num)
                        state = num + " : Correct : " + str(testNum.t_cor(N, g)) + " Position : " + str(testNum.t_pos(N, g))    #Give feedback to the user
                        history.append(state)
                        for i in range(0, attempt):
                            print(history[i])                              #Show the history of guess
                        attempt += 1
                        if attempt > 8:                                    #Maximum of 8 attempts
                            attempt = 1
                            print("Game over! Number: " + str(N))          #Game over by running out of the 8 chances
                            break
                    else:
                        print("Invalid input! Please input a four-digit integer without repeating digits.")                      #Warn the user for invalid input
            elif ans == 'no':
                break                                                      #Quit the game
            else:
                print("Answer me!")                                        #Request a choice of continuing or quiting the game

if __name__ == '__main__':
    
    if len(sys.argv) == 2 and sys.argv[1] == 'show':                       #To show the number that is randomly generated
        show_number = True
        fix_number = False

    elif len(sys.argv) == 3 and sys.argv[1] == 'fix':                      #To fix a number for guessing throughout the game and show it as well
        if testNum.t_int(sys.argv[2]):
            show_number = True
            fix_number = True
    else:
        show_number = False
        fix_number = False
    
    game.Number_Guessing(show_number, fix_number)