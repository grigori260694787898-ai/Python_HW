from address import Address

class Mailing:
    def __init__(self, to_address, from_address, coast, track):
        self.to_address = to_address
        self.from_address = from_address
        self.coast = coast
        self.track = track

    def __str__(self):
        from_address_str = ", ".join ([str(from_address_) for from_address in self.from_address])
        return f"{to_address} отправитель: {from_address_str}"
    
   



