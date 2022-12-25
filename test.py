import csv


class Details():
    #Importing necessary libraries
    import csv

    #Declaring class variables
    pay_rate = 0.6
    all=[]

    #Class constructer
    def __init__(self,name:str,price:float,quantity:int):
        assert price >=0,"price is less than zero !!"
        assert quantity >=0,"Quantity is less than zero !!"
        #assigning values to object's attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        Details.all.append(self)

    #declaring discount method
    def apply_discount(self):
        self.price = self.price*self.pay_rate

    def __repr__(self):
        return self.name + str(self.price)

    # declaring instantiation method
    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv','r') as reader:
            r = csv.reader(reader)
            for item in r:
                Details(name=item[0], price=int(item[1]), quantity=int(item[2]))

    @staticmethod
    def is_integer(num):
        if type(num) == int:
            return True


Details.instantiate_from_csv()
print(Details.all)

print(Details.is_integer(5.0))


#for instances in Details.__dict__:
#    print(instances.name)