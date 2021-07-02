class Hockey:
    def __init__(self, name, city, founded_in, stanley_cups):
        self.name = name
        self.city = city
        self.founded_in = founded_in
        self.stanley_cups = stanley_cups

    def __str__(self):
        return f"The {self.name} is based in {self.city} and was founded in {self.founded_in}. They have won {self.stanley_cups} Stanley Cups."

canadiens = Hockey("Montreal Canadiens", "Montreal", 1909, 23)
leafs = Hockey("Toronto Maple Leafs", "Toronto", 1917, 13)

print(canadiens)
print(leafs)