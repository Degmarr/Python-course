class Student():
    __group = " "
    __age = 0
    def __init__(self, name = " ", age1 = " ", pk = " "):
        self.name = name
        self.age = age1
        self.pk = pk
        

    def Set_Group(self, group):
        self.__group = group
        print("Группа персонажа", self.name, " изменена на ", self.__group)
    
    def Set_Age(self, age):
        if age < 0:
            print("Age cannot be negative")
        else:
            self.age1 = age
            print("Возраст персонажа", self.name, " изменена на ", self.age1)

student1 = Student("Кавех", 24, 1)     
# персонажи взяты из игры Genshin Impact, где выбранные персонажи имеют свой факультет
student2 = Student("Аль-Хайтам", 22, 2)


for i in range(3):
    a = int(input("Введите число, соответсвующее желаемому действию: 1 - узнать информацию про персонажа, 2 - изменить группу персонажа, 3 - изменить возраст персонажа   "))
    if a == 1:
        print("Имя: ",student1.name, "Возраст: ",student1.age, "Номер студента: ",student1.pk, sep = "\n")
        print("Имя: ",student2.name, "Возраст: ",student2.age,"Номер студента: ", student2.pk, sep = "\n")
    elif a == 2:  
        student1.Set_Group("Кхашевар")
        student2.Set_Group("Хараватат")
    elif a == 3:
        ag = int(input("Введите желаемый возраст для Кавеха "))
        student1.Set_Age(ag)
        af = int(input("Введите желаемый возраст для Аль-Хайтама "))
        student2.Set_Age(af)

