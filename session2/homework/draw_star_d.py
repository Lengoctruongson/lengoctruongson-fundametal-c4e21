n = int(input("Enter n: "))
m = int(n/2)
d = n % 2
for i in range(m-1):
    print("x",end=" * ")
if d == 1:
    print("x")
else:
    print("x *")