import random

number= random.randint(1,50)

print("Hey bbg, guess the number between 1 and 50 okay")


while 1:
    choice=int(input("what's your guess? "))

    if choice < number:
        print("oops, you went low")
    
    elif choice>number:
        print("oops, you went high")
    
    else:
        print("congrats queen")
        break