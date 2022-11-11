import random
def trickortreat():
    global thewhat
    addition = random.randrange(1, 5)
    randee = random.randrange(0, 100)
    if randee < 15:
        addtoo = 0
    elif randee < 35:
        addtoo = 1
    elif randee < 70:
        addtoo = 2
    elif randee < 80:
        addtoo = 3
    elif randee < 98:
        addtoo = 4
    else:
        addtoo = 5
    thewhat[addtoo] += addition
    if addtoo == 0:
        if addition == 1:
            print("You got a butterfinger bar!")
        else:
            print("You got", addition, "butterfinger bars!")
    elif addtoo == 1:
        if addition == 1:
            print("You got a Hershey Bar!")
        else:
            print("You got", addition, "Hershey Bars!")
    elif addtoo == 2:
        if addition == 1:
            print("You got a Peanutbutter Cup!")
        else:
            print("You got", addition, "Peanutbutter Cups!")
    elif addtoo == 3:
        if addition == 1:
            print("You got a M&M!")
        else:
            print("You got", addition, "M&Ms!")
    elif addtoo == 4:
        if addition == 1:
            print("You got a Sour Patch Kid!")
        else:
            print("You got", addition, "Sour Patch Kids!")
    elif addtoo == 5:
        if addition == 1:
            print("You got A ROCK!!!")
        else:
            print("You got", addition, "ROCKS!!!")

thewhat = [0,0,0,0,0,0]
for i in range(5):
    trickortreat()
print("Your final candies are:", thewhat)