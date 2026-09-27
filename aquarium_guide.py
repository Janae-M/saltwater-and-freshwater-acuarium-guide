"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
Guides users through the process of setting up and maintaining a freshwater or saltwater aquarium, including selecting the right fish, plants, and equipment for their specific needs.
September 25th,2026
"""

fish_database = {
    "freshwater" : [
       {
           "name": "Tetras", "minimum_gallons": 20, "fahrenheit": 72
       },
       {
           "name": "Betta", "minimum_gallons": 5, "fahrenheit": 80
       },
       {
           "name": "Danios", "minimum_gallons": 20, "fahrenheit": 70
       },
       {
            "name": "Platys", "minimum_gallons": 20, "fahrenheit": 80
       },
       {
            "name": "Corydoras", "minimum_gallons": 20, "fahrenheit": 75
       }
    ],
    "saltwater": [
       {
           "name": "Clownfish", "minimum_gallons": 20, "Salinity": 1.025
       },
       {
           "name": "Gramma", "minimum_gallons": 30, "Salinity": 1.025
       },
       {
           "name": "Firefish", "minimum_gallons": 20, "Salinity": 1.020
       },
       {
            "name": "Banggai", "minimum_gallons": 30, "Salinity": 1.023
       },
       {
            "name": "Elacatinus", "minimum_gallons": 10, "Salinity": 1.023
       }
    ]
}

plants = {
    "freshwater": [
        {
            "name": "Java Fern", "lighting":"low" 
        },
        {
            "name": "Anubias", "lighting":"low",
        },
        {
            "name": "Amazon Swords", "lighting": "moderate"
        }
    ],
    "saltwater": [
        {
            "name": "Eelgrass", "lighting":"high"
        },
        {
            "name": "Chaetomorpha", "lighting":"moderate"
        },
        {
            "name": "Mangroves", "lighting":"moderate"
        }
    ]
}

aquarium_equipment = {
    "freshwater": ("tank", "filtration", "heater", "LED lighting", "substrate", "test kits", "dechlorinator"),
    "saltwater": ("tank", "filtration", "heater", "LED lighting", "substrate", "test kits", "live rock", "protein skimmer", "circulation pump", "marine salt")
}

aquarium = {
    "type": "",
    "tank size": 0,
    "budget": 0,
    "decorations": [],
    "fish": [],
    "equipment": []
}

def user_aquarium_type():
    """asks users to choose between a freshwater or saltwater aquarium"""

    while True:
        aquarium_type = input(
            "Would you like to create a freshwater or saltwater aquarium?"
        ).lower()
        if aquarium_type == "freshwater":
            return aquarium_type
        elif aquarium_type == "saltwater":
            return aquarium_type
        else:
            print("Please enter either 'freshwater' or 'saltwater'.")

def user_tank_size():
    """retrieves users prefered tank size by gallons"""

    while True:
        try:
            size = float(input(
                "How many gallons of water will your tank contain?"
            ))
            if size > 0:
                return size
            else:
                print("Tank size must be greater than 0.")

        except ValueError:
            print("Please enter a number.")

def user_budget():
    """users budget for their aquarium build"""

    while True:
        try:
            budget = float(input(
                "What is your budget (in dollars) for this build?"
            ))
            if budget > 0:
                return budget 
            else:
                print("Budget must be greater than 0.")
        except ValueError:
            print("Please enter a number.")

def get_decorations(aquarium_type):
    """users choices for freshwater or saltwater plants"""

    options = plants[aquarium_type]
    selected = []

    if aquarium_type == "freshwater":
        category = "plants"
    else:
        category = "saltwater plants"
    while True:
        print("\nChoose your", category + ":")

        for number in range(len(options)):
            print(
                number + 1,
                ".",
                options[number]["name"],
                "- Lighting:",
                options[number]["lighting"]
            )

        print("0. Done")

        choice = input("Enter your choice: ")

        if choice.isdigit():

            choice = int(choice)

            if choice == 0:
                break
            elif 1 <= choice <= len(options):
                selected.append(options[choice - 1])
                print(
                    options[choice -1]["name"], "added!"
                )
            else:
                print("Invalid choice.")

        else:
            print("Please enter a number.")

    return selected

def find_fish(aquarium):
    """valid fish based on aquarium type and size""" 
    aquarium_type = aquarium["type"]
    tank_size = aquarium["tank size"]

    possible_fish = []

    for fish in fish_database[aquarium_type]:
        if tank_size >= fish["minimum_gallons"]:
            possible_fish.append(fish)

    return possible_fish
