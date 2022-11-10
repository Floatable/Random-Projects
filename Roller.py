# Dice Rolling Simulator
import random
import time
def space(x):
    time.sleep(x)
    print(" \n ")

print(" ")
print("Welcome!")
space(1)

def die_roll(x):
    # print(f"Rolling a D{x}")
    # space(1)
    global roll
    roll = random.randint(1,x)
    # print(f"You rolled a {roll} on a D{x}")
    # space(1)
    return roll

def list(*dice_list):
    print(f"Available dice:")
    for dice in dice_list:
        print(f"- {dice}")

while True:
    list("D4","D6","D8","D12","D20","D100")
    space(1)
    print("""Types of rolls: 
    F or Flat
    D or Disadvantage
    A or Advantage""")
    space(1)

    amount = int(input("Enter number of dice you want to roll: "))
    dice = int(input("What dice do you want to roll (Ex: '6' for D6 etc): "))
    type = input("Enter roll type: ").title()
    bonus = float(input("Enter bonus if any (Ex: +2 or -4): "))

    space(1)
    counter = 0
    while counter < amount:
        counter += 1
        if type == "D" or type == "disadvantage":
            roll1 = die_roll(dice)
            roll2 = die_roll(dice)
            if roll1 <= roll2:
                space(1)
                if bonus >= 0:
                    print(f"A {roll1} was rolled at disadvantage. The total after bonuses is {bonus+roll1}")
                    print(f"The higher roll was a {roll2}")
                if bonus <= 0:
                    print(f"A {roll1} was rolled at disadvantage. The total after bonuses is {bonus-roll1}")
                    print(f"The higher roll was a {roll2}")
            else:
                space(1)
                if bonus >= 0:    
                    print(f"A {roll2} was rolled at disadvantage. The total after bonuses is {bonus+roll2}")
                    print(f"The higher roll was a {roll1}")
                elif bonus <= 0:    
                    print(f"A {roll2} was rolled at disadvantage. The total after bonuses is {bonus-roll2}")
                    print(f"The higher roll was a {roll1}")
                
        elif type == "A" or type == "Advantage" and dice == 20:
            roll1 = die_roll(dice)
            roll2 = die_roll(dice)
            if roll1 >= roll2:
                space(1)
                if bonus >= 0:    
                    print(f"A {roll1} was rolled at advantage. The total after bonuses is {bonus+roll1}")
                    print(f"The lower roll was a {roll2}")
                elif bonus <= 0:    
                    print(f"A {roll1} was rolled at advantage. The total after bonuses is {bonus-roll1}")
                    print(f"The lower roll was a {roll2}")
            else:
                space(1)
                if bonus >= 0:    
                    print(f"A {roll2} was rolled at advantage. The total after bonuses is {bonus+roll2}")
                    print(f"The lower roll was a {roll1}")
                elif bonus <= 0:    
                    print(f"A {roll2} was rolled at advantage. The total after bonuses is {bonus-roll2}")
                    print(f"The lower roll was a {roll1}")
        elif type == "F" or type == "Flat":
            die_roll(dice)
            space(1)
            if bonus >=0:
                print(f"You rolled a {roll} on a D{dice}. After bonuses it becomes a {roll+bonus}")
            elif bonus <= 0:
                print(f"You rolled a {roll} on a D{dice}. After bonuses it becomes a {roll-bonus}")
            
    space(1)

    user_input = (input("Enter Y to role again or N to quit: ")).title()
    if user_input == "N":

        break
