#Christina & Eliana

#functions

import random

pokemon_level=0
pokemon_name=("Abra")
day=1

def main():
    global day
    print("Welcome to Pokemon Evolution!")
    while True:
        print("Choose an activity for Day:  " + str(day))
        print("""
        1.Train
        2.Gym battle
        3.Rest
        4.Quit""")

        activity=int(input("Activity for the day: "))
        if activity == 1:
            Train()
            evolve()
        if activity==2:
            Gym_battle()
            evolve()
        if activity==3:
            rest()

        day=day +1


def Train():
    global pokemon_name
    global pokemon_level
    pushup=input("How many pushups do you want to do?")
    print((pokemon_name)+ " just did " + pushup + " push ups!")
    pokemon_level=pokemon_level+1
    print((pokemon_name)+ "gained 1 level")

def evolve():
    global pokemon_level
    global pokemon_name
    if pokemon_level>=20:
        pokemon_name==Alakazam
    elif pokemon_level<=19:
        pokemon_name==Kadabra
    elif pokemon_level<=9:
        pokemon_name==Abra


def Gym_battle():
    global pokemon_name
    global pokemon_level
    x=random.randint(1,2)
    if int(x)==1:
        print("You lost, Your Pokemon lost a level!")
        pokemon_level=pokemon_level-1
    if int(x)==2:
        print("You Win, Your Pokemon gain 2 levels!")
        pokemon_level=pokemon_level+2

def rest():
    global day
    global pokemon_level
    global pokemon_name
    print(pokemon_name)
    print(pokemon_level)
    print(day)


def Abra():
        print((r"                                                       _\n"))
        print((r"                                                  _, -\"'|\n"))
        print((r"                                              _.-'   ,'j\n"))
        print((r"                      ____           _,.....-'      /  |\n"))
        print((r"                     `.   `'--..,--\"'              .   |\n"))
        print((r"                      `.                           |   |\n"))
        print((r"                       .`.                         \\  j\n"))
        print((r"               _.,     '  .                         ` |\n"))
        print((r"             .','       . |                            \\\n"))
        print((r"           ,\" /         `./                             \\\n"))
        print((r"          /  /           /                    ,-'        \\\n"))
        print((r"        ,'  j           j  .._              ,'            L._\n"))
        print((r"       /    |           |     `.          ,'             ,'  `-.\n"))
        print((r"      .     |           |       `.       .            _,'       `.\n"))
        print((r"      |     |           `.        `               _,-'            \\\n"))
        print((r"      |     `           / `-.                  ,\"/                `.\n"))
        print((r"      |    _.\\         j     `-.._       ,   .' |                  ;\n"))
        print((r"      '  ,'   \\        |        _,'.    '  ,'    `.              .'\n"))
        print((r"       +'   ,.-^.      `-..,..-'/ _,^-----+.       `._       _,-'\n"))
        print((r"       .+--`._   `-._     L_   j-\"          `-.  _,-\\ `..,--'\n"))
        print((r"         \\    `      `\"-+'  `-.'               \"\" ,.'/ ` |      ,\n"))
        print(("_____      L    `       /       `.._.----.._   _.-'  /   F     ,'|\n"))
        print(("`.   `.    |     \\     '.           `\"\"\"-+.-`\"'     '    |`. ,'  |\n"))
        print((r" `.   `.  |      L   _,+\\__              `          \\   |/ /    |\n"))
        print((r"   \\    +,'      |  '     `.`._           `.         |  |.,     |\n"))
        print((r"   `.  '         |,\"        \\  `.          |.      _,|         /\n"))
        print((r"     `           |           |   +.       / | _,-+'  |        /\n"))
        print((r"      \\          |          '    |\\.     /-',\"  /    |       j\n"))
        print((r"       \\         |         /_    | \\`..,-\".\"   |     j       |\n"))
        print((r"        \\         \\ _   _,'  `-.  `-,|/___.\\,-.|    /        '\n"))
        print((r"        `         `' \"\"\"        `\"\"'            \\  |        .\n"))
        print((r"         `. ,\"\"'   |                             `-+`./     |\n"))
        print((r"           `.     '                                  |      F\n"))
        print((r"             )   |                                    \\    /\n"))
        print((r"            /__,.'                                     \\,.' mh\n"))


def Kadabra():
        print((r"                      .-\n"))
        print((r"                      | \\               _,\n"))
        print((r"                     j   \\           ,-' |\n"))
        print((r"                     |    \\       ,''   .'\n"))
        print((r"                     |     \\    ,'   .  |\n"))
        print((r"        .-`.        .|    __\\_,'    ,  ,\n"))
        print((r"      ,'   |        ||  \"\"        .'  /\n"))
        print((r"     .     +.      ,\"'           .   /   ___\n"))
        print((r"   ,-.\\ _,`.'     ,  __._        `. ,  ,'   |\n"))
        print((r"   .  `'   /     /  <   ,'    _    \\`.'     `-,._\n"))
        print((r",\\_|`.,-`.'     /`. `-^-'  _.|    .-\"||     .'   `-.\n"))
        print(("` `. //`.`      j \\`.     ,'|)|   ,\\  |`.    |  ,.--'\n"))
        print((r"`. `'`//       |  `|   .:,-'     |`.'   `.___`\" '\n"))
        print((r" `.|>,'\\       |`..|  /     ____.' |    `-. >    \\,_..._\n"))
        print((r" // `   \\     ,',-'| /  \"'-\".  ` `.`.    ,-\"\"\\  ,'      `\".\n"))
        print((r"(/   :  `-._,/ /,'`./  '\"-._ `. `. ``--..\\_,-' ,'          \\\n"))
        print((r"     '.    .',' /'|     /|  `. `. ._.__ _,'.\"|'             \\\n"))
        print((r"       .   `,' /  |  ` /-'    \\  `. ` -..-'  |\"`.            '\n"))
        print((r"        `--'/ /    `+-'        \\  ``.       .    `.          `\n"))
        print((r"           ' .       `-.  ,-\"--.+  \\ .    .' `.    `    .   | \\\n"))
        print((r"          '| |          `.\\,\" ,. ` ' '_.-'     \\    \\   |   ' |\n"))
        print((r"          |' |    __,.-\"' .| '|`. . \\`.   \\     \\    .  | ,'  |\n"))
        print((r"          || |  ,'\\        .`. V  | |     |      .   |  '   /.'\n"))
        print((r"          `| | /   `._     `. _|  | ||    |      |   | /..-' /   .\n"))
        print((r"           ' . '      /`---'.`.`._| '|,--.|      |   |'     /    '|\n"))
        print((r"            . . \\    ,'      ` \\/ '/ `    `._    '  ,'     |   ,' |\n"))
        print((r"             `.\\ `.  \\        `. .'   |      `.,' ,'|      '+-'   '\n"))
        print((r"           _.--`.-j   `-.-..    `-.   `-.     | ,/  `.       `  .'\n"))
        print((r"         .'_.'+\"\"' _   _,.'-`      `-..._,\\   |-'     `-...__..'\n"))
        print((r"         ' /_..|/-' `\"'                ,_.`'   `..__\n"))
        print((r"                                         `.  `-._  ,-'\n"))
        print((r"                                          `,..`. `/  |\n"))
        print((r"                                           :  /    `.'\n"))
        print((r"                                            `.' mh\n"))

def Alakazam():
        print((r"                                              _,'|\n"))
        print((r"                                            .'  /\n"))
        print((r"                   __                     ,'   '\n"))
        print((r"                  `  `.                 .'    '\n"))
        print((r"                   \\   `.             ,'     '\n"))
        print((r"                    \\    `.          ,      /\n"))
        print((r"                     .     `.       /      ,\n"))
        print((r"                     '       ..__../'     /\n"))
        print((r"                      \\     ,\"'   '      . _.._\n"))
        print((r"                       \\  ,'             |'    `\"._\n"))
        print((r"                        |/               ,---.._   `.\n"))
        print((r"                      ,-|           .   '       `-.  \\\n"))
        print((r"                    ,'  |     ,   ,'   :           '__\\_\n"))
        print((r"                    |  /,_   /  ,U|    '            |   .__\n"))
        print((r"                    `,' `.\\ `./..-'  __ \\           |   `. `.\n"))
        print((r"                      `\",_|  /     ,\"  `.`._       .|     \\ |\n"))
        print((r"                     / /_.| j  ---'.     `._`-----`.`     | |\n"))
        print((r"                    / // ,|`'  `-/' `.      `\"/-+--'    ,'  `.\n"))
        print((r"                _,.`,'| / |.'  -,' \\  \\       \\ '._    /     |\n"))
        print((r".--.      _,.-\"'   `| L \\ \\__ ,^.__.\\  `.  _,--`._,>+-'  __,-'\n"))
        print((":    \\   ,'          |  | \\          /.   `'      '.  `--'| \\\n"))
        print(("'    | ,-.. `'   _,--' ,'  \\        `.\\            7      |,.\\\n"))
        print((r"`._ '.  .`.    .>  `-.-    |-.\"\"---..-\\        _>`       `.-'\n"))
        print((r"   `.,' | l  ,' ,>         | `.___,....\\._    ,--``-.\n"))
        print((r"  j | .'|_|.'  /_         /   _|         \\`\"--+--.   ` ,..._\n"))
        print((r"  |_`-'/  |     ,' ,.._,.'\"\"\"'\\           `--'    `-..'     `\".\n"))
        print((r"    \"-'_,+'\\    '^-     |      \\                    /         |\n"))
        print((r"         |_/         __ \\       .                   `.`.._  ,'`.\n"))
        print((r"                 _.:'__`'        `,.                  |   `'   |\n"))
        print((r"                `--`-..`\"        /--`               ,-`        |\n"))
        print((r"                  `---'---------'                   \"\"| `#     '.\n"))
        print((r"                                                      `._,       `:._\n"))
        print((r"                                                        `|   ,..  |  '.\n"))
        print((r"                                                        j   '.  `-+---'\n"))
        print((r"                                                        |,.. |\n"))
        print((r"                                                         `. `;\n"))
        print((r"                                                           `' mh\n"))


#main

main()
