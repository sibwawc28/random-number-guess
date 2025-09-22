import random
#python doesnt have do while loop

score=0

def play ():

    number= random.randint(1,50)

    print("Hey bbg, guess the number between 1 and 50 okay")
    print("PS: you only get 15 tries")

    tries=1
    global score

    while tries<=15:
        choice=int(input("what's your guess? "))
        tries+=1

        if choice < number:
            print("oops, you went low")
    
        elif choice>number:
            print("oops, you went high")
    
        else:
            print("congrats queen")
            score+=1
            break

    else:    #python has a while-else loop
        print("sorry queen, went out of tries. the number was", number)



playing=1

while (playing==1) :
    play()
    print("your score so far: ", score)
    playing=int(input("enter 1 if you want to play again, 0 to stop "))
    tries=1

print(f"final score: {score}")