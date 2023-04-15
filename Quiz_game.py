print("Welcome to my computer quiz")

playing = input("Do You Want to play (yes/no)? ").lower()

if playing != "yes":
    quit()

print("Okey! Lets Play :) ")

score = 0

answer = input("what does CEO stands for? ").lower()

if answer == "chief executive officer":
    print("It's Correct")
    score+=1
else:
    print("Incorrect")

answer = input("what does CPU stands for? ").lower()

if answer == "central processing unit":
    print("It's Correct")
    score+=1
else:
    print("Incorrect")

answer = input("what does Mrss. stands for? ").lower()

if answer == "mistress":
    print("It's Correct")
    score+=1
else:
    print("Incorrect")

answer = input("what does H2O stands for? ").lower() 

if answer == "water":
    print("It's Correct")
    score+=1
else:
    print("Incorrect")

answer = input("what does LILO stands for? ").lower() 

if answer == "linux loader":
    print("It's Correct")
    score+=1
else:
    print("Incorrect")

print("You Got "+str(score)+" Score")

print("You Got "+str((score/5)*100)+"%")
