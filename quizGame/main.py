# Welcoming the user to the game
print("Welcome to My Quiz Game")

# Asking the user if they want to play
playing = input("Do you want to play? ")

# Checking if the user typed yes or no
if playing.lower() != "yes":
    quit()

# Specifying Instructions
print("Okay! Let's play!")
print("Affirm the statements by answering with true or false")

score = 0

# Questions
# 1
answer = input("Light travels in a straight line. ")
if answer.lower() == "true":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Light travels in a straight line until it meets an obstacle that can influence its angle.")

# 2
answer = input("Electrons move faster than the speed of light. ")
if answer.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Electrons are much slower than the speed of light because they have mass")

# 3
answer = input("Peanuts are not nuts! ")
if answer.lower() == "true":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Peanuts are legumes like lentils and peas. ")

# 4
answer = input("Spaghetto is the singular form of the word spaghetti. ")
if answer.lower() == "true":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("In general, Italian nouns that end in “o” are single in nature, whereas those that finish in “i” are plural."
          "Spaghetti is made using a large amount of spaghetto.")

# 5
answer = input("The capital of Australia is Sydney. ")
if answer.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("It is Canberra.")

# 6
answer = input("Seahorses have stomachs, which aid in the digestion of food. ")
if answer.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Seahorses lack stomachs and instead have intestines.")

# 7
answer = input("The United Kingdom is almost the same size as France. ")
if answer.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The UK is smaller than France.")

# 8
answer = input("The first Disney princess was Cinderella. ")
if answer.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Snow White was the first princess after she debuted in December 1937.")

# 9
answer = input("Among the letters of the alphabet, only the letter J is not included in the periodic table. ")
if answer.lower() == "true":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 10
answer = input("South Africa officially has two capital cities. ")
if answer.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("There are three: Pretoria, Cape Town, and Bloemfontein.")

print("You got " + str(score) + " points!")
print("You got " + str((score/10)* 100) + "%")