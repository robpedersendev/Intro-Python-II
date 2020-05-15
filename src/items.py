class Item:
    def __init__(self, item_description, item):
        self.item = item
        self.item_description = item_description

    def __str__(self):
        return f"{self.item}--{self.item_description}"
