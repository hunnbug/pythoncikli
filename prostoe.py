print("Введите начало диапазона: ")
a = input()

print("Введите конец диапазона: ")
b = input()
print(" ")

anum = int(a)
bnum = int(b)

for num in range(anum, bnum):

    if num <= 1:
        continue
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
         print(num)
