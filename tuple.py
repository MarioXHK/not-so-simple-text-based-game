tupperbox = ("Steve", "Alex", "The number 23", "Tommy", "Ben", "Lewis", "Simon")
spiderbox = ("Noelle", "The you", "Among", "Sand", "Sjin", "The number 24") #enemies
tupperage = []
print("Frens are", tupperbox)
for i in tupperbox:
    print("Pls enter the age of ur fren", i)
    tupperage.append(int(input()))
sumee = 0
for j in range(len(tupperbox)):
    print("Age of fren", tupperbox[j] + ":", tupperage[j])
    sumee += tupperage[j]
print("The average age of ur fren group is", (sumee/len(tupperbox)))