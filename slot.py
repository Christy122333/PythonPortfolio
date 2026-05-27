#Christina Y and Eliana C

import random
global money
#functions
credit=0
def game():
    global credit
    while True:
        print("""
=====Welcome to the Lucky-Ducky Machine=====


                """)
        print("Slot Machine Symbols: ♈ ♌ ♎ 7")

        symbols=["♈", "♌","♎", "7"]
        spin=input("Would you like to spin Yes/No OR load credits """)


        if spin=="load":
            spending=int(input("How much credit would you like to spend? "))
            credit=credit+spending
        if credit<=0:
            print(credit)
            break


        elif spin=="Yes":
                sign1=random.choice(symbols)
                print(sign1)
                sign2=random.choice(symbols)
                print(sign2)
                sign3=random.choice(symbols)
                print(sign3)
                if symbols=="♈" and symbols=="♈" and symbols=="♈":
                    print("Jackpot!")
                    credit=credit+100
                    print("Money left: ")
                    print(credit)
                    continue
                elif symbols=="♌" and symbols=="♌" and symbols=="♌":
                    print("Jackpot!")
                    credit=credit+100
                    print("Money left: ")
                    print(credit)
                    continue
                elif symbols=="♎" and symbols=="♎" and symbols=="♎":
                    print("Jackpot!")
                    credit=credit+100
                    print("Money left: ")
                    print(credit)
                    continue
                elif symbols=="7" and symbols=="7" and symbols=="7":
                    print("Jackpot!")
                    credit=credit+100
                    print("Money left: ")
                    print(credit)
                    continue

                else:
                    print("You lose:(")
                    credit=credit-150
                    print("Money left: ")
                    print(credit)
                    if credit<=0:
                        print("You ran out of money! ")
                        print("Money left: ")
                        print(credit)
                        break
                    else:
                        continue

        elif spin=="No":
            print("Goodbye!")
            print(credit)
            break

def streak():
    global money
    losses=0
    wins=0

    for i in range(1000):
        end=game()
        if end=="Jackpot!":
            wins=wins+1
        if end=="You lose:(":
            losses=losses-1


#main
streak()
