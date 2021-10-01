#get name and ask if they would like to hear a story
##The story being is they are given a certain amount of money to start the day, and must make it through witout running out of money.
import random
from my_pkg.midday_module import big_tipper, cartow, catch_Happy_hour, flat_tire, rando_venmo, walk_out
from my_pkg.morning_module import total, Avo_toast, smoothie, burrito, coffee, energy_drink, eat_at_work
from my_pkg.afternoon_module import * 





name = input("Welcome to the Millenial Nightmare. What is your name?")
print("hello", name,",Do you think you have what it takes to make it through the day?")
choice = input("1) yass queen \n2) I literally cannont even")
while True:
    if choice == 2 or choice == "2":
        print("You are so brave for taking care of yourself, get some hot cocoa and watch some netflix, we'll talk later! #selfcare.....Also, you dont really have a choice so here we go!")
        exit
    if choice == 1 or choice == "1":
        print(" Thats the spirit! this is going to be so much fun.")
        break
print("You have", total, "bucks to spend today.")
#a series of comical choices that give or take away money
print("1) yes\n2) no ")
choice_2 = input(" Are you going to get breakfast today?")
#create second if statments here
while True:
    if choice_2 == 1 or choice_2 == "1":
        morning_list = [Avo_toast, smoothie, burrito ]
        random.choice(morning_list)()
        total1 = total
        break
    elif choice_2 == 2 or choice_2== "2":
        morning_list_no = [coffee, energy_drink, eat_at_work]
        random.choice(morning_list_no)()
        total1 = total
        break
    
print("-------------YOU HAVE SURVIVED THE MORNING----------------")
print(input("press enter to continue"))
print("--------------------------------------------------------------------")
print("                 MID-DAY                 ")

print("You have the option of leaving your serving job early: \n 1) Yes 2) No ")
choice_3 = input("Do you want to go?")
while True:
    if choice_3 == 1 or choice_3 == "1":
        afternoon_list = [catch_Happy_hour, flat_tire, rando_venmo]
        random.choice(afternoon_list)()
        total2 = total1
        break
    elif choice_3 == 2 or choice_3 == "2":
        afternoon_list_no = [walk_out, big_tipper, cartow]
        random.choice(afternoon_list_no)()
        total2 = total1
        break


    

# print("You dont have too much at home to cook. Do you make do with what you have?\nOr do you stop and get something to eat on the way home?: \n 1) I'll chance it at home 2) Just pick up something small on the way home ")
# choice_4 = input("Choose one")

#using the random function, offer the user an input choice to be used as a mad libs variable. have the variable inserted into a randomly generated module(library of paragraphs that can be used to create a story)


# give the user the option to continue the story or exit. assign random numbers to add or subtract to the total wallet amount for the day.
