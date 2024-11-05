# NPC Random Generator-Created by James Kochan

## Summary
Hello! My name is James Kochan, I'm a freshman at Voorhees High school. I was tasked with making an NPC Generator for an open world game. The software I designed is easy to use, intuitive, and open for expansion by a coder more advanced than me (a whole lot of people!). In this README, I'll show some highlights of my software, and explain why they were coded like this.


## 🌟 Highlights


#### Lists

First, I made a few lists for my new function to call upon. Such as...

```
names = ["Alex", "Jamie", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Cameron", "Dakota", "Quinn"]
professions = ["Blacksmith", "Farmer", "Merchant", "Guard", "Scholar", "Thief", "Baker", "Fisherman", "Carpenter", "Healer"]
hometowns = ["Rivertown", "Eagle's Nest", "Sunfield", "Mystic Falls", "Stormhold", "Whiterun", "Greenshire", "Ironforge"]
```

These made it a lot easier, and possible for me, to make a pseudo random generator for things like names and professions.

#### The "generate_npcs" Function

The def feature was perhaps the most helpful in coding my project, it made the whole thing efficient to code, because I could use custom functions specialized to the task at hand.

```
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
```

In short, this function searches the lists **already created** for a random choice out of them to return to the user, such as the NPC's professions and heights.

```
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
```

This function helped the user interface be more dynamic, with "f floats" plugging in the random information found through the other functions.

## Conclusion

My "NPC Generator" has many uses for potential users. I intentionally made this program so that others could build off and use it for their own purposes. Things such as the lists are almost infinitely changeable, because the user can alter the lists for the functions to call upon whatever they wish. 

Effortless Creativity: Generate a vast array of NPCs, each with unique traits, backstories, and personalities.

Tailor-Made Characters: Customize your NPCs to fit any narrative or environment with ease.

Time-Saver Extraordinaire: Spend less time on character creation and more on crafting epic stories and gameplay.

Limitless Variety: From quirky shopkeepers to formidable foes, NPC Generator ensures no two characters are alike

*Have fun with my program!*
