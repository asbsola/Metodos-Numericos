s1 = 0.0
s2 = 0.0

for i in reversed(range(2, 10001)):
    s1 = s1 + i**-2
    s2 = s2 + i**2
for i in range(1, 10001):
    s1 = s1 + i**2
    s2 = s2 + i**-2


print(f"best sum: {s1}")
print(f"worst sum: {s2}")