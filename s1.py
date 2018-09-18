inp = int(input("input a number: "))
for i in range (1, inp+1):
    print(" " * (inp - i),("*" * i))

inp = int(input("input a number: "))
for i in range (1, inp+1):
    print("*" * (inp + 1 - i))

inp = int(input("input a number: "))
nilai1 = int(1)
nilai2 = int(inp-1)
for i in range (1,inp+1):
    x = int(abs((inp - nilai1)/2))
    y = int((inp - abs(nilai2)))
    print(" " * (x)+"*" * (y))
    nilai1 = nilai1 + 2
    nilai2 = (nilai2 - 2)







