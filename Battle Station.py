import random
print("Welcome to a superflat world")
def BattleSystem(monsterType, playerHealth):
    if monsterType == "Creeper":
        monsterHealth = 10
        print("A creeper attacks! (Aww man!)")
    elif monsterType == "Skeleton":
        monsterHealth = 15
        print("A skeleton attacks!")
    
    while monsterHealth > 0 and playerHealth > 0:
        if monsterType == "Creeper":
            monsterAttack = random.randrange(20,30)
        elif monsterType == "Skeleton":
            monsterAttack = random.randrange(10,25)
        print("The", monsterType, "attacks for", monsterAttack)
        playerHealth= playerHealth-monsterAttack
        print("Your health is now", playerHealth)
        input()
        playerAttack = random.randrange(3,5)
        print("You attack for",  playerAttack)
        monsterHealth= monsterHealth-playerAttack
        print("The monster's health is now", monsterHealth)
    if monsterHealth < 0:
        print("u win")
    else:
        print("u died")
BattleSystem("Creeper",69)