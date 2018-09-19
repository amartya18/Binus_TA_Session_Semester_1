inp = int(input("input a number: "))
for i in range (1, inp+1):
    print("*" * i)
print("")

for i in range (1, inp+1):
    print(" " * (inp - i)+("*" * i))
print("")

for i in range (1, inp+1):
    print("*" * (inp + 1 - i))
print("")

for i in range (0, inp):
    print(" " * i+"*" * (inp - i))
print("")

nilaiA = int(1)
nilaiB = int(inp-1)
for i in range(1,int(inp+1)):
    print(" " * nilaiB + "*" * nilaiA)
    nilaiA = nilaiA + 2
    nilaiB = nilaiB - 1
print("")

#try putting in an even number
inp2 = inp*2 - 1
nilai1 = int(1)
nilai2 = int(inp2-1)
for i in range (1,inp2+1):
    x = int(abs((inp2 - nilai1)/2))
    y = int((inp2 - abs(nilai2)))
    if inp2 % 2 == 0 and i == inp2 / 2:
        nilai1 = nilai1 - 1
    print(" " * (x)+"*" * (y))
    nilai1 = nilai1 + 2
    nilai2 = (nilai2 - 2)
print("")
