def racecar(tacocat):
    palen = 0
    forbidchars = {",",".",":","'",";"}
    radar = []
    eve = "".join(tacocat.split())
    print(eve)
    for h in eve:
        if not (h in forbidchars):
            radar.append(h)
    eve = "".join(radar)
    print(radar)
    print(eve)
    for i in range(len(eve)):
        if eve[i] == eve[len(eve)-i-1]:
            palen += 1
    if palen == len(eve):
        print(tacocat, "is a palindrome")
        return True
    else:
        print(tacocat, "isn't a palindrome")
        return False
racecar("hello")
racecar("tacocat")
racecar("megaman")
racecar("racecar")
racecar("sin on your mother's mouth")
racecar("step on no pets")
racecar("you are too loot erau, oy")
racecar("i got carried away")
racecar("alright, we get it.")
racecar("do geese see god")
racecar("pull up if i pull up")
racecar("on a clover, if alive, erupts a vast, pure evil; a fire volcano")