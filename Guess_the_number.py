import random

secret_number=random.randrange(1,100)
user_input=None
guessses=0

f=open("highscore.txt", "r")
highscore=int(f.read())



print('''
  $$\     $$\                                           $$\                                 $$\                                               $$\                                 
  $$ |    $$ |                                          $$ |                                $$ |                                              $$ |                                
$$$$$$\   $$$$$$$\   $$$$$$\         $$$$$$$\ $$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$\        $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$$\       
\_$$  _|  $$  __$$\ $$  __$$\       $$  _____|$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\  \____$$\ $$  _____|$$  __$$\ $$  __$$\ $$  _____|      
  $$ |    $$ |  $$ |$$$$$$$$ |      $$ /      $$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ |  $$ |$$ |  \__|$$$$$$$$ | $$$$$$$ |$$ /      $$ |  $$ |$$$$$$$$ |\$$$$$$\        
  $$ |$$\ $$ |  $$ |$$   ____|      $$ |      $$ |  $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |      $$   ____|$$  __$$ |$$ |      $$ |  $$ |$$   ____| \____$$\       
  \$$$$  |$$ |  $$ |\$$$$$$$\       \$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |            $$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$\ $$$$$$$  |      
   \____/ \__|  \__| \_______|       \_______| \____$$ |\_______/  \_______|\__|            \_______/ \__|       \_______| \_______| \_______|\__|  \__| \_______|\_______/       
                                              $$\   $$ |                                                                                                                          
                                              \$$$$$$  |                                                                                                                          
                                               \______/                                                                                                                           
''')

print("So Let's play the game with a very simple rule.")
print("The just thing you have to do is guess a number between 1-100 as per the instruction")
play_exit=input("If you want to play the game press 'p' and to exit press any other key--> ")
if play_exit=="p":
  while(secret_number!=user_input):
    guessses+=1
    user_input=int(input("Guess the number--> "))
    if secret_number==user_input:
         print("Yes, you are correct.") 
    elif secret_number>user_input:
          print("No, You are wrong. Number is smaller than secret number.")
    else:
          print("No, You are wrong. Number is bigger than secret number.")
else:
  print("Thank you")
          
if play_exit=="p":
  guessses=str(guessses)
  print(f"You guessed it correct in {guessses} guesses")
  guessses=int(guessses)
  print("You did something amazing!")
  if guessses<highscore:
    print("You just broke the highscore!")
    f=open("highscore.txt", "w")
    guessses=str(guessses)
    f.write(guessses)
  else:
    print("Not a record but Good try!")
else:
  print("Have a good day!")
