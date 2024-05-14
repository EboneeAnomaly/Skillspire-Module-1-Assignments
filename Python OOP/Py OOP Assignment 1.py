class Car:
    def __init__(self, topSpeed, miles):
        self.topSpeed = topSpeed
        self.miles = miles

    def printCarInfo(self):
     print(f"{self.topSpeed} topSpeed")

mustang = Car("163mph","")


print("Mustang Top Speed: ", mustang.topSpeed)



mustang.printCarInfo()

location = Car("", 0)

def drive():
    for i in range(0):
        print("start")
def stop():
    for i in range(11):
        if i > 10:
            break
        print(i)

drive()

print("\nStopping at 10:" + "Destination Reached")
stop()