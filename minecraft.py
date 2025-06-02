import json
from fuzzywuzzy import process

class MinecraftAI:
    def __init__(self, version="1.20"):
        self.version = version
        self.data = self.load_sample_data()  # In practice, load from external JSON files
        self.entity_names = self.compile_entity_names()

    def load_sample_data(self):
        # Sample data for demonstration; replace with actual JSON loading from minecraft-data
        return {
            "entities": {
                "zombie": {
                    "health": "20 hearts",
                    "attack": "2.5 hearts",
                    "spawn": "Overworld at night or probably in dark areas",
                    "drops": "Rotten Flesh",
                    "description": "A hostile undead mob that attacks players and villagers."
                },
                "ender_dragon": {
                    "health": "200 hearts",
                    "attack": "Variable (melee, breath attack)",
                    "spawn": "The End",
                    "drops": "Dragon Egg, Experience",
                    "description": "The final boss of Minecraft, found in The End."
                }
            },
            "items": {
                "diamond_sword": {
                    "damage": "7 hearts",
                    "durability": "1561 uses",
                    "crafting": "2 Diamonds + 1 Stick (Crafting Table)",
                    "description": "A powerful melee weapon made from diamonds."
                }
            },
            "blocks": {
                "obsidian": {
                    "hardness": "50",
                    "blast_resistance": "1200",
                    "description": "A tough block used for portals and strong structures."
                }
            }
        }

    def compile_entity_names(self):
        # Compile all entity names for fuzzy matching
        names = []
        for category in ["entities", "items", "blocks"]:
            names.extend(self.data[category].keys())
        return names

    def process_query(self, query):
        query = query.lower().strip()
        tokens = query.split()

        # Check for version specification
        if "version" in query:
            version = [t for t in tokens if t.startswith("1.") or t == "latest"]
            if version:
                return f"Currently set to version {self.version}. Specify a version like '1.19' if needed."

        # Identify entity using fuzzy matching
        entity = self.identify_entity(tokens)
        if not entity:
            return "I'm sorry, I couldn't recognize any Minecraft entity in your query."

        # Identify attribute or intent
        attribute = self.identify_attribute(tokens)

        if attribute:
            return self.get_attribute(entity, attribute)
        else:
            return self.get_description(entity)

    def identify_entity(self, tokens):
        # Use fuzzy matching to find the closest entity name
        query_str = " ".join(tokens)
        best_match, score = process.extractOne(query_str, self.entity_names)
        if score > 80:  # Threshold for match confidence
            return best_match
        return None

    def identify_attribute(self, tokens):
        # Define attribute keywords
        attribute_keywords = {
            "health": ["health", "hp", "hearts"],
            "attack": ["attack", "damage", "dmg"],
            "spawn": ["spawn", "where", "found"],
            "drops": ["drops", "loot"],
            "crafting": ["craft", "recipe", "make"],
            "durability": ["durability", "uses"],
            "hardness": ["hardness", "strength"],
            "blast_resistance": ["blast", "resistance"]
        }
        for attr, keywords in attribute_keywords.items():
            if any(keyword in tokens for keyword in keywords):
                return attr
        return None

    def get_attribute(self, entity, attribute):
        # Search across categories for the entity
        for category in ["entities", "items", "blocks"]:
            if entity in self.data[category]:
                if attribute in self.data[category][entity]:
                    return f"The {attribute} of {entity} is {self.data[category][entity][attribute]}."
                else:
                    return f"I don’t have {attribute} info for {entity}."
        return f"I don’t recognize '{entity}' in my data."

    def get_description(self, entity):
        # Provide a general description
        for category in ["entities", "items", "blocks"]:
            if entity in self.data[category]:
                desc = self.data[category][entity].get("description", "No description available.")
                return f"{entity.capitalize()}: {desc}"
        return f"I don’t recognize '{entity}' in my data."

def main():
    ai = MinecraftAI()
    print(f"Welcome to the Minecraft AI (Version {ai.version})!")
    print("Ask me anything about Minecraft (e.g., 'What is the health of a zombie?' or 'Tell me about obsidian'). Type 'exit' to quit.")
    
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = ai.process_query(query)
        print("AI:", response)

if __name__ == "__main__":
    main()








    