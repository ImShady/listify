
class Ingredient():

	def __init__(self, amount, unit, name):
		self.amount = self.convert_to_decimal(amount)
		self.unit = unit
		self.name = name

	def convert_to_decimal(self, amount):
	    try:
	        return float(amount)
	    except ValueError:
	        num, denom = amount.split('/')
	        return float(num) / float(denom)

	def convert_to_grams(self):
		pass