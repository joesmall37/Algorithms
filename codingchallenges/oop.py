class CreditCard:
    def __init__(self, number, limit, company):
        self.number = number
        self.limit = limit
        self.company = company
        print('An instance of crdit card class has been created')

# my_card = instance of CredidCard class
# my_card = CreditCard()
# my_card.number = "110101"
# my_card.limit = 5000
# my_card.company = "silvers"

# # attriubute
# # what will belong to an instance of a class

# print(my_card.number)

# these attributes only apply to this instance


# construcotr = or __init


c1 = CreditCard(number="1112000", limit= '100', company = 'jon')

print(c1.number)
