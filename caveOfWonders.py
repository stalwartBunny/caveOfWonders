#Text-based dungeon crawler
from sys import exit
import random

pcHP = 6
pcHPmax = 6
lightAttack = 2
heavyAttack = 4
locationX = 1
locationY = 1
silverBulletCounter = 0
insightCounter = 0
startRoomCounter = 0






class Mon:

    name = "Rabid Dog"
    HP = 4
    attack1 = "Bite"
    attack1Dmg = 1
    attack2 = "Chomp Chomp Chomp"
    attack2Dmg = 3
    loot = "Generic Loot"

    def __init__(self, name, HP, attack1, attack1Dmg, attack2, attack2Dmg, loot):
        self.name = name
        self.HP = HP
        self.attack1 = attack1
        self.attack1Dmg = attack1Dmg
        self.attack2 = attack2
        self.attack1Dmg = attack2Dmg
        self.loot = loot

    def func(self):
        print("After calling the func method...")
        print(f"{self.name}'s HP is {self.HP}, {self.attack1} deals {self.attack1Dmg}, {self.attack2} deals {attack2Dmg} and holds {loot}.")
        print("....function end....")

    #putridBeast = Mon("Putrid Beast", 4, "Swipe", 1, "Lunge", 2)
    #putridBeast.func()
    #print(putridBeast.HP)
def combat():
    global pcHP
    global lightAttack
    global heavyAttack
    global locationX
    global locationY
    global pcHPmax
    global silverBulletCounter
    global insightCounter
    global startRoomCounter

    seed = random.randint(1,10) #used on the monster list to pick a mon
    pcHP = pcHP #work to do, make it recognize and pull pcHP from global variable
    lightAttack = lightAttack #work to do, make it recognize and pull pcHP from public variable
    heavyAttack = heavyAttack #work to do, make it recognize and pull pcHP from public variable

    print(f"Monster Seed value is: {seed}") #generates a mon based on this seed

    if seed == 1:
        monster = Mon("Putrid Beast", 4, "Swipe", 1, "Lunge", 2, "two blood vials")
    elif seed == 2:
        monster = Mon("Rabid Dog", 2, "Bite", 1, "Chomp Chomp Chomp", 3, "a blood vial")
    elif seed == 3:
        monster = Mon("Church Servant", 7, "Cane Strike", 2, "Arcade Missile", 4, "silver bullets")
    elif seed == 4:
        monster = Mon("Church Giant", 9, "Towering Slash", 4, "Stomp Stomp", 3, "huge blood echoes")
    elif seed == 5:
        monster = Mon("Lab Rat", 3, "Nibble", 1, "Swarm", 3, "a blood vial")
    elif seed == 6:
        monster = Mon("Mad One", 6, "Sickle Slash", 3, "Overhead Cleave", 5, "insight")
    elif seed == 7:
        monster = Mon("Maneater Boar", 8, "Ggreeeeeee!", 6, "*Snort Snort*", 0, "huge blood echoes")
    elif seed == 8:
        monster = Mon("Gravekeeper Scorpion", 5, "Poisoned Pincers", 2, "Swarm", 4, "two blood vials")
    elif seed == 9:
        monster = Mon("Keeper of the Old Lords", 6, "Sword Slash", 2, "Flame Spray", 5, "insight and echoes!")
    elif seed == 10:
        monster = Mon("Hunter Mob", 7, "Axe Swing", 3, "Rifle Shot", 4, "silver bullets")

    #print(f"testing monster object: {monster}")
    print(f"You look around for loot only to find a {monster.name}!")
    print(f"{monster.HP}:Mon HP, {pcHP}: Player HP, {lightAttack}: Light attack damage, {heavyAttack}: Heavy attack damage")


    while monster.HP > 0 and pcHP > 0:  #as long as monster's HP and playerHP is above 0
        #print("Mon HP loop")
        print(f"Player HP: {pcHP}, Monster HP: {monster.HP}")
        randomRoll = random.randint(1, 9) #used to determine a miss from the enemy
        seed2 = random.randint(1,11) #used to determine monster's attack choice
        print(f"The {monster.name} is readying to attack, what do you do?") #prompt players for move
        combatChoice = input("Light attack, heavy attack, dodge, or escape >>>")
        if combatChoice == "quit" or choice == "Quit":
            quit()
        if randomRoll % 3 != 0: #enemies have a 2/3 hit rate
            if combatChoice == "light attack" or combatChoice == "Light Attack" or combatChoice == "Light attack" or combatChoice == "light Attack":
                if seed2 % 2 != 0: #enemies have a slight preference for light attacks
                    monster.HP = monster.HP - lightAttack
                    if monster.HP >=1:
                        pcHP = pcHP - monster.attack1Dmg #monster loses HP first during lightAttack, then player light damage
                        print(f"You exchange blows. The enemy used {monster.attack1}!")
                    else:
                        print(f"You killed him before he could respond. Your HP is at {pcHP}.")
                elif seed2 % 2 == 0:
                    monster.HP = monster.HP - lightAttack
                    if monster.HP >=1:
                        pcHP = pcHP - monster.attack2Dmg #monster loses HP first during lightAttack, then player recieves heavy damage
                        print(f"You exchange blows. The enemy used {monster.attack2}!")
                    else:
                        print(f"You killed him before he could respond. Your HP is at {pcHP}.")
            elif combatChoice == "heavy attack" or combatChoice == "Heavy Attack" or combatChoice == "Heavy attack" or combatChoice == "heavy Attack":
                if seed2 % 2 == 0:
                    print(f"You exchange blows. The enemy used {monster.attack1}!")
                    pcHP = pcHP - monster.attack1Dmg #during Heavy attacks monster deals dmg first but player heals a little at the end (if alive)
                    monster.HP = monster.HP - heavyAttack
                    if pcHP < pcHPmax:
                        pcHP = pcHP + 1 #the player WILL get this HP back in time not to die if their health was sitting at 0 prior
                elif seed2 % 2 != 0:
                    print(f"You exchange blows. The enemy used {monster.attack2}!")
                    pcHP = pcHP - monster.attack2Dmg
                    monster.HP = monster.HP - heavyAttack
                    if pcHP < pcHPmax:
                        pcHP = pcHP + 1
            elif combatChoice == "Dodge" or combatChoice == "dodge":
                if randomRoll % 2 == 0: #succes for a dodge
                    print(f"The blow missed!. You retaliate for light damage!")
                    monster.HP = monster.HP - lightAttack
                else:
                    if seed2 % 2 != 0: #fail on dodge
                        print(f"You try to dodge and take half damage from {monster.attack1}.")
                        if monster.attack1Dmg % 2 == 0:
                            pcHP = pcHP - (monster.attack1Dmg / 2)
                        else:
                            pcHP = pcHP - ((monster.attack1Dmg - 1) / 2)
                    else:
                        print(f"You try to dodge and take half damage from {monster.attack2}.")
                        if monster.attack2Dmg % 2 == 0:
                            pcHP = pcHP - (monster.attack2Dmg / 2)
                        else:
                            pcHP = pcHP - ((monster.attack2Dmg - 1) / 2)
            elif combatChoice == "escape" or combatChoice == "Escape": #leave combat, always works
                print("You flee the way you came!")
                pcMove(locationX, locationY)
            else:
                print("Invalid input, try again.")
        else: #this is for those 1/3 enemy misses aka randomRoll IS divisible by 3
            if combatChoice == "heavy attack" or combatChoice == "Heavy Attack" or combatChoice == "Heavy attack" or combatChoice == "heavy Attack":
                print("Your blow lands and their's misses!")
                monster.HP = monster.HP - heavyAttack
                if pcHP < pcHPmax:
                    pcHP = pcHP + 1
            elif combatChoice == "light attack" or combatChoice == "Light Attack" or combatChoice == "Light attack" or combatChoice == "light Attack":
                print("Your blow lands and their's misses!")
                monster.HP = monster.HP - lightAttack
            elif combatChoice == "dodge" or combatChoice == "Dodge":
                print("The enemy missed their attack and you retaliate for light damage.")
                monster.HP = monster.HP - lightAttack
    if pcHP <= 0: #player character runs out of HP
        print("Oh no! You died! That's the way the cookie crumbles.")
        exit(0)

    if monster.HP <= 0: #monster runs out of HP
        print("You defeated the monster! Good for you! You take the loot and run.")

        if monster.loot is "a blood vial": #this list details the effects of various loot drops
            print("You use a stray blood vial to patch up.")
            if pcHP + 2 <= pcHPmax:
                pcHP = pcHP + 2
            else: pcHP = pcHPmax
        elif monster.loot is "two blood vials":
            print("You find two bloodvials but have nowhere to put them. You patch yourself up and leave the rest.")
            if pcHP + 4 <= pcHPmax:
                pcHP = pcHP + 4
            else: pcHP = pcHPmax
        elif monster.loot is "silver bullets":
            silverBulletCounter = silverBulletCounter + 1
            print("You pick up some silver bullets, maybe these will help fend off predators.")
            if silverBulletCounter >= 2:
                lightAttack = lightAttack + 1
                print("Your light attack damage has increased by 1.")
        elif monster.loot is "huge blood echoes":
            heavyAttack = heavyAttack + 2
            lightAttack = lightAttack + 1
            pcHPmax = pcHPmax + 1
            pcHP = pcHP + 1
            print("You get massive blood echoes. Your attacks all feel stronger.")
        elif monster.loot is "insight":
            insightCounter = insightCounter + 1
            if insightCounter > 1:
                print("You now have enough insight to go beyond the stairwell fogwall.")
            else:
                print("You gained some insight, a little more and you can pass the fogwall.")
        elif monster.loot is "insight and echoes!":
            insightCounter = insightCounter + 1
            lightAttack = lightAttack + 1
            heavyAttack = heavyAttack + 2
            pcHPmax = pcHPmax + 1
            pcHP = pcHP + 1
            print("This much insight gets you passed the stairwell fogwall and the echoes make your attacks stronger!")
        print(f"Your current health is {pcHP}.")

def pcMove(locationX, locationY):
    if locationX is 3:
        if locationY is 0:
            startRoom()
        elif locationY is 5:
            room35()
        elif locationY is 6:
            room36()
        elif locationY is 7:
            room37()
    elif locationX is 2:
        if locationY is 1:
            room21()
        elif locationY is 3:
            room23()
        elif locationY is 5:
            room25()
        elif locationY is 6:
            room26()
    elif locationX is 1:
        if locationY is 2:
            room12()
        elif locationY is 4:
            room14()
    elif locationX is 4:
        if locationY is 1:
            room41()
        elif locationY is 3:
            room43()
        elif locationY is 5:
            room45()
        elif locationY is 6:
            room46()
    elif locationX is 5:
        if locationY is 2:
            room52()
        elif locationY is 4:
            room54()
    else:
        print("You seem to have fallen off the map somehow. Let's go back to the beginning.")
        startRoom()

def bossFight():
    global pcHP
    global lightAttack
    global heavyAttack
    global locationX
    global locationY
    global pcHPmax
    global silverBulletCounter
    global insightCounter
    global startRoomCounter

    pcHP = pcHP #work to do, make it recognize and pull pcHP from global variable
    lightAttack = lightAttack #work to do, make it recognize and pull pcHP from public variable
    heavyAttack = heavyAttack #work to do, make it recognize and pull pcHP from public variable

    monster = Mon("Cleric Beast", 25, "Massive Swipe", 4, "Unholy Smash", 5, "some loot")

    #print(f"testing monster object: {monster}")
    print(f"The Beast begins its rampage!")
    print(f"{monster.HP}:Mon HP, {pcHP}: Player HP, {lightAttack}: Light attack damage, {heavyAttack}: Heavy attack damage")


    while monster.HP > 0 and pcHP > 0:  #as long as monster's HP and playerHP is above 0
        #print("Mon HP loop")
        print(f"Player HP: {pcHP}, Monster HP: {monster.HP}")
        randomRoll = random.randint(1, 9) #used to determine a miss from the enemy
        seed2 = random.randint(1,11) #used to determine monster's attack choice
        print(f"The {monster.name} is readying to attack, what do you do?") #prompt players for move
        combatChoice = input("Light attack, heavy attack, dodge, or escape >>>")
        if randomRoll % 3 != 0: #enemies have a 2/3 hit rate
            if combatChoice == "light attack" or combatChoice == "Light Attack" or combatChoice == "Light attack" or combatChoice == "light Attack":
                if seed2 % 2 != 0: #enemies have a slight preference for light attacks
                    monster.HP = monster.HP - lightAttack
                    if monster.HP >=1:
                        pcHP = pcHP - monster.attack1Dmg #monster loses HP first during lightAttack, then player light damage
                        print(f"You exchange blows. The enemy used {monster.attack1}!")
                    else:
                        print(f"You killed him before he could respond. Your HP is at {pcHP}.")
                elif seed2 % 2 == 0:
                    monster.HP = monster.HP - lightAttack
                    if monster.HP >=1:
                        pcHP = pcHP - monster.attack2Dmg #monster loses HP first during lightAttack, then player recieves heavy damage
                        print(f"You exchange blows. The enemy used {monster.attack2}!")
                    else:
                        print(f"You killed him before he could respond. Your HP is at {pcHP}.")
            elif combatChoice == "heavy attack" or combatChoice == "Heavy Attack" or combatChoice == "Heavy attack" or combatChoice == "heavy Attack":
                if seed2 % 2 == 0:
                    print(f"You exchange blows. The enemy used {monster.attack1}!")
                    pcHP = pcHP - monster.attack1Dmg #during Heavy attacks monster deals dmg first but player heals a little at the end (if alive)
                    monster.HP = monster.HP - heavyAttack
                    if pcHP < pcHPmax:
                        pcHP = pcHP + 1 #the player WILL get this HP back in time not to die if their health was sitting at 0 prior
                elif seed2 % 2 != 0:
                    print(f"You exchange blows. The enemy used {monster.attack2}!")
                    pcHP = pcHP - monster.attack2Dmg
                    monster.HP = monster.HP - heavyAttack
                    if pcHP < pcHPmax:
                        pcHP = pcHP + 1
            elif combatChoice == "Dodge" or combatChoice == "dodge":
                if randomRoll % 2 == 0: #succes for a dodge
                    print(f"The blow missed!. You retaliate for light damage!")
                    monster.HP = monster.HP - lightAttack
                else:
                    if seed2 % 2 != 0: #fail on dodge
                        print(f"You try to dodge and take half damage from {monster.attack1}.")
                        if monster.attack1Dmg % 2 == 0:
                            pcHP = pcHP - (monster.attack1Dmg / 2)
                        else:
                            pcHP = pcHP - ((monster.attack1Dmg - 1) / 2)
                    else:
                        print(f"You try to dodge and take half damage from {monster.attack2}.")
                        if monster.attack2Dmg % 2 == 0:
                            pcHP = pcHP - (monster.attack2Dmg / 2)
                        else:
                            pcHP = pcHP - ((monster.attack2Dmg - 1) / 2)
            elif combatChoice == "escape" or combatChoice == "Escape": #leave combat, always works
                print("You flee the way you came!")
                pcMove(locationX, locationY)
            else:
                print("Invalid input, try again.")
        else: #this is for those 1/3 enemy misses aka randomRoll IS divisible by 3
            if combatChoice == "heavy attack" or combatChoice == "Heavy Attack" or combatChoice == "Heavy attack" or combatChoice == "heavy Attack":
                print("Your blow lands and their's misses!")
                monster.HP = monster.HP - heavyAttack
                if pcHP < pcHPmax:
                    pcHP = pcHP + 1
            elif combatChoice == "light attack" or combatChoice == "Light Attack" or combatChoice == "Light attack" or combatChoice == "light Attack":
                print("Your blow lands and their's misses!")
                monster.HP = monster.HP - lightAttack
            elif combatChoice == "dodge" or combatChoice == "Dodge":
                print("The enemy missed their attack and you retaliate for light damage.")
                monster.HP = monster.HP - lightAttack
    if pcHP <= 0: #player character runs out of HP
        print("Oh no! You died! That's the way the cookie crumbles.")
        exit(0)

    if monster.HP <= 0: #monster runs out of HP
        print("Beast Slain! You are victorious!")



def startRoom():
    global locationX
    global locationY
    global startRoomCounter

    if startRoomCounter == 0:
        name = input("Please enter your name: ")
        print("Welcome to the Cave of Wonders. It's a wonder it exists at all!")
        print(f"We thank you, {name}, for coming here today. \n I'm sure inside you'll find your deepest desires.")
        locationX = 3
        locationY = 0
        choice = input("There is a door to your left and a door to your right. Which do you take?  >>>")
        if choice == "left" or choice == "Left":
            locationX = locationX - 1
            locationY = locationY + 1
    #        return locationX, locationY
        elif choice == "right" or choice == "Right":
            locationX = locationX + 1
            locationY = locationY + 1
    #        return locationX, locationY
        else:
            print("You chose neither, turned around, and walked out on this entire excercise.")
            exit(0)
        startRoomCounter = startRoomCounter + 1
        pcMove(locationX, locationY)

    else:
        choice = input("You're back at the start! There is a door to your left and a door to your right. Which do you take?  >>>")
        if choice == "left" or choice == "Left":
            locationX = locationX - 1
            locationY = locationY + 1
    #        return locationX, locationY
        elif choice == "right" or choice == "Right":
            locationX = locationX + 1
            locationY = locationY + 1
    #        return locationX, locationY
        else:
            print("You chose neither, turned around, and walked out on this entire excercise.")
            exit(0)
        pcMove(locationX, locationY)

def room21():
    print("Welcome to room 21. You walked through a door, amazing. It has a north and west exit.")
    locationX = 2
    locationY = 1
    choice = input("Choose either forward or left: >>>")
    if choice == "Left" or choice == "left":
        locationX = locationX - 1
        locationY = locationY + 1
    elif choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You mumble to yourself incoherently and try that again...")

    pcMove(locationX, locationY)

def room41():
    print("Holy cows, you went right through a door and ended up in room 41. Astonishing. It has a north and east exit. ")
    locationX = 4
    locationY = 1
    choice = input("There is a door forward and a door right, choose one:  >>>")
    if choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    elif choice == "right" or choice == "Right":
        locationX = locationX + 1
        locationY = locationY + 1
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You mumble to yourself incoherently and try that again...")

    pcMove(locationX, locationY)

def room12():
    print("Welcome to room 12. It's a dead end, so you want to return the way you came with your loot but something is wrong...")
    print(" ")
    combat()
    print(" ")
    locationX = 2
    locationY = 1
    pcMove(locationX, locationY)

def room52():
    print("Welcome to room 52. It's a dead end, so you want to return the way you came with your loot but something is wrong...")
    print(" ")
    combat()
    print(" ")
    locationX = 4
    locationY = 1
    pcMove(locationX, locationY)

def room23():
    print("Room 23 welcomes you. It exits to a hallway that breaks into three directions (all four, counting the way you came.)")
    locationX = 2
    locationY = 3
    choice = input("Left, right, forward, or back; which do you take?  >>>")
    if choice == "left" or choice == "Left":
        locationX = locationX - 1
        locationY = locationY + 1
    elif choice == "right" or choice == "Right":
        locationX = locationX + 2
    elif choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    elif choice == "back" or choice == "Back":
        locationY = locationY - 2
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You mumble to yourself incoherently and try that again...")

    pcMove(locationX, locationY)

def room43():
    print("Room 43 welcomes you. It exits to a hallway that breaks into three directions (all four, counting the way you came.)")
    locationX = 4
    locationY = 3
    choice = input("Left, right, forward, or back; which do you take? >>>")
    if choice == "left" or choice == "Left":
        locationX = locationX - 2
        locationY = locationY + 0
    elif choice == "right" or choice == "Right":
        locationX = locationX + 1
        locationY = locationY + 1
    elif choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    elif choice == "back" or choice == "Back":
        locationY = locationY - 2
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You mumble to yourself incoherently and try that again...")

    pcMove(locationX, locationY)


def room14():
    print("Room 14 is a dead end, so you want to return the way you came with your loot but something is wrong...")
    print(" ")
    combat()
    print(" ")
    locationX = 2
    locationY = 3
    pcMove(locationX, locationY)

def room54():
    print("Room 54 is a dead end, so you want to return the way you came with your loot but something is wrong...")
    print(" ")
    combat()
    print(" ")
    locationX = 4
    locationY = 3

    pcMove(locationX, locationY)

def room25():
    print("Room 25 has one exit northward. You go through it.")
    print(" ")
    locationX = 2
    locationY = 6

    pcMove(locationX, locationY)

def room45():
    print("Room 45 has one exit northward. You go through it.")
    print(" ")
    locationX = 4
    locationY = 6

    pcMove(locationX, locationY)

def room26():
    print("Room 26 leads to one room forward that looks peaceful and one spiral stairwell that leads to the tallest tower.")
    locationX = 2
    locationY = 6
    choice = input("Forward or Stairwell?? >>>")
    if choice == "forward" or choice == "Forward":
        locationX = locationX + 1
        locationY = locationY + 1
    elif choice == "stairwell" or choice == "Stairwell":
        locationX = locationX + 1
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You mumble to yourself incoherently and try that again...")

    pcMove(locationX, locationY)

def room36():
    print("You arrive at the base of the tower, which also has a slide down to the start point.")
    choice = input("Tower or start? >>> ")
    locationX    = 3
    locationY = 6
    if choice == "Tower" or choice == "tower":
        if insightCounter < 2:
            print("You lack the insight to continue and retreat back into the dungeon.")
            room46()
        else:
            print("You move up the the tower as the fogwall disappates in front of you.")
            locationY = locationY - 1
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You take the slip n slide back to the beginning!")
        startRoom()
    pcMove(locationX, locationY)

def room46():
    print("Room 46 leads to one room northward that looks peaceful and one spiral stairwell that leads to the tallest tower. Forward or stairwell?")
    locationX = 4
    locationY = 6
    choice = input("??? >>>")
    if choice == "forward" or choice == "Forward":
        locationX = locationX -1
        locationY = locationY + 1
    elif choice == "stairwell" or choice == "Stairwell":
        locationX = locationX - 1
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You have chosen an illegitimate move. Try again.")


    pcMove(locationX, locationY)

def room37():
    print("Room 37 is a bedroom for servants that has gone unused for some time. Exits left and right but a swarm of monsters are awoken all at once.")
    combat()
    combat()
    combat()
    print("Phew, that was rough but the loot was good. Do you go left or right?")
    locationX = 3
    locationY = 7
    choice = input("??? >>>")
    if choice == "left" or choice == "Left":
        locationX = locationX - 1
        locationY = locationY - 1
    elif choice == "right" or choice == "Right":
        locationX = locationX + 1
        locationY = locationY - 1
    elif choice == "quit" or choice == "Quit":
        quit()
    else:
        print("You mumble to yourself incoherently and try that again...")

    pcMove(locationX, locationY)

def room35():
    print("You arrive at the peak of the tower. In front of you stands a hideous beast of matted fur, towering over you and attacking with all its might!")
    bossFight()
    print("You have beaten the game! Thanks for playing!")
    exit(0)


startRoom()
