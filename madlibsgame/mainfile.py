import random
from my_pkg.Sciencefiction import ScienceStory, ScienceStory2, ScienceStory3

print("Welcome to the big game of madlibs")
name = input("What is your name?    ")
print(f"Welcome {name}! lets create a story!")
name2 = input("Please create another random name: ")
name3 = input("And give me one more name:  ")

print("              -----LETS BEGIN-----           ")
input("Press enter to continue")
print("Choose a story!")
choice = input("1)Science fiction \n2)Western \n3)Spanish Romance  ")

while True:  # when completed, this if statement will direct user choice to a corresponding module with the genre of story
    if choice == 1 or "1":
        sciencestorychoices = [ScienceStory, ScienceStory2, ScienceStory3]
        random.choice(sciencestorychoices)(name, name2, name3)
        break
