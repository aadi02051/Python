from test import Details


class Phone(Details):
    def __init__(self,name:str,price:int,total_phones:int):
        self.name = name
        self.price = price
        self.total_phones = total_phones

    @staticmethod
    def Number_of_phones_not_damaged(not_damaged,damaged):
        if not_damaged > damaged:
            return not_damaged-damaged
        else:
            return("Wrong input data")

Phone1 = Phone('Jio',500,5)
Phone1.broken_phone = 2
print(Phone1.Number_of_phones_not_damaged(Phone1.total_phones,Phone1.broken_phone))

Phone2 = Phone('Samsung',1500,15)
Phone2.broken_phone = 3
print(Phone1.Number_of_phones_not_damaged(Phone2.total_phones,Phone2.broken_phone))