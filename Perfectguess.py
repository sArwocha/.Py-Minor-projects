import random                      #python module
n=random.randint(2,99)
a=1
guess=0

while(a!=n):
    a=int(input("Enter the number of your guess ::"))
   
    if(a < n):
        print(" Guess Higher Number.")
        guess+=1

    else:
        print('Guess Lower Number.')
        guess+=1

    #end of loop
print(f"you guessed the number {n} in {guess} attempts. ")

    