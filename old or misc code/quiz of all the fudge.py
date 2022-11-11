apoints = 0
bpoints = 0
cpoints = 0
dpoints = 0
epoints = 0
def surveyquestion(numquest, question, optiona, optionb, optionc, optiond):
    global apoints
    global bpoints
    global cpoints
    global dpoints
    global epoints
    print("Question ", numquest, question)
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
    if youanswer == "a" or youanswer == "A":
        apoints += 1
    elif youanswer == "b" or youanswer == "B":
        bpoints += 1
    elif youanswer == "c" or youanswer == "C":
        cpoints += 1
    elif youanswer == "d" or youanswer == "D":
        dpoints += 1
    else:
        epoints += 1

print("Welcome to the quiz survey of all the fudge!")
print("This will test weather you are a fudge, a circle, a fish, or a tree!")
print("Are you ready?")
print("Are any of us truly ready?")
print("Because really- oh I got too trhhtdhszfhdzdgerhauyvsuyahrgksfda")
surveyquestion("A", "What brand of sponge do you buy?", "Bob", "Silicon", "Natural", "Square")
surveyquestion("2", "WHAT do you water your palnts wint?", "Nothing", "Milk", "Water", "Thick Water")
surveyquestion("3", "DO you recyclee?", "True", "Milk", "No", "SSSSSSSSSS")
surveyquestion("5", "What's 9+10?", "675", "19", "4736", "21")
surveyquestion("7", "What game is the legend of zelda?", "THe zleda", "Linkblocked", "Flowers", "Smashing pots")
surveyquestion("6", "Do you super smash min who?", "Sonic", "MAro", "Spongebob", "Villager")
surveyquestion("4", "How many pieces heart?", "0", "1", "2", "3")
surveyquestion("8", "8", "8", "8", "8", "8")
surveyquestion("Who makes your phone wring?", "Who makes your phone ring?", "The police", "Abmalance", "Fure", "Ink")
surveyquestion("100", "How do you light a fire?", "Medication", "Flint and steel", "bean lazy", "A massive log of wood")
print("ocn u got ane?D yYou dot go the end!")
print("Now calculating IklliKliKlKILKilK!")
listig = [apoints,bpoints,cpoints,dpoints,epoints]
if max(listig) == apoints:
    print("You are a Fudge!")
    print("Your favorite activities include ripping paper apart and eating out of the trash.")
    print("You are an extremely skilled conductor of electricity and with a little more training, you are a god")
    print("You get to be3 the thnwayse on quz/..!")
elif max(listig) == bpoints:
    print("You are a Circle!")
    print("You are obsessed with robox.")
    print("You love the pi and pie and pie nad tpi e a math.pe e ae  apie kapoeai aea aa")
    print("your circle fence is 100.")
elif max(listig) == cpoints:
    print("You are a Fish!")
    print("Lzyalazy. LYou oare aalzy sloth.")
    print("Good for you! YOu cant cna oyn!")
    print("After all, ebcasue you ae asoloth, yiu ge to rul,l as uasll")
elif max(listig) == dpoints:
    print("You are a Tree!\nAll your code will be put into compressed stuff and stored efficiently.\nHowever side effects include morning self, lightbulbs in the eyes, and kcat ears.\nSO beaanss benas furty furry.")
elif max(listig) == epoints:
    print("You are a !")
    print("You don't feel so good today and the entire universe is falling apart around you.")
    print("Luckily, you have something the others don't have!")
    print("a")
else:
    print("Oh poopsy whoopsy we did a lil fudgy wudgy! Xwx")