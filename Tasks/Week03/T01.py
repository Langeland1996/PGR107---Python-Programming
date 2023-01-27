# 1. What do these code fragments print?
# 1a.
from math import sqrt

print("\nTask 1A")
n = 1
m = -1
if n < -m:  # false
    print(n)
else:
    print(m)  # true

# 1b.
print("\nTask 1B")
n = 1
m = -1
if -n >= m:  # true
    print(n)  # true
else:
    print(m)

# 1c.
print("\nTask 1C")
x = 0.0
y = 1.0
if abs(x - y) < 1:  # false
    print(x)
else:
    print(y)  # true

# 1d.
print("\nTask 1D")
x = sqrt(2.0)
y = 2.0
if x * x == y:  # false
    print(x)
else:
    print(y)  # true