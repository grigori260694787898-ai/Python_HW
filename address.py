class Address:
    def __int__ (self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
    def __str__(self):
        return f"{self.index} {self.city}, {self.street}, {self.house}, {self.apartment}"








    
        