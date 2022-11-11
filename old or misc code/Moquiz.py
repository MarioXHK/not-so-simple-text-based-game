points = 0
import time
def fancytext(texty, spext, waig):
    divzex = 1/int(spext)
    for i in range(len(texty)):
        print(texty[i], end = "")
        if texty[i] == ",":
            time.sleep(divzex*1.5)
        if texty[i] == ",":
            time.sleep(divzex*3)
        if texty[i] == "." or texty[i] == "?" or texty[i] == "!":
            time.sleep(divzex*6)
        time.sleep(divzex)
    time.sleep(int(waig))
def quizquestion(numquest, question, optiona, optionb, optionc, optiond, answer):
    global points
    fancytext(("Question ", numquest), 20, 1)
    print(end = " ")
    fancytext(question, 20, 0.5)
    print()
    print("a:", optiona, end = " ")
    if len(optiona) > 20 or len(optionb) > 20:
        print()
    print("b:", optionb, end = " ")
    if len(optionb) > 20 or len(optionc) > 20:
        print()
    print("c:", optionc, end = " ")
    if len(optionc) > 20 or len(optiond) > 20:
        print()
    print("d:", optiond)
    youanswer = input()
    if youanswer == answer:
        points += 1
fancytext("Henlo and welcome to the [yes] quiz! Where we see just how much you are a student of Dr. Mo!\n", 20, 2)
fancytext("Please enter your answers in a single letter lowercase format, otherwise your answers will be counted as ", 20, 0)
fancytext("[REDACTED]!\n", 1000, 2)
fancytext("Ready? Let z", 20, 0)
fancytext(" gOOISOIFDDSHFIODAKLHSDFKOASHDKJF", 100, 2)
print()
quizquestion("1", "How do you call the teacher's name correctly?", "Ms. Mo", "Mr. Mo", "Dr. Mo", "Mo", "c")
quizquestion("2", "Which one of these sticky note colors is NOT in Dr. Mo's classroom?", "Magenta", "White", "Orange", "Blue", "b")
quizquestion("3", "What are those little shining string-like things that hang off the ceiling?", "Fiber Optic Cables", "Wired LEDs", "Magical light forest tendrils", "Microreflection Strings", "a")
quizquestion("4", "On one of the backroom doors, there's a video game poster, which video game is it for?", "The Legend of Zelda", "Pokemon", "Super Mario", "Among Us", "d")
quizquestion("5", "What is Mo short for?", "Monroe", "Moriarty", "Momo", "Molly", "b")
quizquestion("6", "The status of the piano as of the time of this quiz being created?", "Completely broken.", "It's legs are nonfunctional and out of tune.", "Just out of tune.", "It's entirely fine.", "c")
quizquestion("7", "How often does Dr. Moe change the Schoology picture?", "Every month", "Every week", "Every day", "She doesn't change it", "b")
quizquestion("8", "Where did the pokemon Balloon originate from?", "It was a bd gift from amother student", "It appeared out of thin air", "The previous teacher left it in Dr. Mo's classroom", "Dr. Mo bought it", "a")
quizquestion("9", "What is the rule about late work?", "There's a penalty for it being late", "There is no penalty, just pokes", "Dr. Mo will give you -2436 points in the grade book", "You can't turn in late work, you have to do make up work", "b")
quizquestion("10", "How many colors can the trees around the room display? (not counting the flashing/fading colors!)", "3", "4", "6", "7", "d")
quizquestion("11", "What is Elif?", "A combination of an Else and If", "Something in code used to determine random numbers", "Dr. Mo's first name", "A computer part", "a")
quizquestion("12", "Which of the following is NOT a reason why it's very difficult to build a working PC using the parts in the backrooms?", "Where you put the CPU on the motherboard is usually screwed up.", "Most of the parts can't fit together", "Some of the parts got tainted with the lead water", "There aren't enough working parts", "c")
quizquestion("13", "How many hanging stars are there in the room?", "none", "1", "2", "3", "c")
quizquestion("14", "What is used to get proper shapes to display in python?", "for loops", "Pygame", "Elif", "Obelisc", "b")
quizquestion("15", "What is the final for 1st Semester Students?", "Making pong", "Making a TI calculator", "Making a text based game", "Re-creating the offline dino game", "c")
quizquestion("16", "Which console isn't avalable in the backrooms?", "OG Xbox", "PS2", "Oculus", "Dreamcast", "d")
quizquestion("17", "What is the activity on the first friday?", "Crab Tag", "Squid Games", "Fort Day", "Freeze Tag", "c")
quizquestion("18", "What game poster isn't in the classroom?", "Halo", "Batman", "Read Dead Redemption", "Kirby", "d")
quizquestion("19", "How long do breaks last>", "15 minutes", "10 minutes", "20 minutes", "30 minutes", "a")
quizquestion("20", "What allows kids to access video games in this class?", "A special network", "Admin permissions", "Students hacking the network", "They can't", "a")
fancytext("Finished!\n", 20, 1)
fancytext("CALclat stoces?\n", 20, 2)
fancytext("Hmmm, lez si.\n", 10, 2)
if points == 0:
    fancytext("Man you suck at this ngl.\n", 20, 2)
    fancytext("You got not a SINGLE question right.\n", 20, 2)
    fancytext("I mean at least guessing should've gotten you somewhere, but I guess not.\n", 20, 2)
    fancytext("Are you even in this class?\n", 20, 2)
    fancytext("Any2ways i' gonna steal your IP now.\n", 20, 2)
    fancytext("Gooby.\n", 20, 3)
elif points < 5:
    fancytext("Man you suck.\n", 20, 2)
    fancytext("You got some questions right, but not really anything else.\n", 20, 2)
    fancytext("You did your best is all that matters tho, even tho u did kinda pghogrjgfosihfdsoighfdiusoxokcx it.\n", 20, 4)
elif points < 10:
    fancytext("Alright, you got some of the ropes, I guess, but you still have a long way to go.\n", 20, 2)
    fancytext("Not bad...but not good...still not bad.\n", 20, 2)
    fancytext("I'm gonna stop saying stuff before I get pummled for bullying someone.\n", 20, 2)
elif points < 14:
    fancytext("Huh... pretty good.\n", 20, 2)
    fancytext("Y'know this test will probably go expired in some time, but what matters is...", 20, 1)
    fancytext("Cheese.\n", 10, 2)
    fancytext("And of course that you learned something.\n", 20, 2)
    fancytext("Wait, no. You can't. You can't see if you got any of the questions right or not, just your final score.\n", 20, 4)
elif points < 17:
    fancytext("You're pretty good at this...\n", 20, 2)
    fancytext("Too good per chance, as ", 20, 2)
    fancytext("THERE CAN BE ONLY ONE!\n", 5, 2)
    fancytext("...\n", 5, 2)
    fancytext("Kidding!\n", 20, 2)
    fancytext("I'm just a pre-written script! I have no feelings for this!\n", 20, 3)
elif points < 20:
    fancytext("Congradulations, you're good enough to count as a kid of DR MOESESESERASR", 20, 2)
    fancytext("Or you probably did count a few points back.\n", 20, 2)
    fancytext("Do I have to hyperanilize you in order to get this credit?\n", 20, 2)
    fancytext("Because oh boy, I'm screwed if I have to..\n", 20, 3)
elif points == 20:
    fancytext("Yippee! Perfect score!\n", 20, 2)
    fancytext("You now know as much as the first simester student writting this!\n", 20, 2)
    fancytext("Now considering this guy just started this class and there are some PSPESESLLLING erorors here and there, that probably isn't much.\n", 20, 2)
    fancytext("Eh, what are ya gonna do?\n", 20, 3)
else:
    fancytext("...\n", 20, 2)
    fancytext("How did you get here?\n", 20, 2)
    fancytext("I think something's broken...\n", 20, 2)
print("You got", points, "out of 20 questions right.")