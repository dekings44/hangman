#step 1

import random
import words
import art


stages = art.stages
logo = art.logo

word_list = words.word_list


print(f'WELCOME TO\n{logo}\nGAME')


chosen_word = random.choice(word_list)

print(f'The solution starts with {chosen_word[0]} and ends with this last two letters {chosen_word[-2]}{chosen_word[-1]}')


display = []

word_length = len(chosen_word)

for letter in range(word_length):
    display += "_"
print(display)

end_of_game = False
live = 6
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        live -= 1
        if live == 0:
            end_of_game = True
            print('You lose')


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True

        print('You Won')

    print(stages[live])
