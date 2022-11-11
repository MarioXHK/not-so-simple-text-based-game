print("Pardon, but how much money do you have?")
money = float(input())
if money < 50:
    print("I see. How about I buy lunch for you?")
elif money >= 50 and money <= 100:
    print("Well would you like to join me for lunch")
else:
    print("Could you buy me lunch?")