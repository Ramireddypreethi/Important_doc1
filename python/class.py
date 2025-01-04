class computer:
    def __init__(self,ram,hdd): #constructor
        self.ram=ram
        self.hdd=hdd
    def config(self): #instance method
        print("computer configuration:")
        print(self.ram) # self is first arguement for both instance and constructor
        print(self.hdd)
comp1=computer('16gb','500gb')
comp1.config()