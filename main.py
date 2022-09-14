import random

LINE = " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "


def simulation(num_doors=4):
    doors = [str(item) for item in range(1, num_doors)]

    # Put the prize on some random position
    prize = random.choice(doors)

    print(LINE)
    print(f"Doors numbers: {doors}")
    selection = input("Pick up a door number: ")

    if selection == prize:
        remaining = list(set(doors) - set(prize))
        open_door = random.choice(list(set(doors) - set(random.choice(remaining))))
        alternate = random.choice(list(set(doors) - set(open_door) - set(prize)))
    else:
        open_door = random.choice(list(set(doors) - set(selection) - set(prize)))
        alternate = random.choice(list(set(doors) - set(open_door) - set(selection)))

    print(f"I will show you an empty door: {open_door}")
    print(LINE)
    second_chance = input("Would you like to select the third door? Type 'yes' or 'no': ")

    changed_door = True if second_chance == "yes" else False
    won = False
    if changed_door:
        print(f"The door you will switch to is: {alternate}")
        if alternate == prize:
            print(f"Congratulations, you win! The prize was behind of the door: {alternate}")
            won = True
        else:
            print(f"Sorry, the prize was behind the original door: {prize}")
    else:
        print(f"You decided to keep your initial door: {selection}")
        if selection != prize:
            print(f"Sorry, the prize was behind the door: {prize}")
        else:
            print(f"Congratulations, you win! The prize was behind of the original selection: {selection}")
            won = True

    print(LINE)
    print("Let`s check the final result:")
    print(LINE)

    print(f"The prize is behind the door: {prize}")
    print(f"Your initial selection was: {selection} ")
    print(f"You decide {'to change your first choice' if changed_door else 'keep your first choice'}")
    if changed_door:
        print(f"You change from {selection} door to {alternate} door and ...")
    if won:
        print("You Won the price =]")
    else:
        print("You loose the price =(")


def statistical_formula(num_doors):
    list_doors = [str(item) for item in range(0, num_doors)]
    size_of_set = len(list_doors)

    percentage_of_each_door_without_changed = 100.0 / size_of_set
    initial_selection = percentage_of_each_door_without_changed
    distributed_percentage = percentage_of_each_door_without_changed/(size_of_set - 2)
    alternative_door = percentage_of_each_door_without_changed + distributed_percentage

    print(LINE)
    print(f"A problem to choose a door between {size_of_set} doors")
    print(f"Initial probability of winning of each door: {round(percentage_of_each_door_without_changed,2)}%")
    print(f"Probability of win without change: {round(initial_selection,2)}%")
    print(f"Probability of win change the initial selection: {round(alternative_door,2)}%")


if __name__ == '__main__':
    simulation()
    #statistical_formula(3)
    #statistical_formula(4)
    #statistical_formula(5)
    #statistical_formula(10)
    #statistical_formula(50)
