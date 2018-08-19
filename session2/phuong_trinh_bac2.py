a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
denta = b**2 - 4*a*c
if denta > 0:
    sqrt = denta
    x1 = (-b + denta**0.5) / (2*a)
    x2 = (-b - denta**0.5) / (2*a)
    print("Phuong trinh co 2 nghiem:")
    print("x1 =", x1) 
    print("x2 =", x2) 
elif denta == 0:
    x = -b/(2*a)
    print("Phuong trinh co nghiem duy nhat:")
    print("x =", x) 
else:
    print("Phuong trinh vo nghiem")