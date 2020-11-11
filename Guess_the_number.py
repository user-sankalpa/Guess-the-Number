import random

secret_number=random.randrange(1,100)
user_input=None
guessses=0
while(secret_number!=user_input):
    guessses+=1
    user_input=int(input("Guess the  number--> "))
    if secret_number==user_input:
         print("Yes, you are correct.") 
    elif secret_number>user_input:
          print("No, You are wrong. Number is smaller than secret number.")
    else:
          print("No, You are wrong. Number is bigger than secret number.")
          
print("You guessed it correct in "+ guessses+ " guesses")
