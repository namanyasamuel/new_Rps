import random
import sys
from enum import Enum
def play_rps():
    game_count=0
    play_wins=0
    python_wins=0
    Tie_game=0
    
    def play_game():
        nonlocal game_count
        nonlocal play_wins
        nonlocal python_wins
        nonlocal Tie_game
        
        class RPS(Enum):
            ROCK=1
            SCISSOR=2
            PAPER=3
        player_choice=input("enter\n 1 for ROCK\n 2 for SCISSOR\n 3 for PAPER\n")
        computer_choice=random.choice("123")
        if player_choice not in ["1","2","3"]:
            print("Please enter 1,2 or 3")
            return play_game()
        player=int(player_choice)
        computer=int(computer_choice)
        print("You have choose "+str(RPS(player)).replace("RPS.",""))
        print("computer have choose "+str(RPS(computer)).replace("RPS.",""))
        def decider(player,computer):
            nonlocal play_wins
            nonlocal python_wins
            nonlocal Tie_game
            if player==2 and computer==3:
                play_wins+=1
                return("Player wins")
            elif player==1 and computer==2:
                play_wins+=1
                return("player wins")
            elif player==3 and computer==1:
                play_wins+=1
                return("You win")
            elif player==computer:
                Tie_game+=1
                return("Its  a Tie")
            else:
                python_wins+=1
                return("Python wins") 
        decision=decider(player,computer)  
        print(decision)
        game_count+=1
        print("\n")
        
        print(f"You have played:{game_count} games  " )  
        print("\n TO PLAYAGAIN press")  
        while True:
            playagain=input("Enter Y for yes or Q for quit\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        if playagain.lower()=="y":
            return play_game()
           
        else:
            sys.exit(f"you have played {game_count}  games and you have won {play_wins} , lost {python_wins} and you drew {Tie_game} games")
    return play_game       
winner=play_rps()                         
winner()