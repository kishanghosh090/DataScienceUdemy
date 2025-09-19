class Chai:
    temp = "HOT"
    strength = "STRONG"

cuttingChai = Chai()

print(cuttingChai.temp)

cuttingChai.temp = "MILD"
print(f"After changing {cuttingChai.temp}")
cuttingChai.cup = 5

del cuttingChai.cup
print(cuttingChai.cup)

del cuttingChai.temp

print(cuttingChai.temp)