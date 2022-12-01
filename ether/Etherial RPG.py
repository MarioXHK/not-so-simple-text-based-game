import random
import time
room = 0
choice = "None"
maxhp = 50
hp = 50
atk = 5
deff = 1
money = 0
xp = 0
lvl = 1
xpreq = 50

inventory = ["Gummy Bears"]
weapon = "Controller"
armor = "Jacket"
keyitems = []
ghostkeys = []
seenrooms = []
valnorth = {"n","N","north","North"}
valsouth = {"s","S","south","South"}
valeast = {"e","E","east","East"}
valwest = {"w","W","west","West"}
valinv = {"i","I","inv","Inv","inventory","Inventory"}
valquit = {"q","Q","quit","Quit"}
valup = {"u","U","up","Up"}
valdown = {"d","D","down","Down"}
valgrab = {"g","G","grab","Grab"}
valuse = {"use","Use"}
valhelp = {"h","H","help","Help"}
vallook = {"l","L","look","Look"}
valyes = {"y", "Y", "Yes", "Yeah", "Sure", "Ok", "Fine", "yes", "yeah", "sure", "ok", "fine"}
valno = {"n", "N", "No", "Nope", "Nah", "no", "nope", "nah", "Not Today", "not today", "Not today", "not Today"}
team = ["you"]

def fancytext(texty, spext, waig = 0):
    global haste
    divzex = 1/int(spext)
    if haste == False:
        for i in range(len(texty)):
            print(texty[i], end = "")
            if texty[i] == ",":
                time.sleep(divzex*1.5)
            if texty[i] == ",":
                time.sleep(divzex*3)
            if texty[i] == "." or texty[i] == "?" or texty[i] == "!":
                time.sleep(divzex*6)
            time.sleep(divzex)
    else:
        print(texty, end = "")
    time.sleep(int(waig))




def seeroom(hostile,biome = "nul"):
    global room
    global seenrooms
    if not room in seenrooms:
        seenrooms.append(room)
        if room == 0:
            fancytext("You wake up with a gasp of air. Looking around you're in a very dark part of a large forest.\n", 40, 1)
            fancytext("It's nearly impossible to see through this deep darkness, but you can see a light far up north. ", 40, 2)
        elif room == 1:
            fancytext("Coming closer to the light, the dark forest gets more illuminated, and you're able to see you're surroundings.\n", 20, 1)
            fancytext("The tree leaves appear to be a deep purple, the night sky above being filled with cyan stars, managing to even without a sun, bathing the forest ahead in it's light. ", 20, 2)
        elif room == 2:
            fancytext("You finally find yourself some breathing space as you're now at an opening, the forest appears to extend from here, and there are so many pathways to choose from.", 20, 1)
            fancytext("\nNow here, you can truly see that you have indeed ended up far from your school, maybe even in a different realm entirely.", 20, 1)
            fancytext("\nWhat was that thing Dr. Mo said...? ", 20, 1)
            fancytext("Either way, it also seams that you're not alone in this forest, many creatures loom, but they clear way as you walk in.\nBut they look like they won't do it the next time.", 20, 2)
    else:
        if room == 0:
            fancytext("The darkness here is near consuming, ", 20, 2)
        elif room == 1:
            fancytext("The light is coming through, ", 20, 2)
        else:
            num = random.randrange(0, 20)
            if biome == "forest":
                if num < 4:
                    fancytext("Tiedie flowers are seen blooming and wilting by the minute, always seeming to reproduce. The cycle of life continuing.", 20, 2)
                elif num < 10:
                    fancytext("Birds and bees are flying around the forest, ignoring you in the process.", 20, 2)
                elif num < 19:
                    fancytext("The light breeze of forest air fills you with determination.", 20, 2)
                else:
                    fancytext("A shooting star flies by in the sky, maybe it's time to make a wish?", 20, 2)
            if biome == "lightfor":
                if num < 4:
                    fancytext("Illuminous birds are flying around, singing heavenly melodies.", 20, 2)
                elif num < 9:
                    fancytext("The lights of the forest loom as it's luminosity aluminates you.", 20, 2)
                elif num < 12:
                    fancytext("It feels almost like a fresh new day in the forest despite you only being here for less than an hour.", 20, 2)
                else:
                    fancytext("This place is just lovely.", 20, 2)
    if room == 0:
        fancytext("Your only option you can see is going north.", 30, 2)
    elif room == 1:
        fancytext("North still appears to be where your journey will continue.", 30, 2)

def battlesetup(ebiome = "nul",chance = 5, spec = False):
    numb = random.randrange(0, chance)
    if numb == 0:
        ech = random.randrange(0, 20)
        monster = "g_cube"
        if ebiome == "nul":
            if ech == 1:
                monster = "cthurkey"
            if ech == 19:
                monster = "g_dragon"
        if ebiome == "forest":
            if ech < 6:
               monster = "live_tnt" 
            elif ech < 9:
                monster = "wolf"
            elif ech < 14:
                monster = "g_snail"
            elif ech < 19:
                monster = "sculker"
            else:
                monster = "m_yoyo"
        battle(monster)
                
def battle(monster = "g_cube"):
    global hp
    global atk
    global deff
    global valhelp
    global valuse
    global valinv
    global valquit
    global money
    global xp
    global xpreq
    global lvl
    
    valatk = {"Attack", "attack", "Die", "die", "Kill", "kill"}
    valcheck = {"Check","check"}
    valact = {"Act","act"}
    valspare = {"Mercy", "mercy", "Spare", "spare"}
    valrun = {"Run", "run", "flee", "Flee"}
    mercy = False
    boss = False
    gamename = "Monster"
    if monster == "g_cube":
        eatk = 5
        edef = 1
        ehp = 10
        emon = 10
        sreq = 2
        gamename = "Generic Cube"
        fancytext("A Generic Cube attacks!\n", 20, 1)
    elif monster == "g_dragon":
        eatk = 15
        edef = 5
        ehp = 100
        emon = 250
        sreq = 7
        boss == True
        gamename = "Generic Dragon"
        fancytext("A Generic Dragon attacks!\n", 20, 1)
    egph = ehp
    battle = True
    spare = False
    runaway = False
    spval = 0
    while battle == True:
        print("Your stats: hp:", hp, "attack", atk, "defence", deff)
        print("enemy's HP:", ehp)
        for i in range(len(team)):
            turn = True
            while turn == True:
                if mercy == True:
                    print(gamename, "is sparing you.")
                batchoice = input()
                if batchoice in valhelp:
                   fancytext("Glad you asked at this time.\n", 50, 1)
                   fancytext("You are currently inside an enemy battle. The goal is to not die- I mean get knocked out from the enemy.\nThere are many ways to do this, like sparing the enemy or killing it, or just fleeing.\nto attack the enemy, type in \"attack\",\nto use one of your inventory items, type in \"use\", to check the enemy's stats, type in \"check\",\nto spare an enemy, you have to convince it enough by typing in \"action\" or just by attacking it enough, then you can spare them by typing in \"spare\".\nSparing gives more money than fighting, but doesn't give you XP.\nIf you want to attempt to run away, type in \"run\".", 50, 2)
                elif batchoice in valatk:
                    atkdone = (atk+random.randrange(-2,2)) * lvl
                    print(atk)
                    if mercy == True:
                        atkdone = atkdone*2
                    atkdone = atkdone-edef
                    ehp -= atkdone
                    fancytext("\nYou attack and deal ", 20)
                    fancytext(str(atkdone), 20)
                    fancytext(" damage!\n", 20, 1)
                    if ehp <= (egph/4) and boss == False:
                        mercy = True
                    turn = False
                elif batchoice in valspare:
                    fancytext("\nYou spared ", 20)
                    fancytext(gamename, 20, 1)
                    if mercy == True:
                        spare = True
                        battle = False
                    else:
                        fancytext(" but they weren't sparing you yet\n", 20, 1)
                    turn = False
                elif batchoice in valact:
                    if monster == "g_cube":
                        fancytext("You wiggled some of your body at the Generic cube, the cube has no feelings for this.\n", 20)
                    elif monster == "g_dragon":
                        fancytext("You drooled at the dragon and the dragon was somewhat disgusted by your action...\n", 20)
                    spval += 1
                    turn = False
                elif batchoice in valrun:
                    fancytext("You tried to run away...\n", 20, 1)
                    if random.randrange(0,2) == 0 and boss == False:
                        runaway = True
                        battle = False
                        fancytext("and succeeded.\n", 20, 1)
                    else:
                        fancytext("and failed.\n", 20, 1)
                    turn = False
                elif batchoice in valcheck:
                    turn = False
                    print()
                    fancytext(gamename, 20)
                    fancytext(", it's stats are: ", 20, 1)
                    print("attack:", eatk,"defence:", edef,"max hp:", egph)
                    time.sleep(1)
                    if monster == "g_cube":
                        fancytext("This generic little cube likes to wander beyond the bounds of reality.\nIt's hard to encounter and if you have encountered it, it's likely that there's a problem or that you're just testing something.\n", 20, 2)
                    elif monster == "g_dragon":
                        fancytext("This standard dragon looms over you, seeming fearless.\n", 20, 2)
                elif batchoice in valuse:
                    fancytext("What will you use? (Please type it exactly as seen in the inventory)\n", 50)
                    print("Inventory:", inventory)
                    batchoice = input()
                    if batchoice in valquit:
                        fancytext("Going back...\n", 50)
                    elif batchoice in inventory:
                        gitemuse(batchoice, True)
                        turn = False
                    else:
                        fancytext("You don't have an item called", 30)
                        fancytext(batchoice, 30, 1)
                        print()
        if ehp <= 0:
            battle = False
            fancytext(gamename, 20)
            fancytext(" was defeated!", 20, 1)
        if battle == True:
            etkdone = eatk + random.randrange(-5,5)
            etkdone = etkdone - deff
            hp -= etkdone
            fancytext("The ", 20)
            fancytext(gamename, 20)
            fancytext(" attacks and deals ", 20)
            fancytext(str(etkdone), 20)
            fancytext(" damage to you!\n", 20, 1)
            if hp <= 0:
                fancytext("You ran out of hp!\n", 20, 1)
                fancytext("You got knocked out...\n", 20, 2)
                fancytext("\nGAME OVER\n", 10, 2)
                exit()
            if sreq <= spval:
                mercy = True
        else:
            if runaway == False:
                fancytext("You Won!\n", 20, 2)
                mongain = emon + random.randrange(-2,3)
                if spare == True:
                    mongain += (emon/2) + random.randrange(1,8)
                    xpgain = 0
                else:
                    xpgain = emon
                money += mongain
                fancytext("You gained ", 20)
                fancytext(str(xpgain), 20)
                fancytext(" xp and ", 20)
                fancytext(str(mongain), 20)
                fancytext(" money!\n", 20, 1)
                leveling(xpgain)
                if monster == "g_cube" and spare == False:
                    inventory.append("Generic Sword")
                    fancytext("The Generic Cube dropped a Generic Sword! How generic!\n", 20, 2)
            
def leveling(thexp):
    global xp
    global xpreq
    global lvl
    global maxhp
    
    xp += thexp
    if xpreq <= xp:
        xp -= xpreq
        xpreq *= 2
        maxhp += 12
        lvl += 1
        fancytext("Your level increased!\n", 20, 2)
        



def gitemuse(item, bmode = False):
    global inventory
    global weapon
    global armor
    global hp
    global maxhp
    global weapon
    global armor
    global atk
    global deff
    global keyitems
    usedup = True
    if item == "Gummy Bears":
        hp += 12
        if hp > maxhp:
            fancytext("You ate the Gummy Bears and your health maxed out!\n", 20, 1)
            hp = maxhp
        else:
            fancytext("You ate the Gummy Bears and recovered 12 hp!\n", 20, 1)
    if item == "Controller":
        fancytext("You equipped the controller as a weapon.\n", 20, 1)
        atk = 5
        inventory.append(weapon)
        weapon = "Controller"
    if item == "Generic Sword":
        fancytext("You equipped the Generic Sword.\n", 20, 1)
        atk = 20
        inventory.append(weapon)
        weapon = "Generic Sword"
    if item == "Jacket":
        fancytext("You wore the jacket.\n", 20, 1)
        deff = 1
        inventory.append(armor)
        weapon = "Jacket"
    if usedup == True:
        if not item in keyitems:
            inventory.remove(item)
        else:
            keyitems.remove(item)
        

    

def default(choice):
    global gamenotover
    global valhelp
    global valquit
    global valinv
    global valgrab
    global valuse
    global inventory
    global keyitems
    global valquit
    valstats = {"Status", "status", "stats", "Stats", "State", "state"}
    
    
    if choice in valhelp:
        fancytext("Glad you asked!\n", 30, 2)
        fancytext("You see, to move around here, you have to type in the direction you want to go in, which can be north, south, east, west, up, or down.\n", 50, 2)
        fancytext("If you want look around the room to see what is in it and where you can go from there, type in \"look\".\n", 50, 2)
        fancytext("To grab something that is in the room, just type in \"grab\" and the thing will be added to your inventory.\n", 50, 2)
        fancytext("You can't hold a lot of regular items, luckily, your pockets are very deep, so you can hold as many as items.\n", 50, 2)
        fancytext("While you only have soo much space for regular items, you can have as much space as possible to store key items.\n", 50, 2)
        fancytext("To see regular items and key items, type in \"inventory\" or just \"inv\".\n", 50, 1)
        fancytext("You can use these items by typing in \"use\"", 40)
    elif choice in valstats:
        print("Your stats: hp:", hp, "attack", atk, "defence", deff)
        print("You have ", hp, "attack", atk, "defence", deff)
    elif choice in valquit:
        fancytext("Are you sure you want to quit?", 40)
        choice = input()
        if choice in valyes:
            fancytext("...And so...you were stuck forever. ", 10, 2)
            fancytext("The end :D", 40)
            gamenotover = False
    elif choice in valinv:
        fancytext("Inventory: ", 40, 1)
        print(inventory)
        time.sleep(0.5)
        fancytext("Key Items: ", 40, 1)
        print(keyitems)
    elif choice in valgrab:
        fancytext("There is nothing to grab here.", 50)
    elif choice in valuse:
        if inventory == [] and keyitems == []:
            fancytext("You have nothing to use.", 50)
        else:
            fancytext("What will you use? (Please type it exactly as seen in the inventory)", 50)
            print("Inventory:", inventory)
            print("Key Items:", keyitems)
            choice = input()
            if choice in inventory or choice in keyitems:
                gitemuse(choice)
            else:
                fancytext("You don't have an item called", 30)
                fancytext(choice, 30, 1)
                print()


print("Would you like to enable haste mode? (Haste mode instantly prints the text.)\n")
choice = input()
if choice in valyes:
    haste = True
else:
    haste = False
battle()
battle("g_dragon")
fancytext("Do you want to skip the intro?\n", 50)
choice = input()
fancytext("To look at the list of what you can do at any time, type in help.\n", 50, 2)
if (not choice in valyes) or choice in valno:
    fancytext("Let's begin our story.\n", 20, 2)
    fancytext("Long ago, there was a world called...\n", 20, 2)
    fancytext("I forgor. :skull:\n", 10, 2)
    fancytext("Anyways onto the story. It starts on a planet, in a country, in a state, on a hill, in a school, in a class.\n", 50, 2)
    fancytext("\"Man! Why do I have to work with someone Dr. Mo?\"\n", 50, 2)
    fancytext("\"Didn't you see the video about it?\"\n", 50, 2)
    fancytext("\"Augh! It just doesn't make sense! I'm a lone wolf y'know, I work better by myself!\"\n", 50, 2)
    fancytext("\"Well you better find a partner and pair up with someone or else I'm sending you to the Ether.\"\n", 50, 2)
    fancytext("\"Wait...", 10, 1)
    fancytext("The what?\"\n", 20, 2)
    fancytext("\"You heard me! I'm sending you to the Ether if you don't get a partner!\"\n", 50, 2)
    fancytext("\"Umm, ok, Mo, ok.", 50, 2)
    fancytext(" I get it, you're threatening to send me to somewhere like the shadow realm to try and be like one of us younger generations.\"\n", 50, 2)
    fancytext("\"The shadow realm? I'm not that powerful y'know.\n", 50, 2)
    fancytext("This is your last warning. Get a partner or I'm sending you to the Ether.\"\n", 50, 2)
    fancytext("\"Oh, ", 50, 0)
    fancytext("please, ", 5, 1)
    fancytext("this 'Ether' doesn't really exist, and even so, how will you get me to wherever that is?\"\n", 50, 2)
    fancytext("\"With this\"\n", 50, 2)
    fancytext("Dr. Moe pulled out a giant massive magical staff out of her desk.\n", 50, 2)
    fancytext("\"...", 5, 2)
    fancytext("Oh damn.\"\n", 10, 2)
    fancytext("And with that Dr. Mo banished you into the Ether by shattering the floor below you.\n", 50, 1)
    fancytext("\"DOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!\"\n", 100, 2)
    fancytext("You fall and fall, so far down. You were sure that you were dead when you hit the ground, however, when you did hit a ground, you didn't die.\n", 20, 2)
    fancytext("However, you were knocked out cold.", 20, 2)
    fancytext("And thus, your adventure begins, in the realm of\n", 20, 2)
    fancytext("ETHER.", 5, 5)
gamenotover = True
seeroom(False)
while gamenotover == True:
    choice = input("\n")
    print(room)
    if room == 0:
        if choice in valnorth:
            room = 1
        elif choice in vallook:
            fancytext("It's near impossible to see anything here. ", 20, 1)
            fancytext("It's all just darkness without end, like if the trees were a perfect shader.", 20, 2)
        else:
            default(choice)
        seeroom(False)
    elif room == 1:
        if choice in valsouth:
            room = 0
        elif choice in valnorth:
            room = 2
            seeroom(True)
        elif choice in vallook:
            fancytext("Now in this passageway, you can begin to see the forest more clearly, and it's beautiful in a way.", 20, 1)
            fancytext("\nAbove you, the trees are allowing the light of the night to shine through into this odd forest of purple trees.", 20, 2)
        else:
            default(choice)
    elif room == 2:
        if choice in valsouth:
            room = 1
            seeroom(False)
        elif choice in valnorth:
            room = 7
            seeroom(True)
        elif choice in valeast:
            room = 3
            seeroom(True)
        elif choice in valwest:
            room = 9
            seeroom(True)
        elif choice in vallook:
            fancytext("In this opening, you can truly appreciate the forests beauty, nearly everywhere you look there's something about it.", 20, 1)
            fancytext("\nIt fills you with hopes and dreams", 20, 2)
        else:
            default(choice)