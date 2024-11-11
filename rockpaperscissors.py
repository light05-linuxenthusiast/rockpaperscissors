import random
print("Welcome to Rock, Paper, Scissors!")
x = True
while x:
    user_throw = int(input("Please choose a number between 1 and 3, with 1 being rock, 2 being paper, and 3 being scissors!:\n"))
    com_throw = random.randint(1, 3)
    #All possible ways computer can win
    if (user_throw == 1 and com_throw == 2) or (user_throw == 2 and com_throw == 3) or (user_throw == 3 and com_throw == 1):
        if user_throw == 1: 
            user_throw = "rock"
        elif user_throw == 2:
            user_throw = "paper"
        elif user_throw == 3:
            user_throw = 'scissors'
        #///
        if com_throw == 1: 
            com_throw = "rock"
        if com_throw == 2:
            com_throw = "paper"
        elif com_throw == 3:
            user_throw = 'scissors'
        print(f"The computer chose {com_throw}, and you chose {user_throw}")
        print(f"You lose! {com_throw} beats {user_throw}")
        while True:
            user_query2 = input("Would you like to play again (Y/N)?: ")
            if user_query2 == "Y":
                    break
            elif user_query2 == "N":
                    x = False
                    break
            else:
                    print("Please enter Y or N")
                    continue
        
    elif (com_throw == 1 and user_throw == 2) or (com_throw == 2 and user_throw == 3) or (com_throw == 3 and user_throw == 1):
        if user_throw == 1: 
            user_throw = "rock"
        elif user_throw == 2:
            user_throw = "paper"
        elif user_throw == 3:
            user_throw = 'scissors'
        #///
        if com_throw == 1: 
            com_throw = "rock"
        if com_throw == 2:
            com_throw = "paper"
        elif com_throw == 3:
            user_throw = 'scissors'
        print(f"The computer chose {com_throw}, and you chose {user_throw}")
        print(f"You lose! {user_throw} beats {com_throw}")
        while True:
            user_query2 = input("Would you like to play again (Y/N)?: ")
            if user_query2 == "Y":
                    break
            elif user_query2 == "N":
                    x = False
                    break
            else:
                    print("Please enter Y or N")
                    continue
    elif com_throw == user_throw:
        print(f"The computer chose {com_throw}, and you chose {user_throw}")
        print("It's appears it's a tie! Try again!")
        while True:
            user_query2 = input("Would you like to play again (Y/N)?: ")
            if user_query2 == "Y":
                    break
            elif user_query2 == "N":
                    x = False
                    break
            else:
                    print("Please enter Y or N")
                    continue
        

        
    
       
