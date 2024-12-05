import sys 
accaunts = {
    "Nadia": "pa55w0rd",
    "Kyryl": "dr0w55as",
    "Dima": "password",
    "Olia": "pas"
}

def write(accaunts):
    for i in accaunts.items():
        print(f"Країна:{i[0]},\t\t Cтолиця:{i[1]}")
def rem(accaunts, keyy):
    accaunts.pop(keyy)
    write(accaunts)
def add(accaunts, key, value):
    accaunts.update({key: value})
    write(accaunts)
def search(accaunts, key):
    print(accaunts[key])
def change(accaunts, key, value):
    accaunts[key] = value
    write(accaunts)
    
def strr(t):
    pas = t[1]
    for j in range(len(pas)):
        if pas[j] in [f"{g}" for g in range(0,10)]:
            return
    print(t)
    
    

def check(accaunts):
    for i in accaunts.items():
        if len(i[1])<6: 
            print(i)
        else:
             strr(i)
            
def savefile(accaunts, filename="accounts.txt"):
    try:
        with open(filename, "w") as file:
            for key, value in accaunts.items():
                file.write(f"{key}:{value}\n")
        print(f"SAVE IN'{filename}'")
    except Exception as e:
        print(f"ERROR: {e}")

while True:
    
    choise=int(input("1.DELETE BY LOGIN\n2.ADD\n3.SEARCH BY LOGIN\n4.CHANGE PASSWORD BY LOGIN\n5.WRITE DICT\n6.CHECK ALL PASSWORD\n7.SAVE IN FILE\n8.EXIT\nEnter choise: "))
    if choise==1:
        rem(accaunts, input("Enter LOGIN: "))
    elif choise==2:
        add(accaunts, input("Enter LOGIN: "), input("Enter password: "))
    elif choise==3:
        search(accaunts, input("Enter LOGIN: "))
    elif choise==4:
        change(accaunts, input("Enter LOGIN: "), input("Enter password: "))
    elif choise==5:
        write(accaunts)
    elif choise==6:
        check(accaunts)
    elif choise==7:
        savefile(accaunts)
    elif choise==8:
        print("Bye")
        sys.exit()




