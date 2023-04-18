def sum(a, b):
    s = 0
    if b > a:
        s = a
        for i in range(a, b + 1):
            s = s + i
        print(s)
    if a > b:
        s = b
        for i in range(b, a + 1):
            s = s + i
        print(s)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum(a, b)


                