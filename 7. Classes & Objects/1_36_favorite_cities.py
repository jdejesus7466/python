if __name__ == "__main__":

    class City:
        def __init__(self, name, country, population, landmarks):
            self.name = name
            self.country = country
            self.population = population
            self.landmarks = landmarks
        
    las_vegas = City("Las Vegas", "USA", 660929, "The Strip")
    orlando = City("Orlando", "USA", 320742, "Disney World")
    manila = City("Manila", "Philippenes", 1846513, "Metro Manila")

    print(vars(las_vegas))
    print(vars(orlando))
    print(vars(manila))