import random
print("***** WELCOME TO HANDCRICKET GAME *****\n")

#RULES OF THE GAME
def rules():
    choice=input("Enter (y) to view the rules of the game and (n) if not:")
    rules= """\n***** HAND CRICKET RULES *****
    1. Toss:
         Choose "odd" or "even" and a number between 1 and 10. The computer will pick a number too.
         If the sum matches your choice, you win the toss and decide whether to bat or bowl.
        
    2.Batting:
         Pick a number between 1 and 10 to score runs.
         If your number matches the computer’s, you’re out.
         Keep batting until you're out or until the 10 overs are up.
         
    3.Bowling:
         The computer bats, and you bowl. 
         Match the computer’s number to get it out. 
         Defend your score to win the game.

    4.Enjoy the Game:
         Play strategically, have fun, and start your cricket journey!
    *************************************************************************************************"""
    if choice=='y':
        print(rules)
        
#TOSS        
def toss():
    toss_ch= input("TOSS - Please choose either odd(o) or even(e):")
    toss_user= int(input("Enter a number(1-6):"))
    toss_comp= random.randint(1,6)
    print("Computer chose:",toss_comp,",You chose:",toss_user)
    
    #calculating the sum of tosses
    toss_value=toss_user+toss_comp
    if(toss_value%2==0):
        
        print("It's Even")
        sum_tvalue='e'
    else:
       
        print("It's Odd")
        sum_tvalue='o'
    
    if toss_ch==sum_tvalue:
        print("\nYou won the toss!")
        user_decision=input("Would you like to bat(bt) or bowl(bl):")
        return user_decision,"user"
    else:
        print("Computer won the toss!")
        computer_decision = random.choice(['bat','bowl'])
        print("Computer chooses to",computer_decision)
        return computer_decision, "computer"
    
#BATTING

def batting(player):
    print(player,"is batting now!")
    runs=0
    while(True):
        if player=="user":
            player_number= int(input("Enter a number from(1-6):"))
            opp_number=random.randint(1, 6)
        else:
            player_number=random.randint(1, 6)
            opp_number=int(input("Enter a number from(1-6):"))
        
        print(f"{'You' if player == 'user' else 'Computer'} chose: {player_number}")
        print(f"{'Computer' if player == 'user' else 'You'} chose: {opp_number}")
        
        
        if player_number== opp_number:
            print("It's Out!!")
            break
        else:
            runs+=player_number
            print(f"{player}'s score:{runs}")
    return runs
              
def bowling(player):
    print(player,"is bowling now!")
    runs=0
    while(True):
        if player=="user":
            player_number= int(input("Enter a number from(1-6):"))
            opp_number=random.randint(1, 6)
        else:
            player_number=random.randint(1, 6)
            opp_number=int(input("Enter a number from(1-6):"))
        
        print(f"{'You' if player == 'user' else 'Computer'} chose: {player_number}")
        print(f"{'Computer' if player == 'user' else 'You'} chose: {opp_number}")
        
        
        if player_number== opp_number:
            print("It's Out!!")
            break
        else:
            runs+=opp_number
            print(f"{player}'s score:{runs}")
    return runs
    
    
def startgame():
    rules()
    decision,first_player=toss()
    
    if decision=="bat":
        batter=first_player
        bowler="computer" if first_player=="user" else "user"
    else:
        batter="computer" if first_player=="user" else "computer"
        bowler=first_player
    
    first_score=batting(batter)
    second_score=bowling(bowler)
    
    if first_score>second_score:
        print(batter,"won the game!!")
    elif second_score>first_score:
        print(bowler,"won the game!!")
    else:
        print("It's a tie!!")
    
startgame()
