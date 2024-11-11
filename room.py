# Parent class for rooms
class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.is_locked = False

    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character 
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def set_item(self, new_item):
        self.item = new_item 

    def get_item(self):
        return self.item       
    
    def lock_room(self):
        self.is_locked = True

    def unlock_room(self):
        self.is_locked = False

    def is_room_locked(self):
        return self.is_locked        

    # allows for the user to see and understand the room they are in, and move
    def get_details(self):
        print(f"You are in the {self.name}") 
        print("--------------------------------------------")   
        print(self.description)
        print("--------------------------------------------")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")

    # allows for the user to move to different rooms unless locked 
    def move(self, direction):
            if direction in self.linked_rooms:
                next_room = self.linked_rooms[direction]
                if next_room.is_room_locked():
                    print(f"The {next_room.get_name()} is locked. Would you like to 'unlock'?")
                    return None
                return next_room 
            else:
                print("You can't go that way")
                return self
