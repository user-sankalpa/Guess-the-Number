import random

secret_number=random.randrange(1,100)
user_input=None
guessses=0
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
while(secret_number!=user_input):
    guessses+=1
    user_input=int(input("Guess the number--> "))
    if secret_number==user_input:
         print("Yes, you are correct.") 
    elif secret_number>user_input:
          print("No, You are wrong. Number is smaller than secret number.")
    else:
          print("No, You are wrong. Number is bigger than secret number.")
          
guessses=str(guessses)
print(f"You guessed it correct in {guessses} guesses")
