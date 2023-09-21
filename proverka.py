print("введите число")

a = input()
anum = int(a)

k = 0
for i in range(2, anum // 2+1):
    if (anum % i == 0):
        k = k+1

if (k <= 0):
    print("Число простое")
else:
    print("Число не простое")