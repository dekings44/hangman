#step 1

import random

from numpy import disp

word_list = ['ardvark', 'baboon', 'camel']



chosen_word = random.choice(word_list)

print(f'The solution is {chosen_word}')


display = []

word_length = len(chosen_word)

for letter in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True

    print('You Won')
