import random
number = random.randint(1, 128)
is_correct = False
guess = int(input("Please enter a number on interval(1,128):"))
while not is_correct:
    if guess < number:
        guess = int(input("Increase your number:"))
    elif guess > number:
        guess = int(input("Decrease your number:"))
    else:
        print("Good job, Congratulations!")
        is_correct = True
