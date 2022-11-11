import time
import winsound
import math
import easygui
goodending = False
print("I'm a calculator!")
dividezero = False
while dividezero == False:
    numone = float(input("Enter first number."))
    numthi = "cock"
    while not (numthi == "a" or numthi == "b" or numthi == "c" or numthi == "d" or numthi == "e" or numthi == "f" or numthi == "g" or numthi == "h" or numthi == "i" or numthi == "j" or numthi == "q"):
        numthi = input("press a for adding, b for subtracting, c for multiplying, or d for dividing, e for square rooting, f for powering, g for sining, h for cosing, i for taning, j for finding the average of the 2, and q to quit.")
    if not (numthi == "e" or numthi == "g" or numthi == "h" or numthi == "i" or numthi == "q"):
        numtwo = float(input("Enter second number."))
    if numthi == "a":
        print (numone, "plus", numtwo, "equals", (numone + numtwo))
        winsound.Beep(100,100)
    if numthi == "b":
        print (numone, "minus", numtwo, "equals", (numone - numtwo))
        winsound.Beep(200,100)
    if numthi == "c":
        print (numone, "multiplied by", numtwo, "equals", (numone * numtwo))
        winsound.Beep(150,100)
    if numthi == "d":
        if numtwo == 0:
            print("WARNING: You are about to divide by 0 and possibly destroy all of reality")
            proceed = input("Proceed?")
            if proceed == "Yes":
                dividezero = True
                print("Dividing", numone, "by", numtwo)
                
        else:
            print (numone, "divided by", numtwo, "equals", (numone / numtwo))
            winsound.Beep(50,100)
    if numthi == "e":
        if numone < 0:
            print("WARNING: You are about to square root a negative number and possibly destroy all of reality")
            proceed = input("Proceed?")
            if proceed == "Yes":
                dividezero = True
                print("Square rooting", numone)
        else:
            print ("The square root of", numone, "is", (math.sqrt(numone)))
            winsound.Beep(250,100)
    if numthi == "f":
        print (numone, "to the power of", numtwo, "equals", (math.pow(numone,numtwo)))
        winsound.Beep(300,100)
    if numthi == "g":
        print ("the sin of", numone, "is", (math.sin(numone)))
        winsound.Beep(400,100)
    if numthi == "h":
        print ("the tan of", numone, "is", (math.cos(numone)))
        winsound.Beep(500,100)
    if numthi == "i":
        print ("the tan of", numone, "is", (math.tan(numone)))
        winsound.Beep(350,100)
    if numthi == "j":
        print ("the average of", numone, "and", numtwo, "is", ((numone+numtwo)/2))
        winsound.Beep(450,100)
    if numthi == "q":
        winsound.Beep(550,100)
        easygui.msgbox("Gooby!", title="Not an explosion")
        dividezero = True
        goodending = True
if goodending == False:
    winsound.Beep(250,2000)
    print("ERROR! ERROR!")
    winsound.Beep(500,1000)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    winsound.Beep(1000,1000)
    easygui.msgbox(".", title="Explosion")
    time.sleep(0.2)
    easygui.msgbox("o", title="Explosion")
    time.sleep(0.2)
    easygui.msgbox("O", title="Explosion")
    time.sleep(0.2)
    easygui.msgbox("( )", title="Explosion")
    time.sleep(0.2)
    easygui.msgbox(" __ \n(  )\n ~~ ", title="Explosion")
    time.sleep(0.2)
    easygui.msgbox(" ~~ \n~  ~\n ~~ ", title="Explosion")