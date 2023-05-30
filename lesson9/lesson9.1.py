def OpenFile():
    with open('meowmeow.txt', 'r') as file:
        a = file.read()
        print(a)
OpenFile()        
