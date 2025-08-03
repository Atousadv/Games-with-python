import random
user=input("choose Odd or Even:").strip().lower()
user_choice=int(input("pick a number between 0,100: "))
print(f"user_choice: {user_choice}")
computer_choice=random.randrange(0,101)
print(f"computer_choice: {computer_choice}")
total=user_choice+computer_choice
result="Even" if total%2==0 else "Odd"
print(f"total is {result}")
if user==result.lower():
    print("you win!")
else:
    print("computer wins!")

