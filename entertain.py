

#Entertaining user
import random
#different arrays
diff_cats=["Sphynx Cat", "Orange Cat", "Maine Coon Cat", "Persian Cat", "Siamese Cat", "American Shorthair Cat", "Egyptian Mau", "Garfield Cat",
           "Calico Cat", "Black Cat", "Burmese Cat", "Munchkin Cat", "Japanese Bobtail Cat", "American Bobtail Cat", "American Curl Cat", "Somali Cat",
           "Australian Mist Cat", "Lykoi Cat"]
location_cat=["Petco", "Cat Shelter", "Petsmart", "Street", "Gifted", "Market Place"]
cat_mood=["Happy Cat", "Sleepy Cat", "Angry Cat", "Silly Cat", "Dangerous Cat", "Playful Cat",
        "Hungry Cat", "Irritated Cat", "Overstimulated Cat", "Understimulated Cat", "Worried Cat",
        "Lazy Cat", "Mischievious Cat", "Chill Cat", "Cozy Cat", "Disturbed Cat", "Loved Cat", "Traumitized Cat",
        "My Cat Ate My Homework Cat"]
activity_points=0
def main_game():
    while True:
        #starting the adopting game
        print("Welcome to Adopt a Cat!" )
        response=input("Would you like to play[yes/no]? ")
        if response=="yes":
                location("place")
                ending=activity()
                if ending=="quit":
                    break
        elif response=="no":
                print("Goodbye!")
                break
        else:
                print("Please type in yes or no")


def location(place):
    #Choosing a place to select a cat from
    print(location_cat)
    try:
        place=input("Where you like to adopt a cat from?: ")
    except:
        print("Something went wrong please try again")
    #Choosing a cat, different places have different cats
    if place=="Petco":
        print(diff_cats[0:3])
        try:
            choosing_cat=input("Please choose a cat! ")
        except:
            print("Something went wrong please try again")
        if choosing_cat in diff_cats[0:3]:
            print("Awesome, You have adopted a " + choosing_cat)

    elif place=="Cat Shelter":
        print(diff_cats[3:6])
        try:
            choosing_cat=input("Please choose a cat! ")
        except:
            print("Something went wrong please try again")
        if choosing_cat in diff_cats[3:6]:
                print("Awesome, You have adopted a " + choosing_cat)
    elif place== "Petsmart":
        print(diff_cats[6:9])
        try:
            choosing_cat=input("Please choose a cat! ")
        except:
            print("Something went wrong please try again")

        if choosing_cat in diff_cats[6:9]:
            print("Awesome, You have adopted a " + choosing_cat)


    elif place== "Street":
        print(diff_cats[9:12])
        try:
            choosing_cat=input("Please choose a cat! ")
        except:
            print("Something went wrong please try again")
        if choosing_cat in diff_cats[9:12]:
            print("Awesome, You have adopted a " + choosing_cat)


    elif place== "Gifted":
        print(diff_cats[12:15])
        try:
            choosing_cat=input("Please choose a cat! ")
        except:
            print("Something went wrong please try again")
        if choosing_cat in diff_cats[15:15]:
            print("Awesome, You have adopted a " + choosing_cat)

    elif place== "Market Place":
        print(diff_cats[15:17])
        try:
            choosing_cat=input("Please choose a cat! ")
        except:
            print("Something went wrong please try again")
        if choosing_cat in diff_cats[15:17]:
            print("Awesome, You have adopted a " + choosing_cat)
    else:
        print("Error occured, please double check spelling")






def activity():
    while True:
                    #Starting a menu for different options user can chose from
        print("Lets starts some activities!")
        print("""
                            1. Feed
                            2. Play
                            3. Check mood
                            4. Quit
                        """)
        try:
            option=int(input("Please enter a number: "))
        except:
            ("Please enter a number")
        if option == 1:
             feed()

        elif option == 2:
            play("options2")
            result=play("options2")
            if result== "quit":
                return "quit"
        elif option == 3:
            mood()

        elif option== 4:
            print("Goodbye")
            return "quit"

        else:
            print("Please make sure type in a number that is displayed")

def closure():
    #describing the bond between your cat
    global activity_points

    if activity_points>=15:
        print("Your cat loves you!")

    elif activity_points<=5:
        print("You should probably bond more with your cat")

    elif activity_points>=6 and activity_points<=14:
        print("You are forming a bond with your cat!")


def feed():
    global activity_points
    options=input("What kind of cat food would you like to feed your cat? [wet,dry,canned,homemade]")
        #feeding the cat different options
        #each option has a different ending
    if options== "wet":
        print("The cat you've chosen HATES wet food. ")
        activity_points=activity_points-1
        print("You just lost 1 point")
        closure()

    elif options== "dry":
        print("The cat you've chosen is eating the dry food happily. ")
        activity_points=activity_points+1
        print("You just gained 1 point!")
        closure()

    elif options== "canned":
        print("The cat you've chosen loved canned food. ")
        activity_points=activity_points+1
        print("You just gained 1 point!!")
        closure()

    elif options== "homemade":
        print("The cat you've chosen HATES your cooking. ")
        activity_points=activity_points-1
        print("You just lost 1 point")
        closure()

    else:
        print("Please make sure to type in a food")


def play(options2):
    global activity_points
    while True:
        options2=input("Would you like to pet your cat [Yes/No]")

        if options2=="Yes":
            print("You pet your cat and they loved it!")
            activity_points=activity_points+1
            print("You just gained a point!")
            closure()
            return
        elif options2=="No":
            outside=input("Would you like to take your cat to the park instead? [Yes/No] ")
            if outside=="Yes":
                print("Your cat is having so much fun")
                activity_points=activity_points+1
                print("You just gained a point!")
                closure()
                leash=input("Would you like to take your cat off their leash?[Yes/No]")

                if leash=="Yes":
                    print("Your cat ran away")
                    print("Game Over!")
                    return "quit"
                    #game ends
                elif leash=="No":
                    print("Your cat is staying by your side and bonding with you!")
                    activity_points=activity_points+1
                    print("You just gained a point!")
                    closure()
                    return
                else:
                    print("Please make sure you type in a displayed response")


            elif outside=="No":
                print("Your cat feels lonely")
                activity_points=activity_points-1
                print("You just lost a point")
                closure()
                toy=input("Would you like to give your cat a mouse toy to play with[Yes/No]")

                if toy=="Yes":
                    print("Your cat is happy playing but it's not with you")
                    activity_points=activity_points-1
                    #activiy_points increases
                    print("You just lost a point")
                    closure()
                    return
                elif toy=="No":
                    print("Your cat feels lonely and decides to run away")
                    print("Game Over!")
                    return "quit"
                    #game ends
                else:
                    print("Please make sure you type in a displayed response")
            else:
                print("Please make sure you type in a displayed response")

        else:
            print("Please make sure you type in a displayed response")


def mood():
    print("Your cat's mood today is: ")
    print(random.choice(cat_mood))
    #printing random mood from array
#Main
main_game()




