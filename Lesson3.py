a = int(input())
b = int(input())
c = int(input())
if (a + b + c) % 2 == 0:
    res = (a + b + c) // 2
else:
    res = (a + b + c + 1) // 2
print(res)