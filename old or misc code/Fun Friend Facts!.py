print("Cool facts about your friends!")
truemeaning = False
import time
fred = False
aurthur = False
gale = False
tam = False
callie = False
while truemeaning == False:
    print("Friend list: Fredrick, Arthur, Gale, Tam, Callie")
    print("Tell me the name of a friend you want to know the information about!")
    friendname = input()
    if friendname == "Fredrick":
        fred = True
        print("Fredrick is the most chaotic one of your friends,")
        time.sleep(2)
        print("with his frequentness in dabling in craziness, he's never pradictable!")
        time.sleep(2)
        print("He works as a voice actor for Nickelodeon.")
    if friendname == "Arthur":
        aurthur = True
        print("Arthur is a big reader and writer. He's written many books in the past!")
        time.sleep(2)
        print("His way with words and creativity make an unstoppable force that really blow readers away.")
        time.sleep(2)
        print("He sometimes leaves his window open for a small breese to come in,")
        time.sleep(2)
        print("and easy access into his home.")
    if friendname == "Gale":
        gale = True
        print("Gale is a bit old, but nobody minds her still being around.")
        time.sleep(2)
        print("She drives a bus around for work, transporting people from place to place.")
        time.sleep(2)
        print("Despite this, she still drives a car to actually get to her work.")
        time.sleep(2)
        print("Her brakes are fragile.")
    if friendname == "Tam":
        tam = True
        print("Tam is a big fan of the pokemon francize.")
        time.sleep(2)
        print("They've gotten every pokemon in every game.")
        time.sleep(2)
        print("They're so distracted from pokemon that they haven't even notice their door is unlocked.")
        time.sleep(2)
        print("It's too late anyways.")
    if friendname == "Callie":
        callie = True
        print("Callie was pretty smart sometimes, having the highest grade of your class")
        time.sleep(2)
        print("They live a few blocks from you, but you're still friends")
        time.sleep(2)
        print("Their IP address is 163.54.127.23")
    if fred == True and aurthur == True and gale == True and tam == True and callie == True:
        truemeaning = True
    time.sleep(3)

print("...")
time.sleep(3)
print("Why don't we talk about some facts about you?")
input()
print("Good!")
time.sleep(3)
print("You left your outside basement door open.")
time.sleep(3)
print("There is a hidden door to your basement that was painted over by the house's previous owner.")
time.sleep(4)
print("It's open")
time.sleep(3)
print("Your closet smells like lightweight soap.")
time.sleep(5)
print("You haven't washed the back of your hair in awhile.")
time.sleep(6)
print("Alright that's enough fun friend facts for today!")
time.sleep(2)
print("See you soon :D")