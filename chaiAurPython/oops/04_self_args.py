class ChaiCup:
    size = 150

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = ChaiCup()
print(cup.describe()) 

# print(ChaiCup.describe(cup))
    

cup2 = ChaiCup()
print(cup2.describe()) 
cup2.size = 100000000
print(ChaiCup.describe(cup2))
