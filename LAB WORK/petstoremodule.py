class petstore:
    def __init__(self, Pet_Type, Gender, Age, Price, Status):
        self.Pet_Type = Pet_Type
        self.Gender = Gender
        self.Age = Age
        self.Price = Price
        self.Status = Status
        return
    def print_petstore(self):
        petstorelist1 = []
        pet1 =["Dog - Rotwiller", "Male", "2 Years", "5 thousand", "Available"]
        pet2 =["Cat - Siamese", "Female", "1 Year", "2 thousand", "Available"]
        pet3 =["Fish - Goldfish", "Unknown", "6 months", "500", "Sold"]
        petstorelist1.append(pet1)
        petstorelist1.append(pet2)
        petstorelist1.append(pet3)
        for pet in petstorelist1:
            print(pet)
        