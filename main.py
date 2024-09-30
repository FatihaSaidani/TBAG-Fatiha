from room import Room
from character import Enemy
from character import Friendly

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining hall")

dave = Enemy("Dave", "a smelly zombie", "cheese")
dave.describe()
dave.set_conversation("Hi I'm Dave, totally wont eat your brains!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

cat = Friendly("cat", "A cute fluffy pet that is immune from zombies", "cuddles")
cat.describe()
cat.set_weakness("cuddles")
kitchen.set_character(cat) 

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

current_room = kitchen

while True: 
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()

    if inhabitant is not None:
        inhabitant.describe()

        command = input("Would you like to talk to, or fight this character? > ").lower()

    if command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
             print("There's no one to talk to.")    

    elif command == "fight":
        if inhabitant is not None:
            print("Choose a weapon to fight with > ")
            fight_with = input("Choose one: knife, cheese, cuddles ")
            if not inhabitant.fight(fight_with):
                print("You have been defeated! GAME OVER.")
                break
        else:
             print("There's no one to fight with.")   

    elif command in ["north", "south", "east", "west"]:
            next_room = current_room.move(command)
            if next_room is not None:
                    current_room = next_room
            else:
                print("you can't go that way")    
    else:
        print("Invalid command.")
        

       

