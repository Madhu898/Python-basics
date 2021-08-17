import random as r
list=['s','g','w']
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
print("snake and  water and  game ")
print("guess (enter ) s -> for snake \n w -> for water \n g -> for gun")
while no_of_chance<chance:
    _input = input('s-> for Snake, w-> for Water,g-> for Gun:')
    _random = r.choice(list)

    if _input == _random:
        print("Tie Both 0 point to each \n ")
    #if input is snake 

    
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")#this f strings are used to print the out put  in a singgle line with strings without specifying the comma

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
   
    #if input is gun
    elif _input=='g'and _random=='w':
        computer_point=computer_point+1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins one point \n")
        print(f"computer point is {computer_point}and human point is {human_point} \n")
    elif _input=='g'and _random=='s':
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("humans wins one point \n")
        print(f"computer point is {computer_point} and human point is {human_point} \n")

    #if input is water 
    elif _input=='w'and _random=='g':
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("human wins 1 point \n")
        print(f"computer point is {computer_point} and human point is {human_point} \n")
    elif _input=='w' and _random=='s':
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer is {_random} \n")
        print("computer wins one point \n")
        print(f"computer point is {computer_point} and human points are {human_point} \n")
    else:
        print("invalid input !! ")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
print("Game over")
if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")




    
