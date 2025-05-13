name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()



if answer == "left":
    answer1 = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()

    if answer1 == "swim":
        print("You swim acros and were eaten by alligator.")
    elif answer1 == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid answer. You lose")

elif answer == "right":
    answer2 = input('You come to a bridge. You want to cross it or head back? (cross/back): ').lower()

    if answer2 == "back":
        print("Fine, you are not as adventurous as expected, you lose.")
    elif answer2 == "cross":
        answer3 = input('You cross the bridge and meet a stranger. Do you talk to them? Yes/No: ').lower()

        if answer3 == "no":
            print("The stranger could have given you important tips to help you move ahead on the path, but you lost the opportunity.")
        elif answer3 == "yes":
            answer4 = input('The stranger says he can either help you cross the jungle or give you some directions and let you go on your own. What do you choose? (help/alone):  ').lower()

            if answer4 == "alone":
                print("Very bad idea, wild animals attacked you and you lose.")
            elif answer4 == "help":
                answer5 = input('After guiding you through the jungle, the stranger takes his leave. You find yourself alone in a quiet valley. Nearby, a box rests on the ground. Do you dare to open it? Yes/No').lower()

                if answer5 == "yes":
                    print("Well done! You found gold, you WIN!.")
                elif answer5 == "no":
                    print("Bad choice, in the box you would have found the gold to win the game, you lose!")
                else:
                    print("Not a valid answer. You lose")
            else:
                print("Not a valid answer. You lose")

        else:
            print("Not a valid answer. You lose")
    else:
        print("Not a valid answer. You lose")

else:
    print("Not a valid answer. You lose")

print()
print('Thank you for trying ', name, 'it was a pleasure to play with you!')