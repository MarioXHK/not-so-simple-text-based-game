import random
import time
room = 0
choice = "None"
maxhp = 50
hp = 50
money = 0
xp = 0
lvl = 1
xpreq = 50

inventory = ["Gummy Bears"]
weapon = "Controller"
armor = "Jacket"
speedrun = False
mobattle = False
haste = False
repetimes = 0
solvedit = False

def atk(modif = 0):
    global weapon
    global lvl
    weapondic = {"Controller":5,"Soft Sword":10,"Iron Sword":15,"Generic Sword":20}
    return round((weapondic[weapon] + (1.2 * lvl) * (1.2 * modif)))
    
def deff(modif = 0):
    global armor
    global lvl
    armordic = {"Jacket":1,"Pumpkin Helmet":3,"Scarlet Hide":7,"Pipeline Shield":10,"Zomboid Jacket":15}
    return round((armordic[armor] + (1.2 * lvl) * (1.2 * modif)))

keyitems = []
ghostitems = []
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
valheal = {"heal","Heal","h","H"}
valhelp = {"h","H","help","Help"}
vallook = {"l","L","look","Look"}
valshop = {"shop", "Shop", "store", "Store"}
valyes = {"y", "Y", "Yes", "Yeah", "Sure", "Ok", "Fine", "yes", "yeah", "sure", "ok", "fine"}
valno = {"n", "N", "No", "Nope", "Nah", "no", "nope", "nah", "Not Today", "not today", "Not today", "not Today"}
team = ["you"]

def fancytext(texty, spext, waig = 0):
    global haste
    global speedrun
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
    if speedrun == False:
        time.sleep(int(waig))




def seeroom(hostile, room, biome = "nul"):
    global seenrooms
    global team
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
            fancytext("\nWhat was that thing Dr. Mo said...? ", 20, 2)
            fancytext("Either way, it also seams that you're not alone in this forest, many creatures loom, but they clear way as you walk in.\nBut they look like they won't do it the next time.", 20, 1)
        elif room == 3:
            fancytext("Going further into the forest, you find yourself estranged, all of this happening... A whole new world.\n", 20, 1)
            fancytext("You can't help but just take a deep breath and let it all in, and that's when you notice again a house up north, it seams big, whoever might live in it?", 20, 1)
        elif room == 4:
            fancytext("Approaching the house, you get onto it's porch, you wonder who or what could be inside so you decide to knock on the door, but nobody answers.\n", 20, 1)
            fancytext("On the porch there is just a garden gnome and a rotted out welcome mat.", 20, 1)
        elif room == 5:
            fancytext("Entering the house, you are in what appears to be the living room of the house, with a furry couch and a ball on it.\n", 20, 1)
            fancytext("There are many things all around the room that make you wonder just how did the owner of this house collect all of this?", 20, 1)
            fancytext("It was wrong, but you had a feeling of wanting to explore deeper inside this place.", 20, 1)
        elif room == 6:
            fancytext("Entering the next room, it's a corridor that paths out to many other rooms, such as a bathroom, bedroom, and kitchen, strangely having a few signs of activity despite you not seeing anyone in them.\n", 20, 1)
            fancytext("You could spot many things, but the one thing that most interested you was a hatch on the ceiling with a rope on it, appearing to lead to the upstairs of this house.", 20, 1)
            fancytext("There was also a back door, however, it seamed to be combination locked from the inside... strange.", 20, 1)
        elif room == 7:
            fancytext("Going up the ladder, you see many more trinkets here than there were in the living room, practically filling up this entire part of the house.\n", 20, 1)
            fancytext("There is a light coming from the room to the west, with that cat silhouette from the window also noticable from here.", 20, 1)
            fancytext("Maybe you could see what this cat was.", 20, 1)
        elif room == 8:
            fancytext("You finally enter the room, and you now see the cat person in the room as well, holding a candle in one hand, with a cloak on.\n", 20, 1)
            fancytext("'Greetings, human, I have been expecting you-'", 10)
            fancytext(" Suddenly the cat trips and drops the candle.\n", 20, 1)
            fancytext("'CRAP-' A small fire happens on the floor and the cat stomps it out, but then the cat notices a fire on the cloak and then just dunks themselves in a bunch of water.\n", 20, 1)
            fancytext("'...", 10,1)
            fancytext("Well that went horribly...", 10)
            fancytext("Sorry, I fumbled that introduction, I'm Zoey, the main cat of the Ether.\n", 20,1)
            fancytext("You look lost, seams like you've never been to the Ether before. I guess you want to try and get out of here as fast as possible.\n", 20,1)
            fancytext("I can help you with that, we can be a team, y'know.", 20,1)
            fancytext(" Also, I know the combination of the back door,\nand you'll need me to get through it and enter the glow forest, which is possibly your only way to get back.\n", 20,1)
            fancytext("There, you can find the fibers of life, and those can take you back to your own world. So let's go!'\n", 20,1)
            fancytext("ZOEY JOINED THE PARTY!", 5,1)
            team.append("Zoey")
        elif room == -1:
            fancytext("Going further east you find a small stand that you could maybe buy things from.\n", 20, 1)
            fancytext("Perhaps by typing in \"shop\" you could access this store.\n", 20, 1)
        elif room == 9:
            fancytext("This way, the forest appears to get lighter and less dense as fewer trees surround you, and you can see some reflection on the ground in the distance.\n", 20, 1)
            fancytext("It appears to be a lake that is reflecting all that light. ", 20, 1)
            fancytext("It's oddly calming.\n", 20, 1)
        elif room == 10:
            fancytext("You approach the lake and truly have a scope on how big it is. It's very calm with only a few fish showing up within your view, with there also there being something shiny at the bottom of the lake.\n", 20, 1)
            fancytext("Feels like the place to take a breather from your situation.\n", 20, 1)
        elif room == 11:
            fancytext("As you exit the house, you are immediately in a different forest, as if this house was like a boarder between the 2 forests.\n", 20, 1)
            fancytext("This forest was different than the other one, with it's tree bark being all black, having no leaves, but blooming glowing flowers of all sorts of colors.\n", 20, 1)
            fancytext("These trees give you a feeling like no other.\n", 20, 1)
            fancytext("'You know, this part of the Ether can get to you, it's easy to get lost.\n", 20, 1)
            fancytext("Luckily, you have me to guide you through this place, I even marked a path!'\n", 20, 1)
        elif room == 12:
            fancytext("Going down this path fills you with many feelings, all because of the trees around here.\n", 20, 1)
            fancytext("You can see one of the trees being held in something like a furnace as you enter just within reach.\n", 20, 1)
        elif room == 13:
            fancytext("Heading further down the path reveals that the path begins to grow dim and soon becomes unrecognizable.\n", 20, 1)
            fancytext("You weren't even sure where you were going or where you came from anymore because of this, making you almost lost.\n", 20, 1)
        elif room == 14:
            fancytext("You were able to find your way forward in the path as the path comes back to life here.\n", 20, 1)
            fancytext("That was indeed a close one, who knows what would've happened if you had wandered too far off the path.\n", 20, 1)
        elif room == 15:
            fancytext("You continue down the path and see a purple glow tree in the path.\n", 20, 1)
            fancytext("It seamed weirder than the others, and is glowing wrather strong.\n", 20, 1)
        elif room == 16:
            fancytext("You have made it to the fibers of life, these magnificent fibers all appeared to be coming from the sky, like a reverse beacon..\n", 20, 1)
            fancytext("There was also a shine next to the fibers, and a healing aura came off of it.\n", 20, 1)
            fancytext("'Oh, that's a healing shrine! you can type in \"heal\" when you see these to heal up all the way!'\n", 20, 1)
            fancytext("Might wanna do so since these creatures keep beating you up.\n", 20, 1)
            fancytext("Then all you need to do is head into the fibers and you'll be transported to where you need to be.\n", 20, 1)
            fancytext("It's nice to have a visitor once and awhile, but you must be eager to get back to your world.'\n\n", 20, 1)

    else:
        if room == 0:
            fancytext("The darkness here is near consuming, ", 20, 2)
        elif room == 1:
            fancytext("The light is coming through, ", 20, 2)
        elif room == 5:
            fancytext("A small breeze enters the house.", 20, 2)
        elif room == 6:
            if random.randrange(0, 3) == 2:
                fancytext("Some mice are battling for cheese in the bedroom.", 20, 2)
            else:
                fancytext("The ceiling light flickers a bit.", 20, 2)
        elif room == 10:
            fancytext("The lake's shore calmly settles under the nightlight sky.", 20, 2)
        else:
            if random.randrange(0, 3) == 2 and hostile == True:
                    battlesetup(biome)
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
                    elif num < 18:
                        fancytext("It feels like you could get lost by staying long enough, but maybe you wouldn't mind.", 20, 2)
                    else:
                        fancytext("This place is just lovely.", 20, 2)
    if room == 0:
        fancytext("\nYour only option you can see is going north.", 30, 2)
    elif room == 1:
        fancytext("\nNorth still appears to be where your journey will continue.", 30, 2)
    elif room == 2:
        fancytext("\nEvery way you look there is a place to go, north leading to what appears to be a house of some sort, while east and west are more forest.\n", 30, 2)
    elif room == 3:
        fancytext("\nThere is a house up north while going further east there appears to be a shop.\n", 30, 2)
    elif room == 4:
        fancytext("\nThe door to the house is north while the south leads back into the forest.\n", 30, 2)
    elif room == 5:
        fancytext("\nYou can go back the way you came, or go east into a corridor.\n", 30, 2)
    elif room == 6:
        fancytext("\nYou could maybe go upstairs, or try the door on the north.\n", 30, 2)
    elif room == 7:
        fancytext("\nYou can go downstairs or to the westmost room.\n", 30, 2)
    elif room == 8:
        fancytext("\nUnless you consider the window here an exit, the only way back is east.\n", 30, 2)
    elif room == 9:
        fancytext("\nThe opening continues up west, with the way back into the main part of the forest being east.\n", 30, 2)
    elif room == 10:
        fancytext("\nThe way back into the forest is east.\n", 30, 2)
    elif room == 11:
        fancytext("\nThe path continues west and the door behind is south.\n", 30, 2)
    elif room == 12:
        fancytext("\nThe path continues further west while going back is east.\n", 30, 2)
    elif room == 13:
        fancytext("\nYou can't tell where you can go or not.\n", 30, 2)
    elif room == 14:
        fancytext("\nGoing back down is a weird idea, but it seams to be your way back, on the other hand, east is the way forward.\n", 30, 2)
    elif room == 15:
        fancytext("\nEast seams the way forward, west is the way back.\n", 30, 2)
    elif room == -1:
        fancytext("\nThe way back is west.\n", 30, 2)

def shop(yeses, quits, helping,items, monin, dio = 0):
    global invntory
    global lvl
    global team
    
    validitems = {
        "Raw Fish": 6,
        "Soft Chips": 10,
        "Jacket": 18,
        "Controller": 16,
        "Pumpkin Helmet": 20,
        "Soft Sword": 24,
        "Cooked Fish": 26,
        "Attack Ruby": 26,
        "Convincing Stone": 30,
        "Gummy Bears": 16,
        "Bear Burger": 40,
        "Iron Sword": 50,
        "Scarlet Hide":30,
        "Pipeline Shield": 44,
        "Legendary Burger": 100
    }
    valbuy = {"buy","Buy","b","B"}
    valsell = {"sell","Sell","S","s"}
    valtalk = {"talk","Talk","chat","Chat","t","T","c","C", "Lore", "lore", "l", "L"}
    if dio == 0:
        fancytext("\"Welcome to this shop.\"\n", 20, 1)
    elif dio == 1:
        fancytext("\"Welcome, welcome! What would you like?\"\n", 20, 1)
    shopq = False
    
    while shopq == False:
        fancytext("Shop items: ", 30)
        for i in items:
            print(i, end = " ")
            print(validitems[i], end = "$ ")
        print()
        print("Your Inventory:", inventory)
        print("Your Money:", monin)
        shopreq = input("\n")
        if shopreq in helping:
            fancytext("This is a shop, you can either buy or sell items here, each respectively being able to be used by typing in \"buy\" and \"sell\". You are also able to talk to the shopkeeper if you'd like by typing in \"talk\"", 20, 1)
        elif shopreq in valbuy:
            if dio == 0:
                fancytext("\"What are you buying?\"\n", 20, 1)
            elif dio == 1:
                fancytext("\"What are ya buying?\"\n", 20, 1)
            fancytext("(Type exactly as shown)", 20, 1)
            shopreq = input("\n")
            if shopreq in items:
                if validitems[shopreq] <= monin:
                    if len(inventory) < 10:
                        monin -= validitems[shopreq]
                        inventory.append(shopreq)
                        if dio == 0:
                            fancytext("\"Thank you.\"\n", 20, 1)
                        elif dio == 1:
                            fancytext("\"Grand.\"\n", 20, 1)
                    else:
                        if dio == 0:
                            fancytext("\"You don't seam to have enough space in your inventory.\"\n", 20, 1)
                        elif dio == 1:
                            fancytext("\"Seams like your pockets are full, can't fit this in there.\"\n", 20, 1)
                else:
                    if dio == 0:
                        fancytext("\"You can't afford that.\"\n", 20, 1)
                    elif dio == 1:
                        fancytext("\"That aint enough money!\"\n", 20, 1)
            else:
                if dio == 0:
                    fancytext("\"That isn't available.\"\n", 20, 1)
                elif dio == 1:
                    fancytext("\"That ain't an option!\"\n", 20, 1)
        elif shopreq in valsell:
            if dio == 0:
                fancytext("\"What are you selling?\"", 20, 1)
            elif dio == 1:
                fancytext("\"What are ya giving me?\"", 20, 1)
            fancytext("(Type exactly as shown)", 20, 1)
            shopreq = input("\n")
            if shopreq in inventory:
                sellval = validitems[shopreq]/2
                monin += sellval
                inventory.remove(shopreq)
                fancytext("Sold ", 20)
                fancytext(shopreq, 20)
                fancytext(" for ", 20)
                fancytext(str(sellval), 20)
                fancytext(" dollars.\n", 20, 1)
                if dio == 0:
                    fancytext("\"Thank you.\"\n", 20, 1)
                elif dio == 1:
                    fancytext("\"Hehaha, thanks!\"\n", 20, 1)
                
            else:
                if dio == 0:
                    fancytext("\"You don't have an item by that name.\"\n", 20, 1)
                elif dio == 1:
                    fancytext("\"Can't take what you don't have.\"\n", 20, 1)
        elif shopreq in valtalk:
            if dio == 0:
                    fancytext("\"Oh, I'm just a simple shopkeeper, nothing to see here.\"", 20, 1)
            elif dio == 1:
                fancytext("\"So you're curious mind wants to know about this place? Don't blame ya, you don't look like you're from around here.\n", 20, 1)
                fancytext("Well this here place is called 'The Ether', filled with vast layers that your little mind wouldn't even be able to comprehend.\n", 20, 1)
                fancytext("That there house up north belongs to a woman named Zoey, she is practically the caretaker of this here Violet Forest.\n", 20, 1)
                fancytext("Maybe she could help you get out of this world and return to your own, ", 20, 1)
                if "Zoey" in team:
                    fancytext("\nWait, she's with you right now? Guess you already convinced her to help, good luck with that!\"\n", 20, 1)
                else:
                    if lvl > 3:
                        fancytext("or you two could have a little tea party, (the 2 of you look like a perfect fit).\"\n", 20, 1)
                    else:
                        fancytext("just don't try and hurt her, or I'll send yo to hell myself!\"\n", 20, 1)
                        
        elif shopreq in quits:
            fancytext("Are you sure you want to leave?", 20, 1)
            shopreq = input("\n")
            if shopreq in yeses:
                if dio == 0:
                    fancytext("\"Thank you for shopping.\"\n", 20, 1)
                elif dio == 1:
                    fancytext("\"Pleasure doing buisness with ya.\"\n", 20, 1)
                shopq = True
    fancytext("You exit the shop.\n", 20, 1)
    return monin


def battlesetup(ebiome = "nul",): #Sets a randomly generated battle up
    ech = random.randrange(0, 20)
    monster = "g_cube"
    if ebiome == "nul":
        if ech == 1:
            monster = "cthurkey"
        if ech == 19:
            monster = "g_dragon"
    elif ebiome == "forest":
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
    elif ebiome == "lightfor":
        if ech < 5:
            monster = "sculker" 
        elif ech < 7:
            monster = "origami"
        elif ech < 12:
            monster = "m_squid"
        elif ech < 17:
            monster = "wisp"
        elif ech < 19:
            monster = "g_frog"
        else:
            monster = "portalmaker"
    battle(monster)
                
def battle(monster = "g_cube"): #A battle station, spare or murder:bangbang:
    global hp
    global valhelp
    global valuse
    global valinv
    global valquit
    global money
    global xp
    global xpreq
    global lvl
    #A smoothie
    valatk = {"Attack", "attack", "Die", "die", "Kill", "kill"}
    valcheck = {"Check","check"}
    valact = {"Act","act"}
    valspare = {"Mercy", "mercy", "Spare", "spare"}
    valrun = {"Run", "run", "flee", "Flee"}
    valrock = {"Rock", "rock", "r", "R"}
    valpaper = {"Paper", "paper", "p", "P"}
    valscissors = {"Scissors", "scissors", "s", "S"}
    
    
    
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
        print("[]")
        fancytext("A Generic Cube attacks!\n", 20, 1)
    elif monster == "g_dragon":
        eatk = 15
        edef = 5
        ehp = 100
        emon = 250
        sreq = 7
        boss == True
        gamename = "Generic Dragon"
        print("^^")
        print("owo>>")
        print("~<=~<~")
        print("  _____==>")
        print("    v  v")
        fancytext("A Generic Dragon attacks!\n", 20, 1)
    elif monster == "live_tnt":
        eatk = 5
        edef = 0
        ehp = 5
        emon = 15
        sreq = 1
        gamename = "Living TNT"
        print(" ___")
        print("[TNT]")
        print(" ___")
        fancytext("A living piece of TNT hops at you!\n", 20, 1)
    elif monster == "wolf":
        eatk = 5
        edef = 0
        ehp = 5
        emon = 15
        sreq = 1
        gamename = "Wolf"
        print("[how tf do you draw a wolf?]")
        fancytext("A Lone Wolf jumps for you!\n", 20, 1)
    elif monster == "g_snail":
        eatk = 3
        edef = 10
        ehp = 5
        emon = 12
        sreq = 1
        gamename = "Gigasnail"
        print("r~~n     ∞")
        print("|roj|  / |")
        print("L======_J")
        fancytext("A Giga Snail slowly comes at you!\n", 20, 1)
    elif monster == "sculker":
        eatk = 8
        edef = 8
        ehp = 8
        emon = 25
        sreq = 2
        gamename = "Sculker"
        print("~\\ /~")
        print(" (o)")
        print("|r~n|")
        print("|| ||")
        print("||_||")
        print("0J L0")
        fancytext("A Sculker senses you!\n", 20, 1)
    elif monster == "m_yoyo":
        eatk = 6
        edef = 2
        ehp = 7
        emon = 22
        sreq = 2
        gamename = "Magic Yoyo"
        print("O__J")
        fancytext("A sentient magical Yoyo swings at you!\n", 20, 1)
    elif monster == "origami":
        eatk = 8
        edef = 0
        ehp = 5
        emon = 10
        sreq = 1
        gamename = "Enchanted Origami"
        print("[=]")
        fancytext("Some Origami folds up and attacks you!\n", 20, 1)
    elif monster == "m_squid":
        eatk = 7
        edef = 0
        ehp = 15
        emon = 13
        sreq = 2
        gamename = "Music Squid"
        print("<コ:彡")
        fancytext("A musical squid comes to ink you up!\n", 20, 1)
    elif monster == "wisp":
        eatk = 2
        edef = 10
        ehp = 1
        emon = 20
        sreq = 0
        gamename = "Wisp"
        print("E(o)3")
        fancytext("A Wisp sneaks up on you!\n", 20, 1)
    elif monster == "rps_legend":
        eatk = 10
        edef = 10
        ehp = 100
        emon = 100
        sreq = 10
        gamename = "Rock Paper Scissors Legend"
        print("()   v   []")
        print("¯\_(ツ)_/¯")
        print("  (    )")
        print("  (____)")
        print("  /    \\")
        fancytext("The Rock Paper Scissors Legend stands their ground!\n", 20, 1)
    elif monster == "mo":
        eatk = 7
        edef = 5
        ehp = 50
        emon = 120
        sreq = 10
        gamename = "Dr. Mo"
        fancytext("Dr. Mo blocks the path!\n", 20, 1)
        boss = True
    else: #For when an invalid monster is put
        eatk = 1
        edef = 1
        ehp = 1
        emon = 1
        sreq = 1
        gamename = "Missingno"
        print("####")
        print("####")
        print("####")
        print("####")
        print("####")
        print("######")
        print("######")
        print("######")
        fancytext("A wild Missingno appears! Something has gone terribly wrong!\n", 20, 1)
    egph = ehp
    battle = True
    spare = False
    runaway = False
    spval = 0
    atkmod = 0
    defmod = 0
    while battle == True:
        print("Your stats: hp:", hp, "attack", atk(), "defence", deff())
        print("team:", team)
        print("enemy's HP:", ehp)
        for i in range(len(team)):
            if sreq <= spval:
                mercy = True
            turn = True
            while turn == True:
                if mercy == True:
                    print(gamename, "is sparing you.")
                batchoice = input("\n")
                if batchoice in valhelp:
                   fancytext("Glad you asked at this time.\n", 50, 1)
                   fancytext("You are currently inside an enemy battle. The goal is to not die- I mean get knocked out from the enemy.\nThere are many ways to do this, like sparing the enemy or killing it, or just fleeing.\nto attack the enemy, type in \"attack\",\nto use one of your inventory items, type in \"use\", to check the enemy's stats, type in \"check\",\nto spare an enemy, you have to convince it enough by typing in \"action\" or just by attacking it enough, then you can spare them by typing in \"spare\".\nSparing gives more money than fighting, but doesn't give you XP.\nIf you want to attempt to run away, type in \"run\" to initiate a rock paper scissors battle, if you win, you can run away.", 50, 2)
                elif batchoice in valatk:
                    atkdone = atk(atkmod)+random.randrange(-2,2)
                    if mercy == True:
                        atkdone = atkdone*2
                    atkdone = atkdone-edef
                    if atkdone < 0:
                        atkdone = 0
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
                        fancytext("You wiggled some of your body at the Generic cube, the cube has no feelings for this.\n", 20, 2)
                    elif monster == "g_dragon":
                        fancytext("You drooled at the dragon and the dragon was somewhat disgusted by your action...\n", 20, 2)
                    elif monster == "live_tnt":
                        fancytext("You drenched the Living TNT in water, and it becomes more content.\n", 20, 2)
                    elif monster == "wolf":
                        fancytext("You try and pet the wolf, and somewhat succeed.\n", 20, 2)
                    elif monster == "g_snail":
                        fancytext("You wiggled to try and tell the snail something... It seems amused.\n", 20, 2)
                    elif monster == "sculker":
                        fancytext("You grab some of the stuff from the ground and throw it at the Sculker to distract it.\n", 20, 2)
                    elif monster == "m_yoyo":
                        fancytext("You grab the yoyo, but it flew free of your grasp, looking a bit upset.\n", 20, 2)
                    elif monster == "m_squid":
                        fancytext("You take out some painting supplies and paint something for the musical squid, it seames pleased.\n", 20, 2)
                    elif monster == "wisp":
                        fancytext("You spiritually connect with the wisp, you learn it's story... the wisp becomes content.\n", 20, 2)
                    elif monster == "rps_legend":
                        fancytext("You try and reason with the RPS Legend, but they aren't having any of it and want to play rock paper scissors!\n", 20, 2)
                    elif monster == "origami":
                        fancytext("You take some paper and fold the Enchanged Origami some friends, it's happy.\n", 20, 2)
                    elif monster == "mo":
                        fancytext("You try and convince Dr. Mo that you've learned your lesson.\n", 20, 2)
                    else:
                        fancytext("You calm the monster down.", 20, 2)
                    spval += 1
                    turn = False
                elif batchoice in valrun:
                    fancytext("Pick rock paper or scissors\n", 20, 1)
                    batchoice = input("\n")
                    fancytext("Rock...Paper...Scissors...\n", 10, 1)
                    fancytext("SHOOT!\n", 50)
                    if monster == "live_tnt" or monster == "m_yoyo":
                        if random.randrange(0,4) == 0:
                            enchoice = "rock"
                        else:
                            enchoice = "paper"
                    elif monster == "wolf":
                        if random.randrange(0,2) == 0:
                            enchoice = "scissors"
                        else:
                            enchoice = "rock"
                    elif monster == "g_snail":
                        enchoice = "rock"
                    elif monster == "origami":
                        enchoice = "paper"
                    elif monster == "sculker":
                        enchoice = "scissors"
                    elif monster == "m_squid":
                        enchoice = batchoice
                    elif monster == "rps_legend":
                        if random.randrange(0,2) == 0:
                            if batchoice in valrock:
                                enchoice = "paper"
                            elif batchoice in valpaper:
                                enchoice = "scissors"
                            elif batchoice in valscissors:
                                enchoice = "rock"
                        else:
                            if enchoice == 0:
                                enchoice = "rock"
                            elif enchoice == 1:
                                enchoice = "paper"
                            elif enchoice == 2:
                                enchoice = "scissors"
                    elif boss == True:
                        if batchoice in valrock:
                            enchoice = "paper"
                        elif batchoice in valpaper:
                            enchoice = "scissors"
                        elif batchoice in valscissors:
                            enchoice = "rock"
                    else:
                        enchoice = random.randrange(0,3)
                        if enchoice == 0:
                            enchoice = "rock"
                        elif enchoice == 1:
                            enchoice = "paper"
                        elif enchoice == 2:
                            enchoice = "scissors"
                    
                    if batchoice in valrock:
                        print(" ___")
                        print("(    )")
                        print("~~~~~")
                        batchoice = "rock"
                    if batchoice in valpaper:
                        print("____")
                        print("|   |")
                        print("____")
                        batchoice = "paper"
                    if batchoice in valscissors:
                        print("|\\/|")
                        print("\\  /")
                        print("0 0")
                        batchoice = "scissors"
                    else:
                        print("\\ /")
                        print(" X ")
                        print("/ \\")
                        batchocie = "none"
                        
                    if enchoice in valrock:
                        print(" ___")
                        print("(    )")
                        print("~~~~~")
                        batchoice = "rock"
                    if enchoice in valpaper:
                        print("____")
                        print("|   |")
                        print("____")
                        batchoice = "paper"
                    if enchoice in valscissors:
                        print("|\\/|")
                        print("\\  /")
                        print("0`0")
                        enchoice = "scissors"
                    else:
                        print("\\ /")
                        print(" X ")
                        print("/ \\")
                        enchoice = "none"
                    if batchoice == enchoice:
                        fancytext("A draw!", 20, 1)
                    else:
                        if batchoice == "none":
                            fancytext("You didn't do a move! Automatic loss!", 20, 1)
                        elif enchoice == "none":
                            fancytext("The enemy didn't do a move! Automatic win!", 20, 1)
                            battle = False
                            runaway = True
                        elif batchoice == "rock":
                            if enchoice == "paper":
                                fancytext("Paper covers rock, you lose!", 20, 1)
                            elif enchoice == "scissors":
                                fancytext("Rock crushes scissors, you win!", 20, 1)
                                battle = False
                                runaway = True
                        elif batchoice == "paper":
                            if enchoice == "rock":
                                fancytext("Paper covers rock, you win!", 20, 1)
                            elif enchoice == "scissors":
                                fancytext("scissors cuts paper, you lose!", 20, 1)
                                battle = False
                                runaway = True
                        elif batchoice == "scissors":
                            if enchoice == "rock":
                                fancytext("Rock crushes scissors, you lose!", 20, 1)
                            elif enchoice == "paper":
                                fancytext("scissors cuts paper, you win!", 20, 1)
                                battle = False
                                runaway = True
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
                    elif monster == "live_tnt":
                        fancytext("This living TNT doesn't appear to be so harmful unless you attack it.\n", 20, 2)
                    elif monster == "wolf":
                        fancytext("This wolf stands alone, doesn't seam to have any allies for backup.\n", 20, 2)
                    elif monster == "g_snail":
                        fancytext("A giant snail that looks to belong to a garden, however there aren't any around.\n", 20, 2)
                    elif monster == "origami":
                        fancytext("Enchanted pieces of folded paper into life from an enchantment book.\n", 20, 2)
                    elif monster == "sculker":
                        fancytext("Very strong enemy if it were any older, it can't see but it can hear extremely well.\n", 20, 2)
                    elif monster == "m_yoyo":
                        fancytext("This Yoyo likes to go out and yo itself, it doesn't need any hands to yo, yo.\n", 20, 2)
                    elif monster == "m_squid":
                        fancytext("This squid is into music that you can't understand, yet you feel into it too.\n", 20, 2)
                    elif monster == "wisp":
                        fancytext("The Wisp wanders around aimlessly throughout the Ether.\n", 20, 2)
                    elif monster == "rps_legend":
                        fancytext("This guy really likes Rock Paper Scissors, he's studied the arts of all three moves and has been training their entire life for this moment.\nTry to flee to play rock paper scissors with him, it's probably your only choice.\n", 20, 2)
                    elif monster == "mo":
                        fancytext("She's the top witch in CEC with her knowledge of magic unmatched by anyone else.\nAll her time playing video games was really just her training in disquise, hoping to teach her students the ways of magic as well by secretly giving some of them lessons.\nYou've known her for a good while and could've never expected this. Guess you get a front row seat for one of her demonstrations.\n", 20, 2)
                    else:
                        fancytext("A real monster!\n", 20, 2)
                elif batchoice in valuse:
                    fancytext("What will you use? (Please type it exactly as seen in the inventory)\n", 50)
                    print("Inventory:", inventory)
                    batchoice = input("\n")
                    if batchoice in valquit:
                        fancytext("Going back...\n", 50)
                    elif batchoice in inventory:
                        theu = gitemuse(batchoice, True, boss)
                        atkmod += theu[0]
                        defmod += theu[1]
                        if theu[2] == True:
                            mercy = True
                        turn = False
                    else:
                        fancytext("You don't have an item called ", 30)
                        fancytext(batchoice, 30, 1)
                        print()
        if ehp <= 0:
            battle = False
            fancytext(gamename, 20)
            if monster == "live_tnt":
                hp -= 20
                fancytext(" blew up and delt a harsh 20 damage!", 20, 1)
                killsequence(hp)
            else:
                fancytext(" was defeated!", 20, 1)
        if battle == True:
            etkdone = eatk + random.randrange(-5,5)
            etkdone = etkdone - deff(defmod)
            if (monster == "mo" and hp < 7) or etkdone < 0:
                etkdone = 0
            hp -= etkdone
            fancytext("The ", 20)
            fancytext(gamename, 20)
            fancytext(" attacks and deals ", 20)
            fancytext(str(etkdone), 20)
            fancytext(" damage!\n", 20, 1)
            if monster == "mo" and hp <= 0:
                fancytext("Wh-!\n", 50)
            killsequence(hp)
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
                xp = leveling(xp, xpgain)
                if monster == "g_cube" and spare == False:
                    inventory.append("Generic Sword")
                    fancytext("The Generic Cube dropped a Generic Sword! How generic!\n", 20, 2)
    return spare
def killsequence(hep):
    if hep <= 0:
        fancytext("You ran out of hp!\n", 20, 1)
        fancytext("You got knocked out...\n", 20, 2)
        fancytext("\nGAME OVER\n", 10, 2)
        exit()

def leveling(exp,thexp):
    global xpreq
    global lvl
    global maxhp
    
    exp += thexp
    if xpreq <= exp:
        exp -= xpreq
        xpreq *= 2
        maxhp += 12
        lvl += 1
        fancytext("Your level increased!\n", 20, 2)
    return exp
        



def gitemuse(item, bmode = False, bossy = False):
    global inventory
    global weapon
    global armor
    global hp
    global maxhp
    global weapon
    global armor
    global keyitems
    global ghostitems
    global room
    used = False
    
    usedup = True
    atkmodifier = 0
    defmodifier = 0
    instaspare = False
    if item == "Gummy Bears":
        hp += 14
        if hp > maxhp:
            fancytext("You ate the Gummy Bears and your health maxed out!\n", 20, 1)
            hp = maxhp
        else:
            fancytext("You ate the Gummy Bears and recovered 14 hp!\n", 20, 1)
        used = True
    elif item == "Controller":
        fancytext("You equipped the controller as a weapon.\n", 20, 1)
        atk = 5
        inventory.append(weapon)
        weapon = "Controller"
        used = True
    elif item == "Generic Sword":
        fancytext("You equipped the Generic Sword.\n", 20, 1)
        inventory.append(weapon)
        weapon = "Generic Sword"
        used = True
    elif item == "Jacket":
        fancytext("You wore the jacket.\n", 20, 1)
        inventory.append(armor)
        weapon = "Jacket"
        used = True
    elif item == "Soft Chips":
        hp += 10
        if hp > maxhp:
            fancytext("You ate the Soft Chips and your health maxed out!\n", 20, 1)
            hp = maxhp
        else:
            fancytext("You ate the Soft Chips and recovered 10 hp!\n", 20, 1)
        used = True
    elif item == "Raw Fish":
        if room == 12:
            fancytext("You put the raw fish into the stone structure, and it gets cooked up magically!\n", 20, 1)
            fancytext("You were able to cook the fish!\n", 20, 1)
            inventory.append("Cooked Fish")
        else:
            hp += 5
            if hp > maxhp:
                fancytext("You ate the Raw Fish and your health maxed out!\n", 20, 1)
                hp = maxhp
            else:
                fancytext("You ate the Raw Fish and recovered 5 hp!\n", 20, 1)
        used = True
    elif item == "Cooked Fish":
        hp += 20
        if hp > maxhp:
            fancytext("You ate the Cooked Fish and your health maxed out!\n", 20, 1)
            hp = maxhp
        else:
            fancytext("You ate the Cooked Fish and recovered 20 hp!\n", 20, 1)
        used = True
    else:
        if bmode == True:
            if item == "Attack Ruby":
                atkmodifier += 1
                fancytext("You felt the power of the ruby, and your attack increases!\n", 20, 1)
                used = True
            elif item == "Convincing Stone":
                fancytext("You show the enemy the Convincing stone, ", 20)
                if bossy == True:
                    fancytext("but they just slam it into the ground!\n", 20, 1)
                else:
                    instaspare = True
                    fancytext("and were in awe of the stone....\n", 20, 1)
                used = True
        else:
            if item == "Gnome":
                fancytext("You smash the Gnome onto the ground, revealing that it had a key inside!\n", 20, 1)
                fancytext("You obtained the 'House Key'\n", 20, 1)
                ghostitems.append("front_key")
                keyitems.append("House Key")
                used = True
            if item == "House Key" and room == 4:
                fancytext("You unlocked the door to the house!\n", 20, 1)
                keyitems.remove("House Key")
                ghostitems.append("front_open")
                used = True
                usedup = False
            if item == "Fishing Rod" and room == 10:
                fancytext("You begin to fish in the lake...\n", 20, 1)
                for g in range(random.randrange(0,5)):
                    fancytext("...\n", 20)
                    input()
                fancytext("And catch something!\n", 20, 1)
                if random.randrange(0,5) == 4 and not "lucky_charm" in ghostitems:
                    ghostitems.append("lucky_charm")
                    keyitems.append("Lucky Charm")
                    fancytext("You got a lucky charm!\n", 20, 1)
                elif not "fish_1" in ghostitems:
                    if len(inventory) < 10:
                        ghostitems.append("fish_1")
                        inventory.append("Raw Fish")
                        fancytext("You got a bass!\n", 20, 1)
                    else:
                        fancytext("You got a bass, but you didn't have enough space in your inventory, so you let it go.\n", 20, 1)
                elif not "fish_2" in ghostitems:
                    if len(inventory) < 10:
                        ghostitems.append("fish_2")
                        inventory.append("Raw Fish")
                        fancytext("You got a carp!\n", 20, 1)
                    else:
                        fancytext("You got a carp, but you didn't have enough space in your inventory, so you let it go.\n", 20, 1)
                elif not "fish_3" in ghostitems:
                    if len(inventory) < 10:
                        ghostitems.append("fish_3")
                        inventory.append("Raw Fish")
                        fancytext("You got a salmon!\n", 20, 1)
                    else:
                        fancytext("You got a salmon, but you didn't have enough space in your inventory, so you let it go.\n", 20, 1)
                else:
                    fancytext("It was an old sock! ...You threw it back into the water.\n", 20, 1)
                usedup = False
                used = True
    
    if used == False:
        fancytext("This item cannot be used here.", 20, 1)
        usedup = False
    if usedup == True:
        if not item in keyitems:
            inventory.remove(item)
        else:
            keyitems.remove(item)
    if bmode == True:
        return [atkmodifier, defmodifier, instaspare]
        

    

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
    global team
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
        print("Your stats: hp:", hp, "attack", atk(), "defence", deff())
        print("team:", team)
    elif choice in valquit:
        fancytext("Are you sure you want to quit?", 40)
        choice = input("\n")
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
            choice = input("\n")
            if choice in inventory or choice in keyitems:
                gitemuse(choice)
            else:
                fancytext("You don't have an item called", 30)
                fancytext(choice, 30, 1)
                print()


print("Would you like to enable haste mode? (Haste mode instantly prints the text.)\n")
choice = input("\n")
if choice in valyes:
    haste = True
elif choice == "speedrun":
    print("ACTIVATING SPEEDRUN MODE!!!")
    haste = True
    speedrun = True
else:
    haste = False
if speedrun == False:
    fancytext("Do you want to skip the intro?\n", 50)
    choice = input("\n")
    fancytext("To look at the list of what you can do at any time, type in help.\n", 50, 2)
if ((not choice in valyes) or choice in valno) and speedrun == False:
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
seeroom(False, 0)


while gamenotover == True:
    choice = input("\n")
    if room == 0:
        if choice in valnorth:
            room = 1
            seeroom(False, 1, "forest")
        elif choice in vallook:
            fancytext("It's near impossible to see anything here. ", 20, 1)
            fancytext("It's all just darkness without end, like if the trees were a perfect shader.", 20, 2)
        else:
            default(choice)
        
    elif room == 1:
        if choice in valsouth:
            room = 0
            seeroom(False, 0)
        elif choice in valnorth:
            room = 2
            seeroom(True, 2, "forest")
        elif choice in vallook:
            fancytext("Now in this passageway, you can begin to see the forest more clearly, and it's beautiful in a way.", 20, 1)
            fancytext("\nAbove you, the trees are allowing the light of the night to shine through into this odd forest of purple trees.", 20, 2)
        else:
            default(choice)
    elif room == 2:
        if choice in valsouth:
            room = 1
            seeroom(True, 2, "forest")
        elif choice in valnorth:
            room = 4
            seeroom(True, 4, "forest")
        elif choice in valeast:
            room = 3
            seeroom(True, 3, "forest")
        elif choice in valwest:
            room = 9
            seeroom(True, 9, "forest")
        elif choice in vallook:
            fancytext("In this opening, you can truly appreciate the forests beauty, nearly everywhere you look there's something about it.", 20, 1)
            fancytext("\nIt fills you with hopes and dreams", 20, 2)
        else:
            default(choice)
    elif room == 3:
        if choice in valnorth:
            room = 4
            seeroom(True, 4, "forest")
        elif choice in valeast:
            room = -1
            seeroom(True, -1, "forest")
        elif choice in valwest:
            room = 2
            seeroom(True, 2, "forest")
        elif choice in vallook:
            fancytext("In this opening, you can truly appreciate the forests beauty, nearly everywhere you look there's something about it.", 20, 1)
            fancytext("\nIt fills you with hopes and dreams", 20, 2)
        else:
            default(choice)
    elif room == 4:
        if choice in valnorth:
            if "front_open" in ghostitems:
                room = 5
                seeroom(False, 5)
            else:
                fancytext("The door is locked.\n", 20, 1)
        elif choice in valsouth:
            if random.randrange(1,3) == 2:
                room = 2
                seeroom(True, 2, "forest")
            else:
                room = 3
                seeroom(True, 3, "forest")
        elif choice in valgrab:
            if not "gnome" in ghostitems:
                ghostitems.append("gnome")
                keyitems.append("Gnome")
                fancytext("You grabbed the Garden Gnome, and it was added to your ", 20)
                fancytext("Key items.\n", 10, 1)
                
        elif choice in vallook:
            if "Zoey" in team:
                fancytext("On this forestry porch, the window above illuminates the area.\n", 20, 1)
            else:
                fancytext("On this foresty porch, you can make out a cat silhouette in the window.\n", 20, 1)
            if "front_open" in ghostitems:
                fancytext("\nIt appears that the door to the house is locked, ", 20)
            if "gnome" in ghostitems:
                fancytext("with there being nothing but a ruined welcome mat on the porch.", 20, 2)
            else:
                fancytext("and there is only but a garden gnome on the porch along with a rotten welcome mat.", 20, 2)
        else:
            default(choice)
    elif room == -1:
        if choice in valwest:
            room = 3
            seeroom(True, 3, "forest")
        elif choice in valshop:
            money = shop(valyes, valquit, valhelp, ("Soft Chips", "Attack Ruby", "Soft Sword", "Pumpkin Helmet", "Convincing Stone", "Iron Sword"), money, 1)
            seeroom(False, -1, "forest")
        elif choice in vallook:
            fancytext("Here there is a shop, it appears to be ran by a living skeleton with a fez hat.\n", 20, 1)
            fancytext("behind the stand there's deep forest that seams to go on for a good long while, so it would be best to avoid it all together.\n", 20, 2)
        else:
            default(choice)
    elif room == 5:
        if choice in valsouth:
            room = 4
            seeroom(False, 4, "forest")
        if choice in valeast:
            room = 6
            seeroom(False, 6)
        elif choice in valgrab:
            if not "lr_burger" in ghostitems:
                ghostitems.append("lr_burger")
                inventory.append("Bear Burger")
                fancytext("You decided to grab what appeared to be a fresh burger from a table.", 20)
        elif choice in vallook:
            fancytext("The living room of this house appears to be filled with all sorts of trinkets and things. A real adventurer must live here.\n", 20, 1)
            fancytext("You don't know what to grab, if anything, since there just appears to be so much stuff here.", 20, 2)
        else:
            default(choice)
    elif room == 6:
        if choice in valup:
            if "up_rope" in ghostitems:
                room = 7
                seeroom(False, 7)
        elif choice in valwest:
            room = 5
            seeroom(False, 5)
        elif choice in valnorth:
            if "Zoey" in team:
                if not "catunlock" in ghostitems:
                    ghostitems.append("catunlock")
                    fancytext("'Oh, of course, hold on...'\n", 20, 1)
                    fancytext("Zoey inputs the code in for the door... and it opens!\n", 20, 1)
                room = 11
                seeroom(False, 11, "lightfor")
            else:
                fancytext("The door is locked with a combination.\n", 20, 1)
        elif choice in valgrab:
            if not "up_rope" in ghostitems:
                ghostitems.append("up_rope")
                fancytext("You grab the rope that is on the roof and pull it revealing a ladder upstairs!\n", 20)
        elif choice in vallook:
            fancytext("This coridoor leads to a few different rooms, like a bedroom, bathroom, and kitchen, however, none of which seam as interesting as a hatch that can lead upstairs.\n", 20, 1)
            if not "up_rope" in ghostitems:
                fancytext("Maybe you can open it by grabbing the rope that is dangling from it.\n", 20, 2)
            else:
                fancytext("You also notice a trans flag in the bedroom.\n", 20, 2)
                if "Zoey" in team:
                    fancytext("'Umm... Don't we have to get you home soon? Or are you just going to keep standing there?'\n", 20, 2)
        else:
            default(choice)
    elif room == 7:
        if choice in valdown:
            room = 6
            seeroom(False, 6)
        elif choice in valwest:
            room = 8
            seeroom(False, 8)
        elif choice in valgrab:
            if not "fish_rod" in ghostitems:
                ghostitems.append("fish_rod")
                keyitems.append("Fishing Rod")
                fancytext("You grabbed the only thing in reach, a fishing rod, and it was added to your Key items.", 20, 1)
        elif choice in vallook:
            if not "fish_rod" in ghostitems:
                fancytext("There are a lot of things that look to be useful here, but the only thing you could grab is a fishing rod.\n", 20, 1)
            else:
                fancytext("There are a lot of things that look to be useful here, but none of them are within reach.\n", 20, 1)
        else:
            default(choice)
    elif room == 8:
        if choice in valdown:
            fancytext("You jump out the window and get hurt badly.", 20, 1)
            hp -= 25
            killsequence(hp)
            room = 4
            seeroom(True, 4, "forest")
        elif choice in valeast:
            room = 7
            seeroom(False, 7)
        elif choice in valgrab:
            fancytext("You try and grab one of the maps, but Zoey stops you.", 20, 1)
            fancytext("Umm... No thanks..", 20, 1)
        elif choice in vallook:
            fancytext("This room appears to be full of paper that has lots of things written on them.\n", 20, 1)
            fancytext("Maps, equations, drawings, anything that could be drawn on paper was here.\n", 20, 1)
        else:
            default(choice)
    elif room == 9:
        if choice in valwest:
            room = 10
            seeroom(False, 10)
        elif choice in valeast:
            room = 2
            seeroom(False, 2, "forest")
        elif choice in vallook:
            fancytext("The forest here is less dense than any other parts you see\n", 20, 1)
            fancytext("Maps, equations, drawings, anything that could be drawn on paper was here.\n", 20, 1)
        else:
            default(choice)
    elif room == 10:
        if choice in valeast:
            room = 9
            seeroom(True, 9, "forest")
        elif choice in vallook:
            fancytext("There is a giant lake that appears to stretch out for kilometers, with few waves on the surface.\n", 20, 1)
            fancytext("It's hard to look what exactly is in the lake, but you can make out what appears to be a coin.\n", 20, 1)
        else:
            default(choice)
    elif room == 11:
        if choice in valwest:
            room = 12
            seeroom(True, 12, "lightfor")
        elif choice in valsoutht:
            room = 7
            seeroom(False, 7)
        elif choice in vallook:
            fancytext("The glowing forest lights up around you with anticipation, it's nearly hypnotising in a sense\n", 20, 1)
            fancytext("All the pretty colors fill you with kindness...\n", 20, 1)
        else:
            default(choice)
    elif room == 12:
        if choice in valwest:
            room = 13
            seeroom(True, 13, "lightfor")
        elif choice in valeast:
            room = 11
            seeroom(False, 11, "lightfor")
        elif choice in vallook:
            fancytext("There is a big stone structure containing one of these glow trees, and seams to be primed for cooking things.\n", 20, 1)
        else:
            default(choice)
    elif room == 13:
        if choice in valup:
            room = 14
            seeroom(True, 14, "lightfor")
        elif choice in valeast:
            room = 12
            seeroom(True, 12, "lightfor")
        elif choice in vallook:
            fancytext("This glowing forest seams to illuminate the ground, but the path is no longer illuminated after a point.\n", 20, 1)
        else:
            default(choice)
    elif room == 14:
        if choice in valdown:
            room = 13
            seeroom(True, 13, "lightfor")
        elif choice in valeast:
            room = 15
            repetimes = 0
            seeroom(True, 15, "lightfor")
        elif choice in vallook:
            fancytext("The path on the ground has appeared again and leads you where you need to go.\n", 20, 1)
        else:
            default(choice)
    elif room == 15:
        if choice in valwest:
            room = 14
            repetimes = 0
            seeroom(True, 14, "lightfor")
        elif choice in valeast:
            if "Lucky Charm" in keyitems:
                room = 16
                repetimes = 0
                solvedit = True
                seeroom(False, 16, "lightfor")
            else:
                repetimes += 1
                room = 15
                seeroom(True, 15, "lightfor")
                if repetimes > 3 and solvedit == False:
                    solvedit = True
                    fancytext("'Hey... Human, ", 20, 1)
                    fancytext("haven't we seen this same exact tree for 3 times?\nSurely we should've gotten to those fibers of life by now. Maybe we're just unlucky.'\n", 20, 1)
        elif choice in vallook:
            if "Lucky Charm" in keyitems:
                fancytext("There is a giant glow tree in the middle of your path and is glowing a calmful green as it's aura is faded.\n", 20, 1)
            else:
                fancytext("There is a giant glow tree in the middle of your path and is glowing a harsh purple with a menesing aura.\n", 20, 1)
        else:
            default(choice)
    elif room == 16:
        if choice in valwest:
            room = 15
            seeroom(True, 15, "lightfor")
        elif choice in valeast:
            fancytext("You are about to enter the fibers of life and be magically transported back to earth, are you sure you've done everything you have here?\n", 20, 1)
            choice = input("\n")
            
            if choice in valyes:
                if mobattle == False:
                    fancytext("You begin walking to the fibers of life, when you are suddenly stopped by a familiar face.\n", 20, 1)
                    fancytext(" It was Dr. Mo! And she had a red outfit on.\n", 20, 1)
                    fancytext("`Where do you think you're going?`\n", 20, 1)
                    fancytext("'Huh? Who are you?'\n", 20, 1)
                    fancytext("`Doctor Moriarty, and unless this student of mine is willing to work with a partner, I will not be allowing them to leave.`\n", 20, 1)
                    fancytext("'What? Is...' Zoey looks at you 'Is she how you got here?' Zoey then looks at Dr. Mo.\n", 20, 1)
                    fancytext("'Well... I'm their partner, so just let us go!'\n", 20, 1)
                    fancytext("`Oh, so you're partners? ", 20, 1)
                    fancytext("Prove it, prove to me that you are partners, and I will let you go.`\n", 20, 1)
                    fancytext("'...How will we do that?'", 20, 1)
                    fancytext("`With a battle!`", 20, 1)
                    if battle("mo") == True:
                        fancytext("`I see... You two really do make quite the team...\n", 20, 1)
                    else:
                        fancytext("`I see... You two are really strong...\n", 20, 1)
                    fancytext("I... I'm sorry we fought, I've just not been in the best mood as of late, and I got a headache.`\n", 20, 1)
                    fancytext("'Wait, so we just fought to the death because you had a headache?'\n", 20, 1)
                    fancytext("`To the death? Oh, no, the school board would have my head for that, and I would never do such a thing.\n", 20, 1)
                    fancytext("Also, this is just a text based game, this isn't really how I act.`\n", 20, 1)
                    fancytext("'...Yeah, that makes sense.'\n", 20, 1)
                    fancytext("`Now you two should get going with your partner work. There's still a lot to do.`\n", 20, 1)
                    fancytext("Dr.Mo allows you to pass.\n", 20, 1)
                    mobattle = True
                else:
                    fancytext("You begin walking to the fibers of life along with Zoey, with Dr. Mo following behind.\n", 20, 1)
                    fancytext("'Hmm... I've never really seen this world where you've come from. Do you think I'll be welcome?'\n", 20, 1)
                    choice = input("\n")
                    if choice in valyes:
                        fancytext("'Really? That's amazing! I can't wait to see all the wonderful humans you have in your world-'\n", 20, 1)
                    elif choice in valno:
                        fancytext("'...Really?\n", 20, 1)
                        fancytext("...", 20, 1)
                        fancytext("Well... I'm sure we could maybe convince them-\n", 20, 1)
                    else:
                        fancytext("'Umm.. Sorry, couldn't hear that last bit, could you maybe repeat-'\n", 20, 1)
                    fancytext("Suddenly, there was a lot of shaking\n", 20, 1)
                    fancytext("'Huh? What's going on?'\n", 20, 1)
                    fancytext("`An earthquake? I thought tectonic plates weren't in the Ether-`\n", 20, 1)
                    fancytext("The ground then burst open with a massive black dragon breaking through the ground flinging you 3.\n", 20, 1)
                    fancytext("'AAH!'\n", 20, 1)
                    fancytext("`YOU-?!`\n", 20, 1)
                    fancytext("The dragon chomped on the fibers of life and snapped them all and dragged them down back to where he came from.\nAll this also caused you 3 to also fall into the newly formed hole.\n", 20, 1)
                    fancytext("'MISSES MO, WHAT IS HAPPENINGAAAAAH-!!!'\n", 20, 1)
                    fancytext("You all fall...\n", 20, 1)
                    gamenotover = False
        elif choice in valheal:
            hp = maxhp
            fancytext("You use the healing aura of the healing shrine, and your HP was maxed out!\n", 20, 1)
        elif choice in vallook:
            fancytext("The true blight of these fibers shine for you. They're all glowing on the ends and radiating something special.\n", 20, 1)
            fancytext("These fibers also are lightly glowing everywhere else and this glow is more intense the further up they are.\n", 20, 1)
        else:
            default(choice)
fancytext("To be continued...\n", 20, 1)