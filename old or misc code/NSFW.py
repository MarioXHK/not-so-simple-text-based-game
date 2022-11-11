print("WARNING: You are about to enter a NSFW site, please enter your age to continue.")
age = int(input())

if age >= 18:
    print("Alright, welcome to https://cats.com")
    print(" ∧,,,∧")
    print("( ̳• · •̳)")
    print("/    づ♡ I love you")
else:
    print("Sorry, but you are not old enough to access this website")
    print("Please wait", (18-age), "years before entering.")
    if age < 13:
        print("Go play fortnite or whatever you kids do these days.")
    else:
        print("Go play Minecraft.")