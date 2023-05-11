N = int(input("Введите количество монет:"))
orel = reshka = 0
for i in range(N):
    x = int(input("Орел(1) или решка(0)?:"))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print("Переверните {orel} монет с орла на решку, их меньше всего")
elif orel == reshka:
    print("Количество орлов и решек одинаково, по {orel} штук")
else:
    print(("Переверните {reshka} монет с решки на орла, их меньше всего"))