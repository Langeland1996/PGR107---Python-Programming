"""
Write a program to get a weight in either Pound (lbs) or Kilogram (kg) and converts it to the other unit.
1 Kilogram = 2.2 Pounds and 1 Pound = 0.45 Kilogram.

    Sample Output
        Weight: 160 ----- (L)bs or (K)g: L ---- You are 72.0 kilo(s)
"""

def weightSwapper(arg):
    args = str(arg)
    if args.lower().__contains__("kg"):
         weight = args.split(" ")[0]
         weightInLb = float(weight) * 2.2
         print(weightInLb, " Lbs")

    elif args.lower().__contains__("lbs"):
        weight = args.split(" ")[0]
        weightInKg = float(weight) * 0.45
        print(weightInKg, " Kgs")


print("input is 160 Lbs")
weightSwapper("160 LBSs")

print("\ninput 72.0 Kg")
weightSwapper("72.0 Kg")

print("input is 16.2 Lbs")
weightSwapper("16.2 Lbs")

print("\ninput 2 Kg")
weightSwapper("2 Kg")

