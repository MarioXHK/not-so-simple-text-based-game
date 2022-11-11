print("Hey! Would you like to see a joke?")
jokeye = input()
whileast = False
guesser = False
whywhy = False
if ((jokeye == "Yes" or jokeye == "yes") or (jokeye == "Sure" or jokeye == "sure")) or ((jokeye == "Fine" or jokeye == "fine") or (jokeye == "Maybe" or jokeye == "maybe")):
    whileast = True
else:
    while whileast == False:
        print("Please?")
        jokeye = input()
        if ((jokeye == "Yes" or jokeye == "yes") or (jokeye == "Sure" or jokeye == "sure")) or ((jokeye == "Fine" or jokeye == "fine") or (jokeye == "Maybe" or jokeye == "maybe")):
            whileast = True
quity = False
print("Great!")
while quity == False:
    print("Knock knock!")
    whotf = input()
    if (whotf == "Quit" or whotf == "quit") or (whotf == "Q" or whotf == "q"):
        print("Alright fine! I'll quit!")
        quity = True
    else:
        print("Another knock knock joke!")
print("How about the guessing game?")
print("I'm thinking of a number between 1 and 10!")
while guesser == False:
    num = int(input())
    if num == 3:
        guesser = True
        print("Good job, you got it!")
    else:
        print("Not quite...")
print("Now I'm thinking of a number between 1 in 1000000")
while whywhy == False:
    whytf = input()
    if ((whytf == "Quit" or whytf == "quit") or (whytf == "Q" or whytf == "q")) or whytf == "687802":
        whywhy = True
        if whotf == "687802":
            print("Wow! you really did get it!")
        else:
            print("Alright that was a bit unfait tbh.")
    else:
        print("Nope!")
print("Well, that was fun! Goodbye now!")
