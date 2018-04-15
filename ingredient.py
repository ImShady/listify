# grams per measurement (metric conversions)
per_gr_coversion = {
	'tsp': 5, 
	'tbsp': 15, 
	'cup': 250, 
	'pint': 473.176475, 
	'quart': 946.35295, 
	'kg': 1000, 
	'oz': 28.349523125, 
	'lb': 453.59237, 
	'mg': 0.001
}

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

	def convert_to_grams(self, amount, unit):
		return float(amount) * dict.get(per_gr_coversion, unit, 1)

	def convert_from_grams(self, amount, unit):
		return float(amount) / dict.get(per_gr_coversion, unit, 1)
