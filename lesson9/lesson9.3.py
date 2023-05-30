def num():
    numbers = []
    with open("numbers.txt", "r") as f:
        data = f.read().split()
        for i in data:
            try:
                numbers.append(int(i))
            except ValueError:
                continue

    print(numbers)
    for num in numbers:
        with open("integers.txt","a") as f2:
            f2.write(str(num) + "\n")        
                    
num()                    