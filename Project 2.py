import random
n=random.randint(1,101)
a=-1
guesses=0
while(a!=n):
    a=int(input("Enter Your Guess Please : "))
    if(a<n):
        print("Higher Number Please")
    elif(a>n):
        print("Lower Number Please")
    guesses+=1
print(f"You have guessed the number {n} correctly in {guesses} attempts") 