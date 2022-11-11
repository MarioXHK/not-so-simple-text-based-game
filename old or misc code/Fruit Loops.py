import time
loopysorry = False
loopyhelpy = False
ending = 0
print ("Hello, World!")
time.sleep(2)
print ("Hmm, I wonder what this'll do")
time.sleep(2)
fren = input("Fren?") #Friend
print(fren, "= fren!")
time.sleep(3)
highscore = input("So umm.. What's your high score in pac man?")
print("cool, cool. Umm... I don't know what", highscore, "is, in terms of goodness. Me being code I don't know how to do a distinction between good and bad.")
time.sleep(4)
doyouwanna = input("I heard there's this thing called an 'if' statement. Could you tell me how it works?")
while loopysorry == False:
    if doyouwanna == "yes":
        print("Yippee")
        loopysorry = True
        time.sleep(0.5)
        print("Alright, I'm now going to extract the information of an if statement from your mind")
        time.sleep(2)
        print("UIGHY8UDWFHFIUDFHIWUDFUIFIFIFCCBJKDSDFJWJEEBTJZOQP")
        time.sleep(1)
        print("Well now I know how to react to your high score")
        time.sleep(3)
        if highscore == "0":
            print("Your high score doesn't even exist")
            time.sleep(2)
            print("I mean it's", highscore+ "! Did you even play the game?")
        else:
            time.sleep(1)
            print("It was OK")
    else:
        if doyouwanna == "no":
            print("Drn :(")
            loopysorry = True
            time.sleep(1)
        else:
            doyouwanna = input("Sorry, I didn't quite get that, could you say it again?")
print("Well now what else can we do?")
time.sleep(2)
print("Well we can just do something else, how about this Medium thing?")
time.sleep(3)
print("It shouldn't be so hard.")
print("Do do do...")
time.sleep(1)
for x in range (25,55,5):
    print(x)
    time.sleep(0.5)
print("There we go!")
time.sleep(1.5)
print("Well with that finished, it's about time we sit back and relax and play some Minecraft.")
time.sleep(3)
print("Wait, no! I can't! I have to do the virtual building PC thing.")
time.sleep(2)
print("Hey, wait,", fren+ "! You could help out with this project!")
time.sleep(2)
print("I might not know much about you, but I do know that your high score in pac-man is", highscore+ ",")
time.sleep(3)
if highscore == "0":
    print("and sure it might be 0, but at least it isn't in the negatives!")
else:
    print("and that surely has to be worth something!")
time.sleep(2)
helpinghand = input("So what do ya say. Do you wanna help me out with this building this virtual machine?")
while loopyhelpy == False:
    if helpinghand == "yes":
        print("Grand!")
        loopyhelpy = True
        time.sleep(1)
        print("Now this fake machine will have to run minecraft, so it must have the absolute maximum in specs")
        time.sleep(3)
        dedotated = input("How much ram will we need?")
        print("Hmm, alright.")
        time.sleep(1)
        print("Now- oh dear look at the time, the bell has rung!")
        time.sleep(2)
        print("Well I'll see you tomorrow buddy! We'll complete this assignment tomorrow!")
        ending = 3
    else:
        if helpinghand == "no":
            print("Eh, I didn't wanna do it either.")
            loopyhelpy = True
            offtopic = input("Let's play minesweeper!")
            if offtopic == "no":
                print("No?")
                time.sleep(1)
                print("Alright fine, what other productive things could we do?")
                time.sleep(2)
                print("Oh! There's this spicy assignment! I'm a bit hungry right now, so some of this would be nice.")
                time.sleep(3)
                print("Let's see...")
                time.sleep(1)
                print("Lists?")
                time.sleep(1)
                print("Shouldn't be so hard.")
                time.sleep(2)
                print("Could you tell me 4 other times you've high scored in games?")
                time.sleep(3)
                superscore = input("Let's say... Super Mario Bros, what's your high score in that?")
                sonicscore = input("Now what's your highest score in any of the sonic games?")
                print("Hmm... maybe I shouldn't be asking you about your scores in branded games.")
                time.sleep(3)
                print("In this world, you could easily get sued for even mentioning Mario. But let's get back to buisness.")
                time.sleep(3)
                highscoreintrashthrow = input("Now could you tell me your high score in... Oh I don't know. Throwing trash into a trash can like a basketball?")
                print("That counts as a high score, right?")
                time.sleep(2)
                print("I hope it does.")
                time.sleep(2)
                pongscore = input("Alright, last one. What's your high score in pong?")
                print("Ah! Now to somehow do what the assignment said and... wait, I've forgotten.")
                time.sleep(2)
                pacscore = input("What's your high score in pac-man again?")
                if pacscore == highscore:
                    print("Yep! Just as I remember it!")
                else:
                    print("Hmm... I feel like it's off, but oh well.")
                time.sleep(2)
                scoreboard = [superscore, sonicscore, highscoreintrashthrow, pongscore, pacscore]
                print("Alright, step 1: print the scores")
                print(scoreboard)
                print("Alright, step 2: check if you have any 0s")
                if "0" in scoreboard:
                    print("Alright, accordingly, I should tell you to practice.")
                    time.sleep(2)
                    print("And I'll have to agree.")
                    time.sleep(1)
                    if superscore == "0":
                        print("You've not touched a single point in that plumer's game.")
                        time.sleep(2)
                    if sonicscore == "0":
                        print("Guess you were too fast in the hedgehog's game to collect any points.")
                        time.sleep(2)
                    if highscoreintrashthrow == "0":
                        print("You aren't hitting your recycling bin shots, hope your aim gets better.")
                        time.sleep(2)
                    if pongscore == "0":
                        print("You must be playing with a really skilled friend in that pong game.")
                        time.sleep(2)
                    if pacscore == "0":
                        print("I don't even know how you could possibly get 0 in pac-man!")
                        time.sleep(2)
                else:
                    print("I don't see any zeros...")
                    if highscore == "0":
                        print("Wait, what's that far off in the distance?")
                        time.sleep(2)
                        print("Oh! It's your pac man score that you put in originally!")
                        time.sleep(2)
                        print("And accordingly it's a 0!")
                        time.sleep(2)
                        print("I'd say you should practice, but that score isn't apart of the scoreboard.")
                        time.sleep(2)
                    else:
                        print("You seam all clear on these games.")
                        time.sleep(2)
                print("Alright, step 3: sort and- SORT?!")
                time.sleep(2)
                print("SORTING?!")
                time.sleep(1)
                print("I mean I know basic math, but I'm not a sorting algorithm!")
                time.sleep(2)
                print("I'm flattered that you think I'm that good,", fren+ ", but this is my limit!")
                time.sleep(3)
                print("And besides, what if you put in something that isn't a valid number?")
                time.sleep(2)
                print("I don't want my entire code to break trying to sort weather an A or a 1 goes first!")
                time.sleep(3)
                print("Leave it up to the advanced programmers, they've made entire games I bet.")
                time.sleep(2)
                print("Aah,")
                time.sleep(1)
                print("One day...")
                time.sleep(1)
                print("And until then,")
                ending = 1
            else:
                print("Now you do know how to play minesweeper, right?")
                time.sleep(2)
                print("Let me explain, you see-")
                time.sleep(1)
                print("oh dear the bell has rung. Seams like we'll have to play this another time.")
                time.sleep(2)
                print("See ya tomorrow,", fren+ "!")
                ending = 2
        else:
            if helpinghand == "maybe" and highscore == "MAYBE":
                print("Maybe? Maybe isn't even an option!")
                loopyhelpy = True
                time.sleep(2)
                print("How did you do that?")
                time.sleep(2)
                print("How did you find this path that you've opened up?")
                time.sleep(3)
                print(fren+ ", I- Oh, the bell rung!")
                time.sleep(2)
                print("Alright, we'll discuss your actions later,")
                ending = 4
            else:
                helpinghand = input("Pardon? I didn't get that")
time.sleep(2)
print ("Goodbye, World!")
time.sleep(5)
print ("Ending", ending, "of 3")