class Car:
    def __init__(self, regnum, maxspeed, curentspeed, traveleddis):
        self.regnum = regnum
        self.maxspeed = maxspeed
        self.curentspeed = 0
        self.traveleddis = 0

    def __str__(self):
        return(f"{self.regnum} {self.maxspeed} {self.curentspeed}")


    def acceleration(self,change):
        self.curentspeed += change
        if self.curentspeed > self.maxspeed:
            self.curentspeed = self.maxspeed
        elif self.curentspeed < 0:
            self.curentspeed = 0

        print(f"the speed after change is{change}: {self.curentspeed}")
    def drive(self,hour):

      traveleddis = self.traveleddis + hour




car1=Car("ABC-123",142,0,0)

print(car1.regnum)
print(car1.maxspeed)
car1.acceleration(30)
car1.acceleration(70)
car1.acceleration(50)
car1.accelerate(-200)
print(car1)