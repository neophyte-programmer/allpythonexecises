name = input("Type your name: ")
print("Hello", name, "Welcome to this adventure! ")

answer = input("You are on a dirt road and you have arrived at a juncture leading left or right. "
               "Which way do you go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can either swim across it or walk around it. "
                   "Type walk to walk around or swim to swim across it. ").lower()
    if answer == "swim":
        print("You swam and ran into an alligator. You lose.")
    elif answer == "walk":
        answer = input("You walked around and came across a snake. Do you run or climb a tree? ").lower()
        if answer == "run":
            print("The snake caught up with you. You lose.")
        elif answer == "climb":
            answer = input("You climbed and saw a big bird. Do you stay or descend? ").lower()
            if answer == "stay":
                print("The bird found you. You lose. ")
            elif answer == "descend":
                print("The snake finds you. You lose.")
            else:
                print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come across an empty house. Do you enter or pass? ").lower()
    if answer == "enter":
        answer = input("You enter and see a treasure box. Do you open it or ignore? Enter open or ignore. ").lower()
        if answer == "open":
            print("You touch the box and a venomous gas erupts. You lose.")
        elif answer == "ignore":
            answer = input("You see a strange door. Do you go to it or you look around? Enter go or look. ").lower()
            if answer == "go":
                print("You found the magic door. Congratulations, you win!")
            elif answer == "look":
                print("After looking around for a while, strange people enter the house and kidnap you. You lose.")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "pass":
        answer = input("You pass the house and see a sign telling you to go back to the house. "
                       "Do you turn or ignore? ").lower()
        if answer == "turn":
            answer = input("You enter and see a treasure box. Do you open it or ignore? Enter open or ignore. ").lower()
            if answer == "open":
                print("You touch the box and a venomous gas erupts. You lose.")
            elif answer == "ignore":
                answer = input("You see a strange door. Do you go to it or you look around? Enter go or look. ").lower()
                if answer == "go":
                    print("You found the magic door. Congratulations, you win!")
                elif answer == "look":
                    print("After looking around for a while, strange people enter the house and kidnap you. You lose.")
                else:
                    print("Not a valid option. You lose.")
            else:
                print("Not a valid option. You lose.")
        elif answer == "ignore":
            print("After ignoring the sign, you come across miles of bare land and become dehydrated. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name)
