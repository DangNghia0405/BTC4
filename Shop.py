class Shop:
    def __init__(self, name, item):
        self.name = name 
        self.item = item
    def get_items_count(self):
        return len(self.items)
shop = Shop("My shop",["Nghĩa","Đat","Chí"])
print(shop.get_items_count()) 