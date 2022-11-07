class airplane:
    #constructor
    def __init__(self, type):
        self.type = type
        self.speed = 0
        self.is_in_air = False
        self.fuel = 5000
    def printagain(self):
        print("I am a", self.type+".")
        if self.is_in_air == False:
            if self.fuel < 0:
                print("I'm grounded")
            else:
                print("I'm on the ground")
        else:
            print("I'm in the air")
        print("My speed is", self.speed, "and my fuel is", self.fuel)
        print()
    def take_off(self, tospeed):
        if self.is_in_air == False:
            self.speed = tospeed
            if self.speed >= 400 and self.fuel > 0:
                print(self.type, "Taking off")
                self.is_in_air = True
            elif self.fuel <= 0:
                print(self.type, "does not have enough fuel to take off")
                self.speed = 0
            else:
                print(self.type, "does not have enough speed to take off")
        else:
            print(self.type, "is already in the air")
        print()
    def landing(self):
        if self.is_in_air == True:
            print("Landing", self.type)
            self.speed = 0
            self.is_in_air = False
        else:
            print(self.type, "is already landed")
        print()
    def fly_for_hours(self,hours):
        if self.is_in_air == True:
            print("Flying", self.type, "for", hours, "hours.")
            self.fuel -= (self.speed*hours)
            if self.fuel <= 0:
                print("Warning:", self.type, "is out of fuel. Landing")
                self.landing()
        else:
            print(self.type,"is not in the air")
        print()
#Drive main somethitngsfdsgkjsgroijh9ihtroihgersoijhesgroigerrdipojdfbiojdfboijvcx oijfcxolibf
ps1 = airplane("Areoplan")
ps2 = airplane("Lamp named car")
ps3 = airplane("[BIG SHOT]")
ps4 = airplane("Lofi Piano")
ps1.printagain()
ps2.printagain()
ps3.printagain()
ps4.printagain()
ps1.take_off(23)
ps1.printagain()
ps1.take_off(500)
ps1.printagain()
ps1.fly_for_hours(3)
ps1.printagain()
ps3.printagain()
ps3.take_off(300)
ps3.printagain()
ps3.fuel = 0
ps3.printagain()
ps3.take_off(400)
ps4.take_off(400)
ps3.printagain()
ps1.fly_for_hours(5)
ps4.printagain()
ps4.landing()
ps2.landing()
ps1.fly_for_hours(6)
ps1.printagain()
ps2.take_off(450)
ps1.fuel += 3500
ps1.printagain()
ps1.fuel += 1000
ps2.fly_for_hours(2)
ps1.printagain()
ps1.fuel += 1000
ps1.printagain()
ps1.take_off(250)
ps2.fly_for_hours(2)
ps1.printagain()
ps1.take_off(640)
ps1.fly_for_hours(2)
ps4.take_off(400)
ps4.fly_for_hours(12)
ps2.landing()
ps1.landing()
ps3.landing()
ps4.landing()
ps1.printagain()
ps2.printagain()
ps3.printagain()
ps4.printagain()