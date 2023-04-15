import random 

num = input("Type Number: ")

if num.isdigit():
    num = int(num)
    if num <= 0 :
        print("Please Enter your number larger then 0")
        quit()
else:
    print("Please Enter the number!...")
    quit()

random_number = random.randint(0,num)

guess = 0

while True:

    guess+=1

    guessing = input("Make Your Guess: ")

    if guessing.isdigit():
        guessing = int(guessing)
    else:
        print("Please Enter the number!...")
        continue

    if guessing == random_number:
        print("Your Guess is Correct!..")
        break

    elif guessing > random_number :
        print("you were above the number!..")
        
    else:
         print("you were below the number!..")
    
print("After "+ str(guess)+ " guess you found the answer")

