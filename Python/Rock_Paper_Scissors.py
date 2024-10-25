import random
choices=["Rock","Paper","Scissors"]
computer=random.choice(choices)
player=False
cpu_s=0
player_s=0
while True:
    player=input("Rock,Paper or Scissors : ").capitalize()
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose!")
            cpu_s+=1
        else:
            print("You Win!")
            player_s+=1
    elif player=="Paper":
        if computer=="Scissors":
            print("You lose!")
            cpu_s+=1
        else:
            print("You Win!")
            player_s+=1
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!")
            cpu_s+=1
        else:
            print("You Win!")
            player_s+=1
    elif player=="End":
        print("Final Scores:")
        print(f"CPU:{cpu_s}")
        print(f"Player:{player_s}")
        break
