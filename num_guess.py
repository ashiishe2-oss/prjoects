import random

print("WELCOME TO THE GUESS QUIZZ!")

comp_choice = random.randint(1,100)
num = 0
while num !=comp_choice:
    try:
        num = int(input("Guess the number: "))
        
    
        if num>comp_choice:
                print("YOUR NUM IS TOO HIGH!!")

        elif comp_choice>num:
                print("YOUR NUM IS TOO LOW")
        else:
                print("YOU GUESSED IT RIGHT")
                print("CONGOO MATEEE!!!")
                break
    except:
            print("INVALID INPUT ")
    


