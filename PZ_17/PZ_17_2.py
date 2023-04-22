class Transport:
    def __init__(self, brand, model, release_date):
        self.brand = brand
        self.model = model
        self.release_date = release_date


class Gruzovik(Transport):
    def __init__(self, brand, model, release_date, gruzovik_type):
        super().__init__(brand, model, release_date)
        self.gruzovik_type = gruzovik_type

