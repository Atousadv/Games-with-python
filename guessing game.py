import random
start=int(input("Enter the start of the range:"))
end=int(input("Enter the end of the range:"))
target_number=random.randrange(start,end)
guess = int(input(f"Guess a number between {start} and {end}: "))

guess=0
while guess!=target_number:
    if guess<target_number:
        print("you guess is lower than the target number,try again")
        
    else:
        print("you guess is higher than the target number,try again")
    guess = int(input("Guess again: "))
    
print("you won,target numbers is" ,target_number)




