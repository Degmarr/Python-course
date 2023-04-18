#Создайте функцию, которая позволяет посчитать периметр и площадь квадрата (значения сторон вводит пользователь).
a = int(input("Enter length of a square's edge: "))

def per(a):
    print("Perimeter of the square is ", 4*a)
per(a)
def area(a):
    print("Area of the squeare is ", a*a)
area(a)        