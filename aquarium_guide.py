"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
Guides users through the process of setting up and maintaining a freshwater or saltwater aquarium, including selecting the right fish, plants, and equipment for their specific needs.
September 25th,2026
"""

fish_database = {
    "freshwater" : [
       {
           "name": "Tetras",
           "minimum_gallons": 20,
           "farenheit": 72,
       },
       {
           "name": "Betta",
           "minimum_gallons": 5,
           "farenheit": 80,
       },
       {
           "name": "Danios",
           "minimum_gallons": 20,
           "farenheit": 70,
       },
       {
            "name": "Platys",
            "minimum_gallons": 20,
            "farenheit": 80,
       },
       {
            "name": "Corydoras",
            "minimum_gallons": 20,
            "farenheit": 75,
       }
    ],
    "saltwater": [
       {
           "name": "Clownfish",
           "minimum_gallons": 20,
           "Salinity": 1.025,
       },
       {
           "name": "Gramma",
           "minimum_gallons": 30,
           "Salinity": 1.025,
       },
       {
           "name": "Firefish",
           "minimum_gallons": 20,
           "Salinity": 1.020,
       },
       {
            "name": "Banggai",
            "minimum_gallons": 30,
            "Salinity": 1.023,
       },
       {
            "name": "Elacatinus",
            "minimum_gallons": 10,
            "Salinity": 1.023,
       }
    ]
}

plants_and_coral = {
    "freshwater": [
        {
            "name": "Java Fern",
            "lighting":"low", 
        },
        {
            "name": "Anubias",
            "lighting":"low",
        },
        {
            "name": "Amazon Swords",
            "lighting": "moderate"
        }
    ],
    "saltwater": [
        {
            "name": "Eelgrass",
            "lighting":"high"
        },
        {
            "name": "Chaetomorpha",
            "lighting":"moderate"
        },
        {
            "name": "Mangroves",
            "lighting":"moderate"
        }
    ]
}

aquarium_equipment = {
    "freshwater": ("tank", "filtration", "heater", "LED lighting", "substrate", "test kits", "dechlorinator"),
    "saltwater": ("tank", "filtration", "heater", "LED lighting", "live rock/ substrate", "test kits", "protein skimmer", "circulation pump", "marine salt")
}
