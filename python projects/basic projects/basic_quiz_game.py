#learing the basics of if and else statements, how to ensure user input variation such as capital letters do not cause the program to fail.
print("Welcome to the Quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("In which country did Manhwa originate? ")
if answer == "Korea":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("In which country did Manhua originate? ")
if answer == "China":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Is Solo Leveling a Manga, Manhwa or Manhua? ")
if answer == "Manhwa":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the name of the main character in Solo Leveling? ")
if answer == "Sung Jinwoo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You have answered: " + str(score) + " questions correct!")
print("You got: " + str(score/4 * 100) + "%.")