print("Welcome to Celery, please enter your age")
age = int(input())
if age <= 13:
    print("Sorry, but you are too young to play this game.")
    print("Go play Mutant Mud instead.")
elif age > 13 and age < 18:
    print("You are technically old enough to play, but the sensory overload mode will be turned off.")
    print("If you want it to turn on, please ask your parent or guardian.")
elif age == 42:
    print("I'm sorry, but you are simply too skilled to play Celery")
    print("Please play the guy instead, as if you play Celery with all it's young players, you will absolutely destroy those people.")
elif age > 42:
    print("Welcome to Celery. Would you like to play in retro mode or regular mode?")
    style = input()
    if style == "retro":
        print("Now loading retro Celery")
        print("CELERY")
    else:
        print("Now loading Celery")
        print("🥬")
else:
    print("Welcome to Celery")
    print("🥬")