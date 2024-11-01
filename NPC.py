# NPC Generator for an Open-World Video Game

import random
import time
import math

# Function to generate NPCs
def generate_npcs(num_npcs):
    npc_list = []
    
    # Prompt user for NPC names
    npc_names = input("Enter names for the NPCs, separated by commas: ").split(',')
    
    # Loop to create NPCs
    for i in range(num_npcs):
        name = npc_names[i % len(npc_names)].strip()  # Use names provided by user
        age = random.randint(18, 65)  # Random age between 18 and 65
        height = round(random.uniform(1.5, 2.0), 2)  # Random height in meters
        is_villain = random.choice([True, False])  # Random boolean for villain status
        profession = random.choice(['Warrior', 'Mage', 'Thief', 'Merchant', 'Healer'])  # Random profession
        
        # Create NPC dictionary
        npc = {
            'Name': name,
            'Age': age,
            'Height (m)': height,
            'Is Villain': is_villain,
            'Profession': profession
        }
        
        npc_list.append(npc)  # Add NPC to the list
    
    return npc_list

# Function to display NPCs
def display_npcs(npcs):
    for npc in npcs:
        print(f"Name: {npc['Name']}, Age: {npc['Age']}, Height: {npc['Height (m)']}m, Is Villain: {npc['Is Villain']}, Profession: {npc['Profession']}")

# Main execution
if __name__ == "__main__":
    num_npcs = 10  # Number of NPCs to generate
    npcs = generate_npcs(num_npcs)  # Generate NPCs
    display_npcs(npcs)  # Display NPCs
