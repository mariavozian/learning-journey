import random

while True:
    level = input("Chose level:\n 1-Easy\n 2-Medium\n 3-Hard\n ")

    if level == "1":
        num_s = random.randint(1,50)
        print("You have plenty of chances")
        while True:
            num = int(input("Guess the number between 1 and 50: "))
            if num > num_s:
                print("Less")
            elif num < num_s:
                print("More")
            else:
                print("You are guessing the number")
                break

    if level == "2":
        num_s = random.randint(1,100)
        print("You have 5 chances")
        for i in range(5):
            num = int(input("Guess the number between 1 and 100: "))
            if num > num_s:
                print("Less")
            elif num < num_s:
                print("More")
            else:
                print("You are guessing the number")
                break
        else:
            print("You are not guessing the number and don't have more chances", f"Number was {num_s}")

    if level == "3":
        num_s = random.randint(1,1000)
        print("You have 10 chances")
        for i in range(10):
            num = int(input("Guess the number between 1 and 1000: "))
            if num > num_s:
                print("Less")
            elif num < num_s:
                print("More")
            else:
                print("You are guessing the number")
                break
        else:
            print("You are not guessing the number and don't have more chances", f"Number was {num_s}")

    try_again = input("Do you want to try again? (yes/no): ")

    if try_again.lower() == "yes":
        continue
    else:
        print("Thank you for your time")
        break