#Christina
#Rock Paper Scissors game

#functions
import random
print("Hello, Welcome to the Rock Paper Scissors Game!")
player_score=0
tie_score=0
computer_score=0


def rps():
            computer=random.randint(1,3)
            if computer==1:
                computer= "Scissors"
            elif computer==2:
                computer="Paper"
            elif computer==3:
                computer="Rock"
            player=input("Please Choose: Rock, Paper, or Scissors?: ")
            if computer== "Rock" and player== "Rock":
                global tie_score
                print(f"TIE!")
                tie_score= tie_score+1
                all()
            elif computer== "Rock" and player == "Scissors":
                global computer_score
                global player_score
                print(f"{computer})beats {player}\n One point for the computer")
                computer_score=computer_score +1
                all()
            elif computer== "Rock" and player== "Paper":
                global player_score
                print(f"{player} beats {computer} \n One point for the player")
                player_score=player_score+1
                all()

            elif computer== "Paper" and player== "Paper":
                print(f"TIE!")
                tie_score= tie_score+1
                all()
            elif computer== "Paper" and player == "Rock":
                print(f"{computer})beats {player}\n One point for the computer")
                computer_score=computer_score +1
                all()
            elif computer== "Paper" and player== "Scissors":
                print(f"{player} beats {computer} \n One point for the player")
                player_score=player_score+1
                all()

            elif computer== "Scissors" and player== "Scissors":
                print(f"TIE!")
                tie_score= tie_score+1
                all()
            elif computer== "Scissors" and player == "Paper":
                print(f"{computer})beats {player}\n One point for the computer")
                computer_score=computer_score +1
                all()
            elif computer== "Scissors" and player== "Rock":
                print(f"{player} beats {computer} \n One point for the player")
                player_score=player_score+1
                all()



def scoreplayer():
            global player_score
            print(f"Player's Score: {player_score}")
def scoretie():
            global tie_score
            print(f"Tied Score:{tie_score}")
def scorecomp():
            global computer_score
            print(f"Computer's score:{computer_score}")

def game():
        while True:
            tired=int(input("Would you like to continue or leave?: "))
            if tired=="continue":
                    continue
            else:
                print("Nice Playing,Goodbye!")
                break

def all():
            scoreplayer()
            scoretie()
            scorecomp()
            game()

#main
rps()
