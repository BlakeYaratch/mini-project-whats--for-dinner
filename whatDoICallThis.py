import random


def generator():
    print("What type of food would you like?")
    result = input("Fast Food, Fine Dining, Chinese, Fictional, Random: ")
    if result == "Fast Food":
        # All Fast Food Restraunts
        restraunts = ["McDonald's", "Wendy's", "In-N-Out Burger"]
        answer = random.choices(restraunts)
        print(answer)
        # Asking user if it wants a new restraunts under Fast Food
        print("Would you like a another try?")
        again = input("y / n ")
        # If yes (y) it pick a new (maybe the same) restraunt
        if again == "y":
            answer2 = random.choices(restraunts)
            print(answer2)
        else:
            print("Enjoy your food!")
    # All Fine Dining Restraunts
    elif result == "Fine Dining":
        restraunts = ["Krust Krab", "Lindey's", "G. Michael's Bistro & Bar"]
        answer = random.choices(restraunts)
        print(answer)
        # Asking user if it wants a new restraunts under Fine Dining
        print("Would you like a another try?")
        again = input("y / n ")
        # If yes (y) it pick a new (maybe the same) restraunt
        if again == "y":
            answer2 = random.choices(restraunts)
            print(answer2)
        else:
            print("Enjoy your food!")
    # All Chinese Restraunts
    elif result == "Chinese":
        restraunts = ["Ho-Toy", "Tiger + Lily", "Happy House"]
        answer = random.choices(restraunts)
        print(answer)
        # Asking user if it wants a new restraunts under Chinese
        print("Would you like a another try?")
        again = input("y / n ")
        # If yes (y) it pick a new (maybe the same) restraunt
        if again == "y":
            answer2 = random.choices(restraunts)
            print(answer2)
        else:
            print("Enjoy your food!")
    # All Fictional Restraunts
    elif result == "Fictional":
        restraunts = ["Central Perk", "Bob's Burgers", "Paunch Burger"]
        answer = random.choices(restraunts)
        print(answer)
        # Asking user if it wants a new restraunts under Fictional
        print("Would you like a another try?")
        again = input("y / n ")
        # If yes (y) it pick a new (maybe the same) restraunt
        if again == "y":
            answer2 = random.choices(restraunts)
            print(answer2)
        else:
            print("Enjoy your food!")
    # All Restraunts
    elif result == "Random":
        restraunts = ["Bob's Burgers", "Paunch Burger", "Central Perk", "Ho-Toy", "Tiger + Lily", "Happy House",
                      "Krust Krab", "Lindey's", "G. Michael's Bistro & Bar", "McDonald's", "Wendy's", "In-N-Out Burger"]  # That should be all restraunts
        answer = random.choices(restraunts)
        print(answer)
        # Asking user if it wants a new restraunts under Fictional
        print("Would you like a another try?")
        again = input("y / n ")
        # If yes (y) it pick a new (maybe the same) restraunt
        if again == "y":
            answer2 = random.choices(restraunts)
            print(answer2)
        else:
            print("Enjoy your food!")
    else:
        print("Please input on of thoes options")
        generator()
    # Used so you dont have to re-run pyton file in terminal
    goAgain = input("Do it again (y)")
    # Make Console easier to read (kind of)
    print("#############################################################################################################")
    if goAgain == "y":
        generator()
    else:
        print("Ok re-run the file")


generator()
