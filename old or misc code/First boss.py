bonkus = False
import time
bonktimes = 0
print("That's it! I'm using 0.1% of my power!")
time.sleep(2)
print("R")
for x in range (10):
    time.sleep(0.05)
    print("A")
time.sleep(0.05)
print("W")
time.sleep(0.1)
print("!")
time.sleep(2)
print("Now before I beat you to dust, I'd like to know, what's your power level?")
time.sleep(2)
print("Don't say something not a number, that'll destroy you instantly.")
powerlevel = int(input())
if powerlevel < 100:
    print("HA! you don't stand a chance against me, fool!")
    print("I don't even need to use my power to defeat you! I'll just use my baseball bat!")
    while bonkus == False:
        bonktimes += 1
        print("BONK!")
        if bonktimes == 10:
            print("You are no match to me!")
        if bonktimes == 20:
            print("Ready to give up?")
        if bonktimes == 30:
            print("You're holding on still? Well, I was going a bit easy on you!")
        if bonktimes == 40:
            print("Enough talk, time to perish!")
        letterinput = input()
        if letterinput == "q" or letterinput == "Q":
            bonkus = True
    print("NO! Get back here!")
    time.sleep(2)
    print("Grr, I'll get you!")