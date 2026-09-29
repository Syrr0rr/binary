import random
min = input("what is the min")
max = input("What is the max")

def set_range():
    min = input("what is the min")
    max = input("What is the max")
    while min.isdigit() == False:
        min = input("what is the min")
    while max.isdigit() == False:
        max = input("what is the min")
    min = int(min)
    max = int(max)

set_range()

target = random.randint(min,max)
Comp_count = []
Player_count = []
comp_guess = 50
comp_max = max
comp_min = min
Comp_range = []
another_round = True

def comp_play():
    global comp_guess, comp_max, comp_min, comp_replay
    if target < comp_guess:
        Comp_count.append(comp_guess)
        comp_max = comp_guess - 1
        comp_guess = (comp_max + comp_min) // 2
        comp_replay = True
    elif target > comp_guess:
        Comp_count.append(comp_guess)
        comp_min = comp_guess + 1
        comp_guess = (comp_max + comp_min) // 2
        comp_replay = True
    else:
        Comp_count.append(comp_guess)
        print("The computer guessed correctly")
        comp_replay = False
        return

def player():
    global player_guess
    player_guess = input("Enter Guess: ")
    while player_guess.isnumeric == False:
        player_guess  = input("Enter Guess: ")
    player_guess = int(player_guess)
    if player_guess > max or player_guess < min:
        print("error")
        player_guess  = input("Enter Guess: ")
    elif player_guess == target:
        print("Done") #------------------------Player got target
        Player_count.append(player_guess)
    else:
        if player_guess > target:
            print("Lower")
            Player_count.append(player_guess)
        elif player_guess < target:
            print("higher")
            Player_count.append(player_guess)

comp_replay = False
player_replay = False
def print_results():
    if len(Player_count) < len(Comp_count):
        winner = "Player"
    if len(Player_count) > len(Comp_count):
        winner = "Computer"
    if len(Player_count) == len(Comp_count):
        winner = "Tie"
    print(f"""
=========FINAL RESULTS=========


Player Guesses:
{Player_count}
Player Guess Count:{len(Player_count)}


Computer Guesses:
{Comp_count}
Player Guess Count:{len(Comp_count)}


Winner: {winner}
""")
   
while True:
    target = random.randint(min,max)
    player()
    comp_replay = True
    while comp_replay == True:
        comp_play()
    while player_guess != target:
        player()
    print_results()
    player_input = input("Another round?(y for yes, other for no): ").strip().lower()
    if player_input != "y":
        break
    Player_count = []
    Comp_count = []
    player_guess = None
    comp_guess = 50
    set_range()
    