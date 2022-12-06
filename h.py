mon = 1500
inventory = []
def shop(coin):
    global inventory
    print("--------------------------------------------------")
    print("welcome to the shop inside the static void")
    while True:
        print("you have", coin, "coins")
        print("Your items:", end = " ")
        for i in inventory:
            print(i, end = "  ")
        print("\nShop items: Potions: $5, Food: $3, Keys: $10, q    : $9999")
        inpee = input("Press p to purchase a potion, f for food, k for key, and q to quit:")
        if inpee == "p":
            if coin >= 5:
                print("You got a potion")
                coin -= 5
                inventory.append("potion")
            else:
                print("You don't have enough money")
        if inpee == "f":
            if coin >= 3:
                print("You got food")
                coin -= 3
                inventory.append("food")
            else:
                print("You don't have enough money")
        if inpee == "k":
            if coin >= 10:
                print("You got a key")
                coin -= 10
                inventory.append("key")
            else:
                print("You don't have enough money")
        if inpee == "q":
            if coin >= 9999:
                print("Finally")
                inventory.append("q        ")
                exit()
            else:
                return coin
shop(mon)
