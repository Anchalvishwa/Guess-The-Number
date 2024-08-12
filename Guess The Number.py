import random

Target_Number= random.randint(1,100)

print("WELCOME TO THE GAME: ---*** GUESS THE NUMBER ***---\n")
while True:
    
    User_Choice= (input("Guess The Target Number! or Quit The Game(Press Q to Quit the game): \n"))
    if(User_Choice == "Q" or User_Choice == "q"):
        break
    
    User_Choice=int(User_Choice)

    if(User_Choice == Target_Number):
        print("SUCCESS : CORRECT GUESS!!")
        break
    elif(User_Choice < Target_Number):
        print("HINT- Your Number Was Too Small : Take a Bigger Guess....")
    else:
        print("HINT- Your Number Was Too Big : Take a Smaller Guess....")



print("-----GAME OVER-----")        
    
                    