class BMW:
    def start(self):
        print("BMW engine starts smoothly.")

    def speed(self):
        print("BMW has a top speed of 250 km/h.")

    def fuel_type(self):
        print("BMW uses petrol or diesel.")


class Ferrari:
    def start(self):
        print("Ferrari engine roars to life!")

    def speed(self):
        print("Ferrari has a top speed of 340 km/h.")

    def fuel_type(self):
        print("Ferrari uses high-octane petrol.")


# Polymorphism in action
def vehicle_details(vehicle):
    vehicle.start()
    vehicle.speed()
    vehicle.fuel_type()


# Creating objects
bmw = BMW()
ferrari = Ferrari()

# Calling same function for different objects
vehicle_details(bmw)
print()
vehicle_details(ferrari)
