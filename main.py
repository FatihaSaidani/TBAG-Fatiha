from room import Room
from character import Enemy
from character import Friendly
from item import Keys

# setting the rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining hall")

# setting the character details and location
dave = Enemy("Dave", "a smelly zombie", "cheese")
dave.set_conversation("Hi I'm Dave, totally wont eat your brains!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# setting the character details and location
cat = Friendly("cat", "A cute fluffy pet that is immune from zombies", "cuddles")
cat.set_weakness("cuddles")
kitchen.set_character(cat) 

# setting the item details 
key = Keys("key", "This item can help you unlock doors, if you are willing to take the risk")
kitchen.set_item(key)

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")

# allowing the rooms to be linked to eachother/next to eachother
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

ballroom.lock_room()

# starting point for user
current_room = kitchen
player_inventory = []


# Main while loop
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    room_item = current_room.get_item()

    # if statement that allows the user to interact
    if room_item is not None:
        print("--------------------------------------------")
        print(f"You have found a {room_item.get_name()} here.")
        take_item = input(f"Do you want to pick up the {room_item.get_name()}? ").lower()
        if take_item == 'yes':
            player_inventory.append(room_item)
            current_room.set_item(None)  # Remove the item from the room
            print("--------------------------------------------")
            print(f"You now have the {room_item.get_name()}.")

    if inhabitant is not None:
        inhabitant.describe()

    # Main loop for game, giving the user options
    command = input("Would you like to talk, fight, or move to another room? > ").lower()

    if command == "talk":
        if inhabitant is not None:
            inhabitant.describe()
            inhabitant.talk()
        else:
            print("There's no one to talk to.")

    # allows the user to fight the characters
    elif command == "fight":
        if inhabitant is not None:
            print("Choose a weapon to fight with > ")
            fight_with = input("Choose one: knife, cheese, cuddles ").lower()
            if not inhabitant.fight(fight_with):
                print("--------------------------------------------")
                print("You have been defeated! GAME OVER.")
                break
        else:
            print("There's no one to fight.")

    # allows the user to move around to different rooms
    elif command in ["north", "south", "east", "west"]:
        next_room = current_room.move(command)
        if next_room is not None:
            current_room = next_room

    # allows the user to utilise the key if collected
    elif command == "unlock":
        direction = input("Which door would you like to unlock (north/south/east/west)? > ").lower()
        if direction in current_room.linked_rooms:
            next_room = current_room.linked_rooms[direction]
            if next_room.is_room_locked():
                has_key = any(item.get_name().lower() == "key" for item in player_inventory)
                if has_key:
                    print(f"Unlocking {next_room.get_name()}...")
                    next_room.unlock_room()
                    print(f"You have unlocked the {next_room.get_name()} with the key!")
                else:
                    print("You do not have the key to unlock this room.")
            else:
                print(f"The {next_room.get_name()} is not locked.")
        else:
            print("There is no room in that direction.")
    
    else:
        print('Invalid command. Try something else.')  # This will only trigger if none of the above commands are valid.
