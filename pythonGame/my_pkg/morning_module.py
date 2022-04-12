

                                ###Morning list yes#####
def Avo_toast(self, total):
    Avo_toast_cost = 25
    
    self.total -= Avo_toast_cost
    print(f"Nothing like a little breakfast to start your morning, but the trendy restaurant doesn't take apple pay and you have to pay for Trent's avocado toast. -${Avo_toast_cost} \n You now have {total} dollars.")
    
def smoothie():
    smoothie_cost = 10
    
    total -= smoothie_cost
    print(f"Gotta love something that costs more than an egg sandwhich and costs twice as much. Plus the Matcha powder really helps to add insult to injury, because now you need water to wash your smoothie down! thats gonna cost you {smoothie_cost} bucks.\n You are at {total} dollars")
##remember that all of your variable values need to be a single integer, The addition and subtraction comes with the 3rd line on each function.
def burrito():
    burrito_cost = 7
   
    total += burrito_cost
    print(f"You snag a burrito on your way about your day, as an added bonus, you are going to be so full that you are wont need lunch, saving you from having to buy it. You technically came up on {burrito_cost} dollars this morning.\nYou now have {total} dollars")



###Morning list no #######
                        
def coffee():
    coffee = 5
   
    total -= coffee
    print(
    f"Keeping it light this morning, I like it. Plus we woke up too late to eat breakfast. Only ${coffee} bucks this morning.\n you are at {total}  dollars")
    
def energy_drink():
    redbull = 3
  
    total -= redbull
    print(f"Nothing like a legal amphetamine to not make you hungry and give you energy.${redbull} bucks. Whats a few years off of your life?\n You now have {total} bucks")

def eat_at_work():
   
    print(f"Thats a good call, You can eat at work. Eating a big 'ole slice of poverty costs nothing\n You now have {total} ")

    
# need to look at how to make a cross module variable. Need to ask about scope in python
