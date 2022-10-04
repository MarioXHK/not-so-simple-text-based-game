import time
import random
task0 = True
task1 = True
task2 = True
task3 = True
task4 = True
tasklist = [False,False,False,False]
def TimedCheesegame(traps,didalre):
    count = 0
    tooSlow = False
    if didalre == False:
        print("Oh boy, cheese~!")
    else:
        print("Lez try again...")
    time.sleep(2)
    while count < int(traps) and tooSlow == False:#Is that a fnf reference?!?/!?/!/1/!1
        num = random.randrange(0, 10)
        TimeStart = time.perf_counter()
        print("Please press teh number", num)
        userNum = int(input())
        TimeEnd = time.perf_counter()
        if TimeEnd-TimeStart < 2 and userNum == num:
            print("Yippee")
            count += 1
        else:
            if userNum != num:
                print("AAAAAANHETRAKJLERGKJLRJHIJDSFAKSDAFKJLSDAFKJB. You hit a mouse trap!")
            else:
                print("ONGDSGHDIUGHS. The cheese now has 1000 flies on it!")
            tooSlow = True
    if tooSlow == False:
        print("Yummeh Cheez")
    time.sleep(2)
    return tooSlow
print("Welcome to amouse us")
time.sleep(2)
print("Try out this practice match,se?")
time.sleep(2)
print("Just enter de number, how ez is that?")
time.sleep(2)
while task0 == True:
    task0 = TimedCheesegame(1,False)
print("ALriathht, time for realz!")
time.sleep(2)
while task1 == True:
    task1 = TimedCheesegame(3,tasklist[0])
    if task1 == True:
        tasklist[0] = True
print("Horray, you got the first cheszzsses, now for the next on1")
time.sleep(2)
while task2 == True:
    task2 = TimedCheesegame(5,tasklist[1])
    if task2 == True:
        tasklist[1] = True
print("Next cheese comun un hott!;")
time.sleep(2)
while task3 == True:
    task3 = TimedCheesegame(7,tasklist[2])
    if task3 == True:
        tasklist[2] = True
print("her come the last chz!")
time.sleep(2)
while task4 == True:
    task4 = TimedCheesegame(10,tasklist[3])
    if task4 == True:
        tasklist[3] = True