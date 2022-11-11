class fridge:
    def __init__(self):
        self.NumberOfItems = 0
        self.DoorOpen = False
        self.isRunning = True
    def foodprint(self):
        print("This fridge has", self.NumberOfItems, "items")
        print("It's door being open is", self.DoorOpen)
        print("And the fridge itself running is", self.isRunning)
        if self.isRunning == True:
            print("You should catch it")
    def openDoor(self):
        self.DoorOpen = True
        print("Ooo light!")
    def closeDoor(self):
        self.DoorOpen = False
        print("Ooo shut!")
    def fillFridge(self, thing):
        self.NumberOfItems += int(thing)
        print("Filling fridge with", thing, "food things.")
    def MakeDinner(self):
        if self.NumberOfItems >= 10:
            self.NumberOfItems -= 10
            print("Yum :)")
        else:
            print("Not enough food :(")
freezer = fridge()
freezer.foodprint()
freezer.openDoor()
freezer.foodprint()
freezer.closeDoor()
freezer.foodprint()
freezer.fillFridge(15)
freezer.foodprint()
freezer.MakeDinner()
freezer.foodprint()
freezer.MakeDinner()
freezer.foodprint()
print(freezer.NumberOfItems)