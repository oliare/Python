class Order:

    # static field
    initNum = 1000

    #constructor
    def __init__(self, title, price, discount):
        self.title = title
        self.discount = discount
        self.__price = price

        self.number = Order.initNum
        Order.initNum += 1

    # destructor
    def __del__(self):
        # clear unmanaged resources
        print("--- delete unmanaged resources ---")


    def show_info(self):
        print(f"product info: {self.title} - {self.price}$")
        
    def getPrice(self):
        return self.price

    def setPrice(self, value):
        self.price = value

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        
    # override base str conversion
    def __str__(self) -> str:
        return f"{self.title} - {self.price}$"
        
order1 = Order('Marshall Major V', 150, 5)
order2 = Order('Xiomi Redmi 5', 130, 3)
order3 = Order('Apple Vision Pro', 1050, 0)

order2.setPrice(279)
print(f"New price: {order2.getPrice}")

order2.price = 189
print(f"New price: {order2.getPrice}")

order1.show_info()

print(order1)
print(order2)
print(order3)