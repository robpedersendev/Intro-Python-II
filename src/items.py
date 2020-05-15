class Items:
    def __init__(self, item_description, items=[]):
        self.items = items
        self.item_description = item_description

    def __str__(self):
        return f"{self.items}--{self.item_description}"
