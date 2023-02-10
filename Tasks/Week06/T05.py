# 6. Write a program using nested for loop to draw the following shapes.
x = ""
for i in range(5):
    for j in range(1):
        if i == 0 or i == 2:
            x = "XXXXX"
            print(x)
        else:
            x = "XX"
            print(x)

print("\n\n\n")

for i in range(5):
    for j in range(1):
        if i == 4:
            x = "XXXXX"
            print(x)
        else:
            x = "XX"
            print(x)

