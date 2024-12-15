# # # 1
# from abc import ABC, abstractmethod
# class Ship(ABC):
#     def __init__(self,title,length, width):
#         self.title=title
#         self.lenght=length
#         self.width=width

#     # def show_info(self):
#     #     print(f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}")
#     # def __del__(self):
#     #     print(f"--- Deleting unmanaged resources ({self.title}) ---")
#     # def __str__(self) -> str:
#     #     return f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}"

#     @abstractmethod
#     def show_info(self):
#         print(f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}")

# class Frigate(Ship):
#     def __init__(self,title,length, width,gunCount,sonarRange):
#         super().__init__(title,length, width)
#         self.gunCount=gunCount
#         self.sonarRange=sonarRange
#     def show_info(self):
#         print(f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}, Gun count: {self.gunCount}, Sonar Range: {self.sonarRange}")
#     def __del__(self):
#         print(f"--- Deleting unmanaged resources ({self.title}) ---")
#     def __str__(self) -> str:
#         return f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}, Gun count: {self.gunCount}, Sonar Range: {self.sonarRange}"



# class Destroyer(Ship):
#     def __init__(self,title,length, width,weaponType,stealthLevel):
#         super().__init__(title,length, width)
#         self.weaponType=weaponType
#         self.stealthLevel=stealthLevel

    
#     def show_info(self):
#         print(f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}, Weapon type: {self.weaponType}, Stealth Level: {self.stealthLevel}")
#     def __del__(self):
#         print(f"--- Deleting unmanaged resources ({self.title}) ---")
#     def __str__(self) -> str:
#         return f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}, Weapon type: {self.weaponType}, Stealth Level: {self.stealthLevel}"

        
# class Cruiser(Ship):
#     def __init__(self,title,length, width, maxspeed,helicopterCapacity):
#         super().__init__(title,length, width)
#         self.maxspeed=maxspeed
#         self.helicopterCapacity =helicopterCapacity
#     def show_info(self):
#         print(f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}, Max Speed: {self.maxspeed}, Helecopter Capacity: {self.helicopterCapacity}")
#     def __del__(self):
#         print(f"--- Deleting unmanaged resources ({self.title}) ---")
#     def __str__(self) -> str:
#         return f"Title: {self.title}, Length: {self.lenght}, Width: {self.width}, Max Speed: {self.maxspeed}, Helecopter Capacity: {self.helicopterCapacity}"



# frigate = Frigate("Frigate Defender", 120.0, 15.0, 10, 150.0)
# destroyer = Destroyer("Destroyer Invincible", 150.0, 20.0, "Laser-guided", 0.8)
# cruiser = Cruiser("Cruiser Aurora", 200.0, 25.0, 30.0, 2)

# frigate.show_info()
# print(frigate)

# destroyer.show_info()
# print(destroyer)

# cruiser.show_info()
# print(cruiser)

# # 2
# class Airplane:
#     def __init__(self,title,type,passengercount, maxpassenger):
#         self.title=title
#         self.type=type
#         self.passengercount=passengercount
#         self.maxpassenger=maxpassenger



#     def __eq__(self, other):
#         return self.type == other.type


#     def __add__(self, other):
#         a=self.passengercount + other
#         if a<=self.maxpassenger: 
#             return a
#         else:
#             print("Error:(")
#     def __gt__(self, other):
#         return self.maxpassenger > other.maxpassenger
#     def __sub__(self, other):
#         a=self.passengercount - other
#         if a>=0: 
#             return a
#         else:
#             print("Error:(")
#     def __iadd__(self, other):
#         a = self.passengercount + other
#         if a <= self.maxpassenger:
#             self.passengercount = a
#         else:
#             print("Error:(")
#         return self 

#     def __isub__(self, other):
#         a = self.passengercount - other
#         if a >= 0:
#             self.passengercount = a
#         else:
#             print("Error:(")
#         return self  






#     def show_info(self):
#         print(f"Title: {self.title}, Type: {self.type}, Passenger Count: {self.passengercount}, Max Passengers: {self.maxpassenger}")
#     def __del__(self):
#         print(f"--- Deleting unmanaged resources ({self.title}) ---")
#     def __str__(self) -> str:
#         return self.type
#     def __int__(self):
#         return self.passengercount




# plane1 = Airplane("Boeing 747", "Passenger", 100, 400)
# plane2 = Airplane("Airbus A320", "Passenger", 50, 180)

# print(plane1 == plane2)

# print(plane1 + 50)

# print(plane1 > plane2)

# print(plane1 - 20)

# plane1 += 50
# print(plane1.passengercount)

# plane1 -= 30 
# print(plane1.passengercount)

# plane1.show_info()

# del plane1

# print(str(plane2))

# print(int(plane2))