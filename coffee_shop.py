class Coffee_shop():

    def __init__(self, name, price):

        self.name = name

        self.price = price


class Order():

    def __init__(self):

        self.items = []
    
    def add_item(self,coffee_obj):

        self.items.append(coffee_obj)

    def view_cart(self):

        for index,item in enumerate(self.items,start=1):
            print(f"{index}. {item.name} -${item.price}")

    def get_total(self):

        total = sum(item.price for item in self.items)
        return total

class Main():

        Menu = [

            Coffee_shop("Americano", 2.0),
            Coffee_shop("Espresso", 2.5),
            Coffee_shop("Latte", 3.0),
            Coffee_shop("Cappuccino", 3.5),
        ]

        order = Order()

        while True:

            print("\n 🧾---- Coffee Shop ----🧾 ")
            for index,coffee in enumerate(Menu, start=1):
                print(f"{index}. {coffee.name} -${coffee.price}")
            print("5. View order List")
            print("6. Checkout")
            print("7. Exit the Coffee Shop APP")
            choice = input("Enter your choice:  ")

        
        if choice in ["1","2","3","4"]:
                coffee_index = int(choice) - 1
                selected = Menu[coffee_index]
                order.add_item(selected)
                print(f" Added {selected.name} to your order.")




