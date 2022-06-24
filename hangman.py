#step 1

import streamlit as st

import random
import words
import art


stages = art.stages
logo = art.logo

word_list = words.word_list

st.title(f'WELCOME TO HANGMAN GAME')
print(f'WELCOME TO\n{logo}\n') 

print('INSTRUCTION:\n This game has 6 lives. for every time you guess the letter wrong, you help build the gallow')
st.subheader('INSTRUCTION: The game has 6 lives. for every time you guess the letter wrong, you help build the gallow\n')

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


    if guess in display:
        print(f'You have already guessed {guess}')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:

        
        live -= 1
        print(f'You guessed {guess}, that is not in the word. You lose a life.\n You have {live} lives left')
        if live == 0:
            end_of_game = True
            print(f'Sorry, You lose.\nThe correct word is {chosen_word}')
           


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True


        print('You Won')

    print(stages[live])
