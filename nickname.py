#Christina

def nickname():
    print("Find out what Avenger you are!" )
    category=input("Are you more of a leader or follower?""(leader,follower)")
    if category=="leader":
        work=input("Would you rather be your own boss or work for something bigger than you?""(boss,bigger)")
        if work==("boss"):
            humor=input("Are you more sarcastic or more serious""(sarcastic, serious)")
            if humor=="sarcastic":
                print("You are Ironman!, sarcastic and a hero!")
            else:
                print("You are Black Panther!, RIP")
        else:
            job=input("Would you rather be a spy or a warrior?""(warrior,spy)")
            if job=="warrior":
                print("You are Captain America, America's sweatheart!")
            else:
                print("You are Black Widow!, woah you must be fearless")
    else:
        power=input("Would rather have super strength or agility?""(agility,strength)")
        if power=="strength":
            humor=input("Would you want to be a God or a world reowned ""(scientist,God)")
            if humor=="scientist":
                print("You are Hulk, you are one strong person lol!")
            else:
                print("Thor!, We miss Loki too")

        else:
            age=input("Would you be a teenager and be in your youth or be an independent adult""(adult,youth)")
            if age=="youth":
                print("You are Spiderman, wait who are you again")
            else:
                print("You are Hawkeye, we miss Natasha too")

#main
nickname()


