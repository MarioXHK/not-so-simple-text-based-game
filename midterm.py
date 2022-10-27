def grizzco(numo,nump,nom):
    return float(numo*nump*nom)
def rootbeer(ex):
    if not int(ex) <= 1:
        print(ex, "bottles of age appropriate beverage on the wall...")
    else:
        if int(ex) == 1:
            print("1 bottle of age appropriate beverage on the wall...")
        else:
            print(ex, "bottles of age appropriate beverage on the wall...")
        print("Nanana nanana nananana nananananana!")
        return
    rootbeer(ex-1)
    
print("I uh... see you've been playing cookie clicker.")
print("Might I just ask: How many cookies to do you have?")
cookies = int(input())
if cookies < 3:
    print("Really? Well, I don't think that's enough.")
elif cookies >= 3 and cookies <= 10:
    print("Hmm, alright. That's a good amount of cookies.")
elif cookies > 10:
    print("That's a bit much don't you think? You just have too many cookies and you're not sharing!")
print("Anyways, star wars is a thing. Are you a jedi or a sith")
starside = input()
if starside == "jedi" or starside == "Jedi":
    print("Well here's a green lightsaber for you.")
if starside == "sith" or starside == "Sith":
    print("Well then here's a red lightsaber (that has 100 other light sabers in it like every other)")
else:
    print("Hmm... here's a baguette. Do whatever you want with it.")
for i in range(2,42,2):
    print(i, end = " ")
print()
for i in range(100,44,-10):
    print(i, end = " ")
print()
knock = "shampoo without the sham"
while knock != "orange" and knock != "Orange":
    print("Knock knock, who's there?")
    knock = input()
    if knock == "orange" or knock == "Orange":
        print("Orange you glad I didn't say banana?!")
    else:
        print("Banana!")
print(grizzco(2,3,4))
print("Enter a number")
rooting = int(input())
rootbeer(rooting)