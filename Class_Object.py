class About_info:                   # Class(Template)
    def Insert_Data(self):          # Method -1
        self.name = input("Enter the name:")
        self.id = int(input("Enter the ID :"))
        self.salary = float(input("Enter the salary:"))
    def display(self):              # Method-2
        print("Employe name:",self.name)
        print("Employe ID:",self.id)
        print("Employe salary:",self.salary)

a= About_info()                     # Object
a.Insert_Data()
a.display()
        
    