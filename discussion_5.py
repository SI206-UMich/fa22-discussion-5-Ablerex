import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for c in sentence:
		if c == 'a' or c == "A":
			total += 1 
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	# setting the current stock item to the max stock item by accessing it using indexing 
	# checking if the item is greater than the current max stock item
	# checking if the item is greater than the current max stock item
	def get_max_stock(self):
		"""max_stock_item = self.items[0] 
		for item in self.items:
			if item.stock > max_stock_item.stock: 
				max_stock_item = item  
		return item """
		stock_list = []
		for item in self.items:
			stock_list.append(item.stock)
			print(stock_list)
		for item in self.items:
			if item.stock != max(stock_list):
				print(item)
				continue
			else:
				print(item)
				return item




	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		price_list = []
		for item in self.items:
			price_list.append(item.price)
			print(price_list)
		for item in self.items:
			if item.price != max(price_list):
				print(item)
				continue
			else:
				print(item)
				return item



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a(" "), 0, "Expected value = 0")
		self.assertEqual(count_a("a"), 1, "Expected value = 1")
		self.assertEqual(count_a("bab"), 1, "Expected value = 1")
		self.assertEqual(count_a("Apples, Bananas, Eggs, AAAA"), 8, "Expected value = 8")
		self.assertEqual(count_a("GaA"), 2, "Expected value = 2")


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		w1 = Warehouse()
		self.assertEqual((len(w1.items) == 0), True, "expected value = 0")
		w1.add_item(self.item1)
		self.assertEqual((len(w1.items) == 1), True, "expected value = 1")


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		stock_list1 = [self.item1, self.item2, self.item3, self.item4, self.item5]
		stock_list2 = [self.item2, self.item4]
		stock_list3 = [self.item1, self.item3, self.item5]
		w1 = Warehouse()
		for item in stock_list1:
			w1.add_item(item)

		w2 = Warehouse()
		for item in stock_list2:
			w2.add_item(item)

		w3 = Warehouse()
		for item in stock_list3:
			w3.add_item(item)

		self.assertEqual((w1.get_max_stock()), self.item3, "Expected stock item with max stock = Water")
		self.assertEqual((w2.get_max_stock()), self.item4, "Expected stock item with max stock = Fanta")
		self.assertEqual((w3.get_max_stock()), self.item3, "Expected stock item with max stock = Water")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		stock_list1 = [self.item1, self.item2, self.item3, self.item4, self.item5]
		stock_list2 = [self.item2, self.item4]
		stock_list3 = [self.item1, self.item3, self.item5]
		w1 = Warehouse()
		for item in stock_list1:
			w1.add_item(item)

		w2 = Warehouse()
		for item in stock_list2:
			w2.add_item(item)

		w3 = Warehouse()
		for item in stock_list3:
			w3.add_item(item)

		self.assertEqual((w1.get_max_price()), self.item1, "Expected stock item with max price = Beer")
		self.assertEqual((w2.get_max_price()), self.item2, "Expected stock item with max price = Cider")
		self.assertEqual((w3.get_max_price()), self.item1, "Expected stock item with max price = Beer")


		

def main():
	unittest.main()

if __name__ == "__main__":
	main()