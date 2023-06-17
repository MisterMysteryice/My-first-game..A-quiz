Playing = input("Do you want to play my quiz game? (yes/no): ")

if Playing.lower() != "yes":
    quit()
print("Okay, brudda - let's go then!")

Score = 0

Answer = input("What planet is known as the red planet?: ")
if Answer.lower() == "mars":
    print("Yaaaaayyyyyy! On to the next!")
    Score = Score + 1
else:
    print("Incorrect!")

Answer = input("What is the powerhouse of the cell?: ")
if Answer.lower() == "mitochondria":
    print("Yaaaaayyyyyy! On to the next!")
    Score = Score + 1
else:
    print("Incorrect!")

Answer = input("What is the name of the largest moon in our solar system?: ")
if Answer.lower() == "ganymede":
    print("Yaaaaayyyyyy! On to the next!")
    Score = Score + 1
else:
    print("Incorrect!")

Answer = input("What is the name of the closest star to our solar system?: ")
if Answer.lower() == "proxima centauri":
    Score = Score + 1
else:
    print("Incorrect!")

print("You got " + str(Score) + " questions correct")
print("You got " + str((Score / 4) * 100) + "%")
