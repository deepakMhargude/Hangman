import random
import hanmanstage

word_list=["javascript", "java", "python","node", "react"]
live =6
chosen_word=random.choice(word_list)
# print(chosen_word)

display=[]
for letter in chosen_word:
    display+= "_"
print(display)

game_over=False
while not game_over:
    guessed_letter=input("Guess letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        live -= 1
        if live == 0:
            game_over=True
            print("You lose")

    if "_" not in display:
        game_over= True
        print("You win!")
    print(hanmanstage.stage[live])