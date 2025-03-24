if __name__ == "__main__":

    class Pokemon:
        def __init__(self, entry, name, types, description, is_caught):
            self.entry = entry
            self.name = name
            self.types = types
            self.description = description
            self.is_caught = is_caught
        
        def speak(self):
            print(self.name + " " + self.name)
        
        def display_details(self):
            print("Entry Number:", self.entry)
            print("Name:", self.name)
            print("Type:", self.types)
            print("Description:", self.description)
    
    charizard = Pokemon("0006", "Charizard", "Fire, Flying", "Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.", False)
    pikachu = Pokemon("0025", "Pikachu", "Electric", "When several of these Pokémon gather, their electricity could build and cause lightning storms.", True)
    vaporeon = Pokemon("0134", "Vaporeon", "Water", "	Lives close to water. Its long tail is ridged with a fin which is often mistaken for a mermaid's.", False)

    pikachu.speak()

    pikachu.display_details()
    charizard.display_details()
    vaporeon.display_details()