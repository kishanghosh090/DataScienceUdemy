# namespace

class Chai:
    origin = "India"


Chai.is_hot = True
# print(Chai.is_hot)

# creating objects from class chai

masala = Chai()

print(masala.origin)
print(masala.is_hot)
masala.is_hot = False
print(masala.is_hot)
print(f"class : {Chai.is_hot}")