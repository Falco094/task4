class Car:
    def __init__(self,make,model,year):
     self.odometer_reading=0
     self.make=make
     self.model=model
     self.year=year
    def get_description(self):
     
     return f"{self.make} {self.model}  {self.year}"
    
    def read_odometer(self):
        print (self.odometer_reading)

    def update_odometer(self,update_odometer):

        if update_odometer > self.odometer_reading:
            self.odometer_reading = update_odometer
            return self.odometer_reading
        else :
            print("wrong")


    def increment_odometer(self,increment):

        self.odometer_reading +=increment
        return self.odometer_reading
s=Car('England','class',2010)

print(s.get_description())

s.read_odometer()

s.update_odometer(40)

s.read_odometer()

s.increment_odometer(60)

s.read_odometer()
