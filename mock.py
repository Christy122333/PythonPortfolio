#Christina Y

import pandas as pd
#The purpose of this program is to help users find a dog that fits their needs.
data=pd.read_csv("dogs.csv")

#Init
#Functions
#Main
id=data["id"].tolist()
dog_names=data["Name"].tolist()
breed=data["Breed Group"].tolist()
dog_specialty=data["BredFor"].tolist()
life_min=data["Minimum Life Span"].tolist()
life_max=data["Maximum Life Span"].tolist()
height_min=data["Minimum Height"].tolist()
height_max=data["Maximum Height"].tolist()
weight_min=data["Minimum Weight"].tolist()
weight_max=data["Maximum Weight"].tolist()
mood=data["Temperament"].tolist
image=data["Image"].tolist

suggested_dogs=[]


def size(dogsize):


    if asking_size =="Tiny":
        for i in range(len(id)):
            if weight_max[i]<=12:
                suggested_dogs.append(dog_names[i])
        print(suggested_dogs)
        suggested_dogs.clear()

    if asking_size =="Small":
        for i in range(len(id)):
            if weight_max[i]>12 and weight_max[i]>=22 :
                suggested_dogs.append(dog_names[i])
        print(suggested_dogs)
        suggested_dogs.clear()

    if asking_size== "Medium":
        for i in range(len(id)):
            if weight_max[i]>22 and weight_max[i]<=57:
                suggested_dogs.append(dog_names[i])
        print(suggested_dogs)
        suggested_dogs.clear()

    if asking_size== "Big":
        for i in range(len(id)):
            if weight_max[i]>57 and weight_max[i]<=99:
                suggested_dogs.append(dog_names[i])
        print(suggested_dogs)
        suggested_dogs.clear()

    if asking_size== "Giant":
        for i in range(len(id)):
            if weight_max[i]>=100:
                suggested_dogs.append(dog_names[i])
        print(suggested_dogs)
        suggested_dogs.clear()

def dog_appearance():
    type=input("What dog breed would you like to see? ")
    for i in range(len(dog_names)):
        if breed[i]==type:
            suggested_dogs.append(image[i])
    print(suggested_dogs)
    suggested_dogs.clear()

def specialty(purpose):
    for i in range(len(dog_names)):
        if dog_names[i]==purpose:
            suggested_dogs.append(dog_specialty[i])
    print(suggested_dogs)
    suggested_dogs.clear()

def personality(names):
    ask=input("Would you like to know the temperaments of the dogs?, if yes please enter a dog name! ")
    for i in range(len(dog_names)):
        if ask==names:
            suggested_dogs.append(mood[i])
    print(suggested_dogs)
    suggested_dogs.clear()

def menu():
    while True:
        print("Welcome to finding a dog!")
        size()
        play=input("Would you like to continue? Yes or No: ")
        if play=="Yes":
            print("Okay")
            dog_appearance()
        play=input("Would you like to continue? Yes or No: ")
        if play=="Yes":
            print("Okay")
            specialty()
        play=input("Would you like to continue? Yes or No: ")
        if play=="Yes":
            print("Okay")
            personality("German Shepard")
        if play=="Yes":
            print("Okay")
            continue
        elif play=="No":
            print("Goodbye!")
            break



#Main
menu()

asking_size=input("What type of dog size would you prefer?(Tiny, Small, Medium, Big, Giant): ")
size(asking_size)


#Sources of Information
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

