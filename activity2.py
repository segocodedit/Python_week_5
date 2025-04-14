class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚢")

class Train:
    def move(self):
        print("Chugging on the tracks 🚆")
    



# Create a list of different objects
things_that_move = [Car(), Plane(), Boat(), Train() ]

# Call the same method on each object
for thing in things_that_move:
    thing.move()
