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
    




