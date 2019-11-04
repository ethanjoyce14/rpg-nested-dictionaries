# Ethan Joyce
# Ms. Cotcher
# CS30
# Period 1
# RPG Nested Dictionaries

# Character dictionaries
characters = {
    # Swordsman stats
    'swordsman' : {
        'weapon' : 'Sword',
        'armour' : 'Chestplate',
        'shield' : 0,
        'atkpwr' : 10,
        'dfns' : 5
    },
    # Axeman stats
    'axeman' : {
        'weapon' : 'Axe',
        'armour' : 'Mail Tunic',
        'shield' : 'Wooden Shield',
        'atkpwr' : 7,
        'dfns' : 7
    },
    # Mage stats
    'mage' : {
        'weapon' : 'Magic Stick',
        'armour' : 'Robe',
        'shield' : 0,
        'atkpwr' : 7,
        'dfns' : 1
    },
}


# Location dictionaries
locations = {
    'forest' : 'Waldurk Forest',
    'town' : 'Falador',
    'castle' : 'Varrock Fort'
}


# Inventory dictionaries
inventories = {
    'weapons' : 'Sword',
    'armour' : 'Chestplate'
    'shield' : 0
    'atkpwr' : 10
    'dfns' : 5
}


# Print statements
print("\nCharacters:\n")
chardict = dict(characters)
print(chardict)

print("\nLocations:\n")
locdict = dict(locations)
print(locdict)

print("\nInventories:\n")
invdict = dict(inventories)
print(invdict)