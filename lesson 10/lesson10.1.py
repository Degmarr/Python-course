class One():
    name = " "
    value = 0

    def product(self, a):
        print(self.value * a)
    
    def sum(self, b):
        print(self.value + b)    
    
    def div(self, c):
        print(self.value / c)

    def sub(self, d):
        print(self.value - d)    



variable1 = One()
variable1.name = 'x'
variable1.value = 666
variable1.product(56)
variable1.sum(64732)
variable1.sub(435)
variable1.div(3)

variable2 = One()
variable2.name = 'y'
variable2.value = 777
variable2.product(67)
variable2.sum(6854)
variable2.sub(934)
variable2.div(111)

