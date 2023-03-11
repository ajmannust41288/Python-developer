# Dictionary
# dic = {}
# dic['a'] = 'alpha'
# dic['b'] = 'Beta'
# dic['c'] = 'Gamma'
# dic['a'] = 6
# if 'a'in dic:print(dic['a'])
# if 'a'in dic:print(dic.get('a'))
# for key in dic.keys():print(key)
# for key in dic:print(key)
# print(dic.keys())
# print(dic.values())
# for key in sorted(dic.keys()):
#   print(key,dic[key])
# print(dic.items())
# for k,v in dic.items():print(k,'>',v)
# Use of % operator
# h = {}
# h['word'] = 'Gearfield'
# h['count'] = 42
# s = 'I want %(count)d to the %(word)s' % h
# print(s)
# var=10
# del var
# list=[1,2,3,4,5,6]
# del list[2]
# print(list)
# var1={'a':23,'b':67,'c':90}
# del var1['a']
# print(var1)
# Echo the contents of a text file
# f = open('ag.txt', 'rt', encoding='utf-8')
# for line in f:
## iterates over the lines of the file
# print(line, end='')
## end='' so print does not add an end-of-line char
## since 'line' already includes the end-of-line.
# f.close()

# with open('ag.txt', 'rt', encoding='utf-8') as f:
#  for line in f:
# here line is a *unicode* string
# with open('write_test', encoding='utf-8', mode='wt') as f:
#    f.write('\u20ACunicode\u20AC\n')
# Day7 part1
# import random

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# guess = input("Guess a letter:")
# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("Wrong")
# part of challeng
# import random
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# guess = input("Guess a letter:")
# display=[]
# for _ in range(len(chosen_word)):
#  display+="_"
# print(display)
# challenge part 3
# import random
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# guess = input("Guess a letter:")
# display=[]
# for _ in range(len(chosen_word)):
#  display+="_"
# print(display)
# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
# if letter==guess:
#   display[position] =letter
# print(display)
# Challege 7 part3 4 5
# import random

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# display = []
# for _ in range(word_length):
#     display += "_"
# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# end_of_game = False
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

# #Check guessed letter
# for position in range(word_length):
#     letter = chosen_word[position]
#     print(
#         f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
#     )
#     if letter == guess:
#         display[position] = letter

# print(display)
# if "_" not in display:
#     end_of_game = True
#     print("you win ")
# Part5 challege 7
#Step 4

import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
