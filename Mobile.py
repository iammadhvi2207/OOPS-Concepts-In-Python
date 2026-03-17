class Mobile:
    def __init__(self, brand, price):
        self.brand =brand
        self.__price = price

    def change_price(self, new_price):
        self.__price = new_price

    def display(self):
        return self.__price

m1= Mobile("Samsung", 50000)
m1.change_price(500)
print(m1.display())