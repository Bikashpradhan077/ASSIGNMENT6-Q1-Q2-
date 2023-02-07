class Dog:
    def __init__(self,name, age, coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    def description(self):
        print(f"name of the Dog is :  {self.name}")
        print(f"age of the dog is : {self.age}")
    def get_info(self):
        print(f'coat color of the dog is : {self.coat_color}')
        
class JackRussellTerrier(Dog):
    def __init__(self,name, age, coat_color,height="20-30 cm",mass="8-10 kg",bodylength="40-50cm"):
        super().__init__(name, age, coat_color)
        self.height=height
        self.mass=mass
        self.bodylength=bodylength
    def lifespan(self,lifeline="Lifespan of this dog breed is 10-12 years"):
        print(lifeline)
    def temprament(self):
        temper="Temprament of dog breed is Intelligent, Stubbon, Fearless"
        print(temper)
    def getappearance(self):
        print(f"height of Jack Russell Terrier is : {self.height}")
        print(f"weight of Jack Russell Terrier is : {self.mass}")
        print(f"overall bodylength of Jack Russell  Terrier is : {self.bodylength}")
         
class Bulldog(Dog):
    def __init__(self,name, age, coat_color,height="31-40 cm",mass="23-25 kg",bodylength="51-69 cm"):
        super().__init__(name, age, coat_color)
        self.height=height
        self.mass=mass
        self.bodylength=bodylength
    def lifespan(self):
        lifeline="Lifespan of this dog breed is : 6-8 years"
        print(lifeline)
    def temprament(self):
        temper="Temprament of this dog breed is Docile, Friendly, Gregacious"
        print(temper)
    def getappearance(self):
        print(f"height of Bulldog is : {self.height}")
        print(f"weight of Bulldog is : {self.mass}")
        print(f"overall bodylength of Bulldog is : {self.bodylength}")
        
J=JackRussellTerrier("Jackson",5,"White")
J.description()
J.get_info()
J.getappearance()
J.temprament()
print()
B=Bulldog("Heather", 7, "Brown & White")
B.description()
B.get_info()
B.getappearance()
B.temprament()