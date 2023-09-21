print("введите число")
a = input()

print("угадайте число:")
b = input()

anum = int(a)
bnum = int(b)
if(anum == bnum):
    print("вы угадали")
else:
    print("вы не угадали")