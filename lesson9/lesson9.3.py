def num():
    with open('numbers.txt', 'r') as file:
        a = file.read()
        for i in range(len(a)):
            if int(i) == i:
                with open('integers.txt', 'w') as file2:
                    b = file.write(i)
                    print(b)
num()                    