class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} {self.age}")
    def sit (self):
        print("Maman wont sit")
    def roll_over(self):
        print("Maman is rolling Over")
dog=Dog("Maman",30)
dog.sit()
dog.roll_over()
        
        