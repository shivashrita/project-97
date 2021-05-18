import random
chances = 0
number = random.randint(1,9)
print("Number Guessing Game")
while chances < 5:
    guess = int(input("guess a number between 1 to 9 :"))

    if guess == number:
        print("Congratulations! You Won!!!")
        break

    if guess > number:
        print("Your Number guess is Too High")

    if guess < number:
        print("Your Number guess is Too Low")


    chances = chances +1

if not chances < 5:
    print("YOU LOSE! the number is",number) 