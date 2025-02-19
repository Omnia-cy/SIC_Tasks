import random
dice = random.randint(1, 100)
guess = -1
CNT = 0
while dice:
    guess = int(input("Enter a number :"))
    if guess == dice:
        print("It's Correct!")
        CNT = CNT + 1
        break
    elif guess < dice:
        print("Lower!")
    elif guess > dice:
        print("Higher!")

    CNT = CNT+1
print("Congratulation Total try is ", CNT)

