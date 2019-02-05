# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name 
        self.products = []


    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!

        self.products.append(product) 



    def print_products(self):
       for product in self.products :

        print(product)


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name 
        self.description = description
        self.price = price 

    def __str__(self):
        # your code goes here!
        return "(%s, %s, %s)" % (self.name, self.description, self.price) 


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0 
        for Product in self.products :
            total += Product.price
        return total
     

    def print_receipt(self):
       
        for product in self.products : 
            print ("your products are: %s" % product)

        print ("your total price is: %s" % self.get_total_price())
    

    def checkout(self):

        # your code goes here!
        print ("your reciept is ")
        self.print_receipt()
        x = input("do you confirm ? Yes / No ")
        if x.lower() == "Yes":
            print("your order has been confirmed")
        elif x == "No":
            print("your order has been cancelled")
        else :
            print ("you did not choose Yes or No")
            self.checkout()