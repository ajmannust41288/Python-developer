# class Vehicle:
#     # class attributes
#     color="white"
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#     pass
# class Car(Vehicle):
#     pass
# school_bus=Bus("Volocano",1200,12)
# print("Bus color : \n",school_bus.color,"\n ",school_bus.name,
#       "\n maxspeed",school_bus.max_speed,"\n mileage :",
#       school_bus.mileage)
# car_veh=Car("AudiQ6",1800,18)
# print("Car color : \n",car_veh.color,"\n name",car_veh.name,"\n maxspeed :",
#       car_veh.max_speed,"\n mileage",car_veh.mileage)
#-------------------------------------------------------excersise 6
# class Vehicle:
#     def __init__(self, name, mileage, capacity,maintenence):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#         self.maintainance=maintenence
#     def fare(self):
#         return self.capacity * 100
#     def maintaince(self):
#         return self.maintainance*10
# class Bus(Vehicle):
#     def fare(self):
#         amount=super().fare()
#         amount+=amount*10/100
#         return amount
# School_bus = Bus("School Volvo", 12, 50,20)
# print("Total Bus fare is:", School_bus.fare(),
#       "\n maintainance charges are :",School_bus.maintainance)
#----------------------------------------------excercise 7
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
# class Bus(Vehicle):
#     pass
# School_bus = Bus("School Volvo", 12, 50)
# # Python's built-in type()
# print(type(School_bus))
#------------------------------------------------------excersise8
#------------------------------------------Excercise 8----------------------
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
# class Bus(Vehicle):
#     pass
# School_bus = Bus("School Volvo", 12, 50)
# # Python's built-in isinstance() function
# print(isinstance(School_bus, Vehicle))
#--------------------------------------------------------------excercise 9
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#     def fare(self):
#         return self.capacity * 100
# class Bus(Vehicle):
#     def __init__(self, name, mileage, capacity=50):
#         super().__init__(name, mileage, capacity)
#     def fare(self):
#         fare = super().fare()
#         # this is bus so we need to add an extra 10% on full fare as a maintenance charge
#         total_fare = fare + (fare * 0.10)
#         return total_fare
# School_bus = Bus("School Volvo", 12)
# print("Total Bus fare is:", School_bus.fare())
#-------------------------------------------------------------------Excercise 10
class Vehicle:
    color = 'white'
    def __init__(self, name='', max_speed='', mileage=''):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seatingcapacity(self):
        print('seating capacity of {} is {}'.format(self.name, self.capacity))
    def display(self):
        print('Vehicle Name:{}'.format(self.name),
              'Max Speed:{}'.format(self.max_speed),
              'Mileage:{}'.format(self.mileage),
              'Color:{}'.format(self.color))
    def fare(self):
        print("The fare for {} is {}".format(self.name, int(self.capacity) * 100))
    def belongs(self):
        print(self.__class__.__name__)
    def checkins(self):
        print('Instance of Vehicle:{}'.format(isinstance(self, Vehicle)))
class Bus(Vehicle):
    def __init__(self, capacity='', **kwargs):
        self.capacity = capacity
        super().__init__(**kwargs)
    def fare(self):
        print(
            "The fare for {} is {}".format(self.name, int(self.capacity) * 100 + int((int(self.capacity) * 100) // 10)))
class Car(Vehicle):
    def __init__(self, capacity='', **kwargs):
        self.capacity = capacity
        super().__init__(**kwargs)
# Example Input:
a = {'name': 'Volvo',
     'max_speed': 30,
     'mileage': 40,
     'capacity': 100}
b = {'name': 'Volkswagon',
     'max_speed': 50,
     'mileage': 100,
     'capacity': 30}
c = Bus(**a)
d = Car(**b)
c.display()
c.seatingcapacity()
c.fare()
c.belongs()
c.checkins()
d.display()
d.seatingcapacity()
d.fare()
d.belongs()
d.checkins()