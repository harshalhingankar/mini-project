import random

target=random.randint(1,100)
while True:
    user=input("Guess the number or  to quit : ")
    if user=='quit':
        break
    user=int(user)
    if user==target:
        print("You have sucessfuly guess the no.")
        print("-----------GAME OVER------------")
    elif user > target:
        print("you have enter the greater no. then the target no. Please try again!")
    else:
        print("you have enter the very small no. then the target no.  Please try again!")

print("-------GAME OVER ---------")
