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

played_charade_word = []

#Game start
print("Let's Play")

# setup teams
num_teams = int(input("How many teams are playing?: "))
teams = {}
for i in range(num_teams):
    team_name = input(f"Enter name for team {i+1}: ")
    teams[team_name] = 0    # score starts at 0

for team in teams:
    print(f"\n{team}'s turn!")
    
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
        print(f"Your word is: {charade_word['word']}!").upper()
        played_charade_word.append(charade_word)
        
        play_again = input("Next word? (Y/N): ").upper()
        if play_again != 'Y':
            break

        filtered = [row for row in filtered if row not in played_charade_word]
        if len(filtered) == 0:
            print("You've played all words in this category!")
            break

# final scoreboard
for team, score in teams.items():
    print(f"{team}: {score} points")

# game end:
print("Thanks for playing Charades Master! 🎭")