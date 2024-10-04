class Item():
    def __init__(self):
        self.name = None
        self.description = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description  
    
    def set_description(self, item_description):
        self.description = item_description      

class Keys(Item):
    def __init__ (self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def describe(self):
        print("--------------------------------------------")
        print(f"This Item: {self.name}")
        print(f"Description: {self.description}")
