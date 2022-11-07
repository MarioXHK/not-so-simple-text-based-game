def gfuel(aby,axz):
    return aby % axz
def somfo():
    for i in range(13):
        print("snorfle")
color = input("color")
if color == "green":
    print("The grass is green")
elif color == "blue":
    print("The sky is blue")
else:
    print("I dunno that color")
age = int(input("age"))
if age < 43:
    print("You're too young")
elif age > 43:
    print("You're too old")
else:
    print("Perfect age")
for h in range(50,30,-3):
    print(h)
g = 10
while g < 60:
    print(g)
    g += 5
print(g)
stop = "no"
while stop != "stop":
    stop = input()
    print(stop)
print(gfuel(63,13))
somfo()