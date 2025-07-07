class Coffee_shop():

    def __init__(self, name, price):

        self.name = name

        self.price = price


class Order():

    def __init__(self):

        self.items = []
    
    def add_item(self,coffee_obj):

        self.items.append(coffee_obj)





