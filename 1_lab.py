a=int(input("Введите число "))
for i in range(1, a+1):
    print(i)

s=int(input("Введите первое число: "))
d=int(input("Введите второе число: "))
if s>d:
    print(f"Большее число {s}")
else:
    print(f"Большее число {d}")