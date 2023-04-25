list = [12, 2334, 46, 25, 86, 654, 23456, 987, 345, 9876, 24, 9876, 345]

def product():
    s = 1
    for i in range(len(list)):
        s = s *  list[i]
    print(s)
      
product()