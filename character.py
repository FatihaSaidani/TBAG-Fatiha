# Creating the parent class for all characters
class Character():
    def __init__ (self, char_name, char_description, char_weakness):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.weakness = char_weakness

    # description of characters and allowing conversation
    def describe(self):
        print("--------------------------------------------")
        print(f"{self.name} is in this room!")
        print(self.description)
        print("--------------------------------------------")
    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("--------------------------------------------")
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print("--------------------------------------------")
            print(f"{self.name} doesn't want to talk to you.")    

    # allowing for the user to fight the character, giving them a weakness 
    def fight(self, combat_item):
        print("--------------------------------------------")
        print(f"{self.name} doesn't want to fight you.")
        return True
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    

# child class, first type of character
class Enemy(Character):
    def __init__(self, char_name, char_description, char_weakness):
        super().__init__(char_name, char_description, char_weakness)

    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print("--------------------------------------------")
            print(f"you fend {self.name} off with the {combat_item}!")
            return True
        else:
            print("--------------------------------------------")
            print(f"{self.name} crushes you, puny adventurer")
            return False
        
# child, class second type of character
class Friendly(Character):
    def __init__ (self, char_name, char_description, char_weakness):
        super().__init__(char_name, char_description, char_weakness)
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print("--------------------------------------------")
            print(f"{self.name} can't fight, but enjoys the {combat_item}")
            return True 
        else:
            print("--------------------------------------------")
            print(f"{self.name} rejects this.")
            return False
