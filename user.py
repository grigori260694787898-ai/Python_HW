class User:

    def __int__ (self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
  
    def sayName(self):
        print("Меня зовут:" , self.fname)
    def saylName(self):
        print("Моя фамилия:, self.lname ")
    def sayall(self):
        print("Меня зовут:" , self.fname, "Моя фамилия:, self.lname")