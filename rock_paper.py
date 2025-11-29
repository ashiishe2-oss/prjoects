import random
choices = ["rock","paper","scissor"]
comp = random.choice(choices)
user = input("YOUR CHOICE: ").lower()
print(f"THE COMPUTER CHOOSE {comp} AND THE USER CHOOSED {user}")
try:
    if user==comp:
        print("TIEE!")

    elif user=="rock"and comp =="paper":

        print("YOU LOST")

    elif user=="rock"and comp =="scissor":
        print("YOU WIN!!")

    elif user=="scissor"and comp =="paper":
        print("YOU WIN!!")

    elif user=="scissor"and comp =="rock":
        print("YOU LOST!")

    elif user=="paper"and comp =="rock":
        print("YOU WINN!")

    else:
        print("YOU LOST!")
except ValueError:
    print("INVALID INPUT TRY AGAIN :(")


