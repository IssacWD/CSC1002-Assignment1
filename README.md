# CSC1002-Assignment2
# Design Document for Assignment_1 (Number-Guessing)

## 1. Scope and Goals
#### 1) Goals
In this assignment, an interactive number-guessing game is to be developed. On each game, the program will first randomly choose a 4-digit number and then repeatedly prompt the user for a guess until a correct number is entered, that is, the number input exactly match the number generated randomly, while a maximum of 8 guesses is allowed per game. On each guess the game will provide the user with feedback about how many digits are exactly matched and how many digit are correct in value but incorrect in position. 
#### 2) Scope
To start the game, the user can run the programme via command line. By default, the number to be guessed is randomly chosen and hidden from the user. Alternatively, the user can request the number to be shown before before starting the game. Also, the number can be fixed for every game, if requested by the user.
After start, limitations of user's input are as below:

**a. The input should be an integer, rather than other types of data.
b. The length of the integer input should be exactly 4 digits.
c. No repeated digits in the integer.**

Any invalid input should be noticed and a warning should be sent back to the user so as to request valid input. Under the condition that the input is valid, feedback should be printed for each guess for the following information:

**a. Count of correct digits (digits from user input correctly match those from chosen number).
b. Count of common digits (digits from user input are found in chosen number but not in correct position).
c. The history of feedback printed previously, in chronological order.**

Once the times of guesses for each game reach 8, provided that no guess matches, the game should be over and the user will be asked if the game is to be started again. If any guess matches the number within 8 tries, the user will be noted by a winning message, and asked whether to start or not.

## 2. Programming Solution
#### 1) Modules Import
Modules **random**, **re**, and **sys** are imported:
```Python
import random
import re
import sys
```

#### 2) Functions Design
Three classes of functions are defined to support the game as below.

**a.** ***getNum***
This class is oriented to get some specified numbers. One function is contained, namely, ***get_int(a, b)*** , which is shown as follows:
```Python
class getNum:                      
    
    def gen_int(a, b):
        while True:
            q = random.randint(a, b+1)
            if len(set(re.findall(r'\d', str(q)))) == 4:
                break
        return q
```
This function is to generate an integer in range [a, b] without repeated digits, using the ***randint()*** and regular expression. If the random number fulfill the requirements, it will be returned.

**b.** ***testNum***
This class is oriented to check if the number fulfill some specific requirements. Three functions are contained, namely, ***t_int(n)*** , ***t_cor(m, n)*** , and ***t_pos(m, n)*** , which are shown as follows:
```Python
class testNum:
    
    def t_int(n):
        if len(set(re.findall(r'\d', n))) == 4:
            return True
        else:
            return False
    
    def t_cor(m, n):
        count = 0
        M = str(m)
        N = str(n)
        for i in range(4):
            if list(M)[i] == list(N)[i]:
                count += 1
        return count

    def t_pos(m, n):
        count = 0
        M = str(m)
        N = str(n)
        for i in list(M):
            for p in list(N):
                if p == i:
                    count += 1
        return count - testNum.t_cor(m, n)
```
The first function is to check if a number in string type is a 4-digit integer and has no repeated digits, in which regular expression is used similar to that in ***get_int(a, b)*** . The second function is to count the number of digits which exactly match each other in the same position in the integers m and n, e.g., ***t_cor(1235, 1234)*** returns 3. The third function is to count the number of digits of integer m which have same values – but in different position – as any digit of another integer n.

**c.** ***game***
This class is oriented to construct interactive programmes that works like games. One function is contained, namely, ***Number_Guessing(show_number, fix_number)*** . This function is the core portion of this number-guessing game. At the beginning, counter for guesses (the string ***attempt*** ) and a list for storing the feedback history (the list ***history*** ) are set up:
```Python
class game:
    
    def Number_Guessing(show_number, fix_number):
        attempt = 1
        history = []
        ......
```
then a ***while*** loop is founded:
```Python
while True:
            
            if fix_number:
                N = int(sys.argv[2])
            else:
                N = getNum.gen_int(1000, 10000)
            
            if show_number:
                print("Number: " + str(N))
                ......
```
The first two ***if*** flows is to check if the random number is requested to be shown or fixed for each game, which will be explained later. After these two flows, the user will be asked whether to start the game or not:
``ans = input("I want to play a game. Join me? (yes/no) : ")``
which will display:
``"I want to play a game. Join me? (yes/no) :``
If 'yes' is input, the game will start; or if 'no' is input, programme will exit directly; otherwise 'Answer me!' will be displayed as a result of any other input.
Once the game is started, the user need to input a number and the programme will check it is valid. If valid, then check if it matches the number to be guessed exactly. If it matches, the user will be noted by a winning message:
``Congratulations!! Number: XXXX``
where XXXX is the number to be guessed. If it does not match, feedback will be displayed. To print the feedback history, code is used as below:
```Python
state = num + " : Correct : " + str(testNum.t_cor(N, g)) + " Position : " + str(testNum.t_pos(N, g))

history.append(state)
for i in range(0, attempt):
    print(history[i])
```
This process goes till 8 attempts of guess is recognized. After 8 attempts, game-over message will be displayed and the game need to be start again, while the counter of the number of guesses will be reset to 1:
```Python
if attempt > 8:
    attempt = 1
    print("Game over! Number: " + str(N))
    break
```
As the ***if*** loop commands to break, the ***while*** loop under the condition that ***ans == 'yes'*** will break:
```Python
ans = input("I want to play a game. Join me? (yes/no) : ")
if ans == 'yes':
    while True:
        times = str(attempt) + '/' + '8'
        num = input("Your Guess {} : ".format(times))
        ......
```
and the user will be asked whether to start again.

#### 3) Startup Design
When the user is about to start the programme via command line, arguments on whether to show the random number before start or on whether to fix a number for each game, can be passed to the programme. The core code is as follows:
```Python
if __name__ == '__main__':
    
    if len(sys.argv) == 2 and sys.argv[1] == 'show':
        show_number = True
        fix_number = False

    elif len(sys.argv) == 3 and sys.argv[1] == 'fix':
        if testNum.t_int(sys.argv[2]):
            show_number = True
            fix_number = True
    else:
        show_number = False
        fix_number = False
```
**a. Show the number**
If 'show' is following the file name, say, guess.py, the parameter ***show_number*** will be assigned ***True*** , which will affect the loop in the function ***Number_Guessing(show_number, fix_number)*** (see code in **c.** ***game*** ). Then the number will be shown before starting the game:
```Python
if show_number:
    print("Number: " + str(N))

ans = input("I want to play a game. Join me? (yes/no) : ")
......
```
**b. Fix the number**
If 'fix' and an integer 'XXXX' are following the file name, the number to be guessed for each game will be fixed as 'XXXX' and it will be shown before starting the game. See example as below:
```bash
bash-3.2$ python3 /users/apple/assignment1.py fix 1234
Number: 1234
I want to play a game. Join me? (yes/no) :
```

## 3. Limitation and Enhancement
#### 1) Limitation
Although, when prompting the user to input a number, the programme is able to recognized some invalid input such as integer with repeated digits, integer out of range [1000, 9999], or other types of data like a string, quantities of types of input can raise error and quit the programme. For instance, if a string with operator, say, '12ea9323=defa', is input, error is displayed as follows:
```bash
Your Guess 1/8 : 12ea9323=defa
Traceback (most recent call last):
  File "/users/apple/assignment1.py", line 97, in <module>
    game.Number_Guessing(show_number, fix_number)
  File "/users/apple/assignment1.py", line 61, in Number_Guessing
    if testNum.t_int(num) and int(num) == N:               #Test if the input is valid
ValueError: invalid literal for int() with base 10: '12ea9323=defa'
```
More conditions should be defined for test of other types of input.

#### 2) Enhancement
The regex used currently is as below:
```Python
if len(set(re.findall(r'\d', n))) == 4:
```
In order to enhance the test for validity of input, regular expressions which are sophisticated enough to match a slew of types of input should be developed.

