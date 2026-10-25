import csv
import random

#Title Page
print("Charades Master")
print("A charades generator that has relatable words and phrases to nigerians without feeling forced and cringe") 

charade_bank = []
with open("charadeswords.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        charade_bank.append(row)
        print(row)             

# after loop, check total
print(f"Total words loaded: {len(charade_bank)}")
#print(charade_bank[0])          

played_charade_word = []

#Game start
print("Let's Play")

# filter by difficulty
player_difficulty = input(f"Select a difficulty (easy/medium/hard): ").lower()
filtered = [row for row in charade_bank if row['difficulty'] == player_difficulty]

#gameplay

# what if category doesn't exist?
if player_difficulty not in ['easy', 'medium', 'hard']:
    print("Category not found!")

# what if no words match the filter?
elif len(filtered) == 0:
    print("No words found for that category and difficulty!")

else:
    while True:
        charade_word = random.choice(filtered)
        print(f"Your word is: {charade_word['word']}!")
        played_charade_word.append(charade_word)
        
        play_again = input("Next word? (Y/N): ").upper()
        if play_again != 'Y':
            break

        filtered = [row for row in filtered if row not in played_charade_word]
        if len(filtered) == 0:
            print("You've played all words in this category!")
            break

# game end:
print("Thanks for playing Charades Master! 🎭")
print(f"You played {len(played_charade_word)} words today!")