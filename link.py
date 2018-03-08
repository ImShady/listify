from bs4 import BeautifulSoup
import requests
from ingredient import Ingredient

class Link():
	def __init__(self, url):
		self.url = url
		self.parse_ings(self.fetch_ings(url))

	def parse_ings(self, ing_strings):
		self.parsed_ings = []
		units = ["cup", "cups", "ounce", "oz", "gram", "tablespoon", "tablespoons", "tbsp", "teaspoon", "teaspoons","tsp"]
		
		for ing in self.ing_strings:
			split_ing = ing.split()
			ing = Ingredient(split_ing[0], split_ing[1] if split_ing[1] in units else "item", ' '.join(split_ing[2:]))
			self.parsed_ings.append(ing)

		return self.parsed_ings

	def fetch_ings(self, url):
		r = requests.get(url) # this is how you comment in Python! =)

		raw_data = r.text
		self.ing_strings = []
		soup = BeautifulSoup(raw_data, "html.parser")

		for item in soup.find_all('span', {"class": "recipe-ingred_txt added"}):
		    self.ing_strings.append(item.text)

		return self.ing_strings