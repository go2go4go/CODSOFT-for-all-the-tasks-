import random
choices=('rock','paper','scissors')
user_score=0
computer_score=0

def game(user,computer):
    global user_score
    global computer_score
    print(f"You choose {user},computer choose{computer}")
    if user==computer:
        print(f"Both players selected {user}.It is a tie\n")
    elif user=="rock":
        if computer=="scissors":
            user_score += 1
            print(f"Rock smashes scissors..You scored 1 point . Your score is {user_score},Computer score is {computer_score}\n")
        else:
            computer_score +=1
            print(f"Paper covers Rock.. computer scorsd 1 point. Your score is {user_score}, Computer score is {computer_score} ")
    elif user=="paper":
        if computer=="rock":
            user_score += 1
            print(f"Paper covers Rock..You scored 1 point . Your score is {user_score},Computer score is {computer_score}\n")
        else:
            computer_score +=1
            print(f"Scissors cuts paper.. computer scorsd 1 point. Your score is {user_score}, Computer score is {computer_score} ")
    elif user=="scissors":
        if computer=="paper":
            user_score += 1
            print(f"Scissors cut paper..You scored 1 point . Your score is {user_score},Computer score is {computer_score}\n")
        else:
            computer_score +=1
            print(f"Rock smashes scissors.. computer scorsd 1 point. Your score is {user_score}, Computer score is {computer_score} ")
    
while True:
    if user_score==10:
        print("#"*20,"Your score reached 10......$ YOU WIN $\n","#"*20)
        exit()
    elif computer_score==10:
        print("#"*20,"Your score reached 10......Unfortunately YOU LOSE","#"*20)
        exit()
    user_choice=input("Enter your choice(rock,paper,scissors):=>").lower()
    computer_choice=random.choice(choices) 
    if user_choice=="Quit game":
        print("Finish game")
        exit()
    elif not user_choice in choices:
        print("Sorry..that is wrong choice")
    else:
        game(user_choice,computer_choice)