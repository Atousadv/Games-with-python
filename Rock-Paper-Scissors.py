print("Rock paper Scissors")
import random
print('Rock=1')
print('Paper=2')
print('Scissors=3')
player_wins=0
computer_wins=0
computer=random.randint(1,3)
while player_wins<5 and computer_wins<5:
    try:
    
      player=int(input("pick a number(1.Rock 2.Paper 3.Scissors):"))
      if player not in [1,2,3]:
        print("not valid number,Try again!")
        continue
    except ValueError:
      print("please enter a number")
      continue

      

    print(f'you chose {player}')
    print(f'computer chose{computer}')

    if player==computer:
      print("try again")

    elif player==1 and computer==3:
      print("player wins")
    elif player==2 and computer==1:
      print("player wins")
    elif player==3 and computer==2:
      print("This round player is the winner")
      player_wins += 1
    else:
      print("Computer is the winner")
      computer_wins += 1
    
if player_wins==5:
    print("player is the final winner,Game is over!")

else:
    print("Computer is the final winner,Game is over!")


