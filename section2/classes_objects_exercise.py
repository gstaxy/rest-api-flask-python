class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}

    def stock_price_method_1(self):
        return sum([item['price']] for item in self.items)

    def stock_price_method_2(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
