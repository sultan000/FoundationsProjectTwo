# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "NAS"

def welcome():
	print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
	for store in stores :
		print (store.name)

def get_store(store_name):
	for store in stores:
		if store_name != store.name :
		 return False
		
	return store

def pick_store():
	
	print_stores()
	my_store = input("Pick a store by typing its name Or type 'checkout' to pay your bills")
	if my_store == 'checkout': 
		return "checkout"
	elif get_store(my_store) : 
		return get_store(my_store)
	else:
		print("Invalid store")

		pick_store()      

# while store_picked.lower () != "checked"
# get_store(store_picked):
# return get_store(store_picked)
#else:
 #   store_picked = input(invalid)
def pick_products(cart, picked_store):
	picked_store.print_products()
	my_product = input("what do you want to add to the cart?")
	while my_product.lower() != 'back' :
		for product in picked_store.product : 
			if product.name == my_product :
				cart.add_to_cart(product)
				my_product = input("what else do you want?")
	

def shop():
	
	cart = Cart()
	store = pick_store()
	while store != "checkout" :
		pick_products(cart, store)
		store = pick_store()
	cart.checkout()

def thank_you():
	print("Thank you for shopping with us at %s" % site_name)
