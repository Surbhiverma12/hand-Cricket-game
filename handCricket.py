import random as r

print("____ Hand Cricket Game ____\n\n")

print("Enter numbers between 1 and 6. If you both choose the same number, the game will be over.\n")
scoreU = 0
isOut = False

while not isOut:
    userIp = int(input("\nEnter a number (1-6): "))
    comIp = r.randint(1, 6)
    if userIp > 0 and userIp <= 6:
        print("\nUser chose: ", userIp)
        print("Computer chose: ", comIp)

        if userIp != comIp:
            scoreU += userIp
            print("\nYour score is:", scoreU)
        else:
            print("\n\nGame over! Your final score is:", scoreU)
            isOut = True
    else:
        print("Invalid number! Please enter a number between 1 and 6.")
