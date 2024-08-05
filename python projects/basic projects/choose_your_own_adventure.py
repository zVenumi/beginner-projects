# if and else loops 

name = input("Type your name: ")
print("Welcome", name , "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go?")

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across. Type to walk to walk around and swim to swim across: ")
    
    if answer == "swim":
        print("You swim across and were eaten by an aligator. You lose.")
    elif answer =="walk":
        print("You walked for many miles and ran out of water. You die from thirst. You lose.")
    else:
        print("Not a valid option. You lose.")
    
elif answer =="right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back): ")
    if answer == "back":
        print("You go back and get eaten by a bear, You lose.")
    elif answer == "cross":
            answer = input(
                "You cross the bridge and meet a stranger. Do you talk to them? (yes/no)")
        
            if answer == "yes":
                print("You talk to the stranger and they teach you the ways of casting testicular torsion. YOU WIN!")
            elif answer == "no":
                print("You ignore the stranger and he casts testicular torsion on you, leaving you in pain till you die. You lose.")
            else:
                print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
        
else:
    print("Not a valid option. You lose.")
    
print("Thank you for trying", name)
