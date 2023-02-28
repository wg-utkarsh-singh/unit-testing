class Discount:
    def __init__(self, item_count, price):
        self.item_count = item_count
        self.price = price


class Checkout:
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_discount(self, item, item_count, price):
        discount = Discount(item_count, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        self.items[item] = self.items.get(item, 0) + 1

    def calc_item_disc(self, item, count, discount):
        discount_count = count / discount.item_count
        total = discount_count * discount.price
        rem = count % discount.item_count
        total += rem * self.prices.get(item, 0)
        return total

    def calc_item_total(self, item, count):
        rslt = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.item_count:
                rslt += self.calc_item_disc(item, count, discount)
        else:
            rslt += self.prices[item] * count
        return rslt

    def calc_total(self):
        total = 0
        for item, count in self.items.items():
            total += self.calc_item_total(item, count)
        return total
