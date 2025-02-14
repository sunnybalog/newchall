###
# Description
# Rock, paper, scissors is a well-known hand game. Each one of two players simultaneously forms one of three shapes with their hands, and then, depending on the chosen shapes, the winner is determined: rock beats scissors, paper wins over rock, scissors beat paper.
# The game is widely used to make a fair decision between equal options.

# Well, now let's do something real. Nobody wants the game where you always lose.
# Using the power of the random module, we'll make a truly interesting game.

# You should write a program that reads input from the user, chooses a random option and then says who won, the user or the computer.
# There are a few examples below, providing output for any outcome (<option> is the option chosen by your program):
#    Lose -> Sorry, but the computer chose <option>
 #   Draw -> There is a draw (<option>)
  #  Win -> Well done. The computer chose <option> and failed
# Objectives
# Your program should:
#    Read user's input specifying the option that user has chosen
#     Choose a random option
#     Compare the options and determine the winner
#     Output a line depending on the result of the game:
#         Lose -> Sorry, but the computer chose <option>
#         Draw -> There is a draw (<option>)
#         Win -> Well done. The computer chose <option> and failed
#         """

import random
x = input().lower()

list = ('scissors', 'paper', 'rock')
random.seed(2)
y = random.choice(list)

if x == 'paper' and y == 'paper':
    print('There is a draw (paper)')
elif x == 'scissors' and y == 'scissors':
    print('There is a draw (scissors)')   
elif x == 'rock' and y == 'rock':
    print('There is a draw (rock)')   
elif x == 'scissors' and y == 'rock':
    print('Sorry, but the computer chose rock')
elif x == 'rock' and y == 'scissors':
    print('Well done, The computer chose scissors and failed')  
elif x == 'rock' and y == 'paper':
    print('Sorry, but the computer chose paper')  
elif x == 'paper' and y == 'rock':
    print('Well done, The computer chose rock and failed')   
elif x == 'paper' and y == 'scissors':
    print('Sorry, but the computer chose scissors')  
elif x == 'scissors' and y == 'paper':
    print('Well done, The computer chose paper and failed')      
else:
    print('Invalid input: choose either scissors, paper or rock') 

  """
Modifying loops
Loop control statements are nested inside loops and designed to change their typical behavior. In this topic, we'll find out how they work and what they are used for.
How to break
The break statement is used to terminate a loop of any type (i. e. for and while loops). It may be said that break "jumps out" of the loop where it was placed. Let’s examine a tiny example:
pets = ['dog', 'cat', 'parrot']
for pet in pets:
    print(pet)
    if pet == 'cat':
        break
We wanted to stop the loop before it iterated for the last time. For that purpose, we introduced a condition when the loop should be stopped. The output is as follows:
dog
cat
Be careful where you put print(). If you put it at the loop’s end, the output will return only the first value – ‘dog’. This happens because break exits from the loop immediately.
Often enough, break is used to stop endless while loops like this one:
count = 0
while True:
    print("I am Infinite Loop")
    count += 1
    if count == 13:
        break
How to continue
The continue operator is commonly used, too. You can stop the iteration if your condition is true and return to the beginning of the loop (that is, jump to the loop's top and continue execution with the next value). Look at the following example:
pets = ['dog', 'cat', 'parrot']
"""
for pet in pets:
    if pet == 'dog':
        continue
    print(pet)
"""
The output will contain all values except the first one ('dog') since it fulfills the condition:
cat
parrot
Thus, the loop just skips one value and goes on running.
One nuance is worth mentioning: the continue operator should be used moderately. Sometimes you can shorten the code by simply using an if statement with the reversed condition:
"""
pets = ['dog', 'cat', 'parrot']
for pet in pets:
    if pet != 'dog':
        print(pet)
"""
In this case, the output will remain the same:
cat
parrot
Loop else clause
If the loop didn’t encounter the break statement, an else clause can be used to specify a block of code to be executed after the loop.
"""
                                                                                                                                           
pets = ['dog', 'cat', 'parrot']
for pet in pets:
    print(pet)
else:
    print('We need a turtle!')
                                                                                                                                           
"""
So after the loop body, the else statement will execute:
dog
cat
parrot
We need a turtle!
Importantly, loop else runs if and only if the loop is exited normally (without hitting break). Also, it is run when the loop is never executed (e. g. the condition of the while loop is false right from the start). Consider an example:
"""
pancakes = 2
while pancakes > 0:
    print("I'm the happiest human being in the world!")
    pancakes -= 1
    if pancakes == 0:
        print("Now I have no pancakes!")
        break
else:
    print("No pancakes...")
"""
When we run the code for the first time we'll get this output:

I'm the happiest human being in the world!
I'm the happiest human being in the world!
Now I have no pancakes!
"""

"""
Execution of the code snippet for the second time (when the condition is not met, for pancakes = 0) will end up with another message:
No pancakes...
In conclusion
To sum up, loop control statements represent a useful tool to alter the way a loop works. You can introduce extra conditions using break, continue and else operators. In addition, they allow you to print a message after the successful code execution, skip a beforehand selected set of values, or even terminate an endless loop. Use them wisely and they'll work wonders.
    break:It may help to exit an infinite loop.
    continue: It skips the current iteration under some specified condition    
else after a for loop: After a certain number of iterations, it runs an additional code.
else after a while loop: 
It executes some block of code if the loop's condition is false.
"""

pancakes = 2
while pancakes > 0:
    print("I'm the happiest human being in the world!")
    pancakes -= 1
    if pancakes == 0:
        print("Now I have no pancakes!")
        break
else:
    print("No pancakes...")

limit = 25
numbers = []
while len(numbers) < 5:
    for i in range(limit):
        if i % 3 != 0:
            continue
        else:
            numbers.append(i)

print(len(numbers))

import random                      # 1
                                # 2
n_guesses = 0                      # 3
while n_guesses < 5:               # 4
    number = random.randint(1, 5)  # 5
    guess = int(input())           # 6
    if guess == number:            # 7
        print('Yes!')              # 8
    else:                          # 9
        print('No!')               # 10
    n_guesses += 1                 # 11
"""
LOOP CONTROL STATEMENTS
Vowels and consonants

Let's work with texts! You'll get a sequence of characters (a word, a sentence or just gibberish). For each character tell if it's a vowel or a consonant. If you hit a non-alphabetic symbol, just stop processing.

The input format:

One line with N characters.

We will use letters from the English alphabet. The symbols aeiou are considered vowels. Treat the rest of the letters as consonants.

The output format:

Print the line vowel if the character is a vowel, and consonant if the character is consonant. Stop printing information at the first non-alphabetic symbol.
"""
n_letters = input().lower()
n_lenght = len(n_letters)
n_vowels = 'aeiou'
n_consonant = 'bcdfjpvwxyzqrstklmngh'

for next_letter in n_letters:
    if next_letter in n_vowels:
        print('vowel')
    elif next_letter in n_consonant:
        print('consonant')
    else:
        break
    
"""
CAT CAFES
Kitty wants to visit a cat café! Help her find the one with the largest number of cats.

Input format
Each string contains a café's name followed by a space and the number of cats in it, e.g. Paws 11, Kittens 9.
The names would be one-word only. Read input lines until you get a string MEOW (without any number).
Output format
The café with the maximum number of cats.
"""
items = 0
cat_cafe = ''
cat_names = []
cat_num = []
cat_nu = []
cat_na = []
# for ind in cat_cafe:
while cat_cafe != 'MEOW':
    cat_cafe = input().split()
    cat_na = cat_na + [cat_cafe[0]]
    cat_nu = cat_nu + [cat_cafe[1]]
    items += 1    
    print(type(cat_nu))
    cnum_max = max(cat_nu)
    print('cnum_max = ' + cnum_max)
    cnames_index = cnum_max(cnum_max)
    print(cat_names[cnames_index])

def cafe_name(cafe_names_cats_numbers):
    while True:
        cafe_info = input().split()
        if len(cafe_info) > 1:
            cafe_names_cats_numbers[int(cafe_info[1])] = cafe_info[0]
        else:
            break
    return cafe_names_cats_numbers.get(max(cafe_names_cats_numbers.keys()))
dicti = dict()    
print(cafe_name(dicti))
       """
Calculate the arithmetic mean of integer numbers and output it. You will receive the integers on separate lines. The numeric sequence ends with a period ., so stop reading the input on it.
Don't round your result before outputting it.
The input will always have at least one number."""

new_number = 0
summation = 0
number_count = 0
while True:
    new_number = input()
    if new_number != '.':
        new_number = int(new_number)
        summation = summation + new_number
        number_count += 1

    else:
        break       
print(summation / number_count)

