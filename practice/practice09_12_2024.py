class Passport:
    def __init__(self,Name, Surname,Birthday, Date, Number):
        self.Name = Name
        self.Surname = Surname
        self.Birthday = Birthday
        self.Date = Date
        self.Number = Number

    def show_info(self):
        print(f"Name: {self.Name}, Surname: {self.Surname}, Birthday: {self.Birthday}, Issue Date: {self.Date}, Passport Number: {self.Number}")
    def __del__(self):
        print(f"--- Deleting unmanaged resources ({self.Number}) ---")
    def __str__(self) -> str:
        return f"Name: {self.Name}, Surname: {self.Surname}, Birthday: {self.Birthday}, Issue Date: {self.Date}, Passport Number: {self.Number}"

class ForeignPassport(Passport):
    def __init__(self,Name, Surname,Birthday, Date, Number,Vise , numforeign):
        super().__init__(Name, Surname, Birthday, Date, Number)
        self.Vise = Vise
        self.numforeign = numforeign

    def show_info(self):
        print(f"Name: {self.Name}, Surname: {self.Surname}, Birthday: {self.Birthday}, Issue Date: {self.Date}, Passport Number: {self.Number}, Visa: {self.Vise}, Forgein passport number: {self.numforeign}")

    def removeVisa(self):
        self.Vise.remove(input("Input Visa number: "))
    def appendVisa(self):
        self.Vise.append(input("Input new Visa number: "))

    def __del__(self):
        print(f"--- Deleting unmanaged resources ({self.numforeign}) ---")

    def __str__(self) -> str:
        return f"Name: {self.Name}, Surname: {self.Surname}, Birthday: {self.Birthday}, Issue Date: {self.Date}, Passport Number: {self.Number}, Visa: {self.Vise}, Forgein passport number: {self.numforeign}"




passport1 = Passport("John", "Doe", "1980-05-15", "2010-06-01","A12345678")
foreign_passport1 = ForeignPassport(passport1.Name, passport1.Surname, passport1.Birthday, passport1.Date, passport1.Number, ["AS123HUO", "ASDIW122",":)"],"G78H32328")


passport1.show_info()
foreign_passport1.show_info()

foreign_passport1.appendVisa()
foreign_passport1.show_info()
foreign_passport1.removeVisa()
foreign_passport1.show_info()





# class Temperature():
#     # def __init__(self,temper):
#     #     self.temper = temper
    
#     counter = 0

#     @staticmethod
#     def cels(t):
#         print("Температура в Цельсіях:", (t - 32) *(5/9) )
#         Temperature.counter += 1

#     @staticmethod
#     def fare(t):
#         print("Температура в Фаренгейтах:", (9/5)*t + 32)
#         Temperature.counter += 1

#     @staticmethod
#     def cou():
#         print("Кількість виконаних змін: ", Temperature.counter)


# Temperature.cou()
# Temperature.cels(int(input("Введіть температуру в Фаренгейтах: ")))
# Temperature.cou()
# Temperature.fare(int(input("Введіть температуру в Цельсіях: ")))
# Temperature.cou()
# Temperature.cels(int(input("Введіть температуру в Фаренгейтах: ")))
# Temperature.cou()
# Temperature.fare(int(input("Введіть температуру в Цельсіях: ")))
# Temperature.cou()









