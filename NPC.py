import random

# Lists of potential names, professions, and hometowns for NPCs
names = ["Alex", "Jamie", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Cameron", "Dakota", "Quinn"]
professions = ["Blacksmith", "Farmer", "Merchant", "Guard", "Scholar", "Thief", "Baker", "Fisherman", "Carpenter", "Healer"]
hometowns = ["Rivertown", "Eagle's Nest", "Sunfield", "Mystic Falls", "Stormhold", "Whiterun", "Greenshire", "Ironforge"]

def generate_npcs(num_npcs):
    npcs = []
    
    for _ in range(num_npcs):
        npc = {
            "name": random.choice(names),
            "age": random.randint(18, 70),  # age between 18 and 70
            "height": round(random.uniform(150, 200), 1),  # height in cm as a float
            "is_friendly": random.choice([True, False]),  # boolean for friendliness
            "profession": random.choice(professions),
            "hometown": random.choice(hometowns)
        }
        npcs.append(npc)
    return npcs

def print_npcs(npcs):
    for idx, npc in enumerate(npcs):
        print(f"NPC {idx + 1}:")
        print(f"  Name: {npc['name']}")
        print(f"  Age: {npc['age']}")
        print(f"  Height: {npc['height']} cm")
        print(f"  Friendly: {'Yes' if npc['is_friendly'] else 'No'}")
        print(f"  Profession: {npc['profession']}")
        print(f"  Hometown: {npc['hometown']}")
        print()

# Main program execution
num_npcs = int(input("Enter the number of NPCs to generate: "))
npcs = generate_npcs(num_npcs)
print_npcs(npcs)
