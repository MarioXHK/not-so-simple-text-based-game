import time
print("This is a story about a man named Stanley")
time.sleep(2)
doExit = False
while doExit == False:
    letterpress = input("Stanley pressed the ")
    print("button.")
    time.sleep(2)
    if letterpress == "q":
        doExit = True
    else:
        print("Then after pressing the", letterpress, "button,")
print("And then the floor below him suddenly opened up and he fell to his demise.")
time.sleep(2)
print("My heavens, all for pressing the letter", letterpress+ "?")
time.sleep(2)
print("Luckily, Stanley had the Aperture Science long fall boots equiped, so he didn't actually die.")
time.sleep(3)
print("Instead, he was sent to a strange facility where he was given a strange device that shot portal holes.")
time.sleep(3)
print("Stanley had a bad feeling for what was coming next.")