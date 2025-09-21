import random

number= random.randint(1,50)

print("Hey bbg, guess the number between 1 and 50 okay")
print("PS: you only get 15 tries")

tries=1

while tries<=15:
    choice=int(input("what's your guess? "))
    tries+=1

    if choice < number:
        print("oops, you went low")
    
    elif choice>number:
        print("oops, you went high")
    
    else:
        print("congrats queen")
        break

else:    #python has a while-else loop
    print("sorry queen, went of of tries")