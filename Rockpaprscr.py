import random
print(" r for Rock \n p for Paper \n s for Scissor ")
youin=input("Enter your choice : ")
computer=random.choice([1,2,3])
dct={"r":1 , "p":2 , "s":3}  
dctrev={1:"ROCk" , 2:"PAPER" , 3:"SCISSOR"}
you=dct[youin]

print(f"You choosed {dctrev[you]} \n And \n Computer Choosed {dctrev[computer]}.")

if youin not in dct:
    print("Invalid Input..\n try again")

elif you==computer:
    print("Draw")

else:
    if (computer==1 and you==2) :   
        print("you won ")
    
    elif (computer==1 and you==3) :   
        print("you loose ")  

    elif (computer==2 and you==1) :   
        print("you loose ") 

    elif (computer==2 and you==3) :   
        print("you won ")

    elif (computer==3 and you==1) :   
        print("you won ")

    elif (computer==3 and you==2) :   
        print("you loose ")

    else:
        print("somethong went wrong")
