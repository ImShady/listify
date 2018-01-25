from bs4 import BeautifulSoup
import requests


def fetch_ings(url):
	r = requests.get(url)

	raw_data = r.text
	ing_strings = []
	soup = BeautifulSoup(raw_data, "html.parser")

	for item in soup.find_all('span', {"class": "recipe-ingred_txt added"}):
	    ing_strings.append(item.text)

	return ing_strings

def parse_ings(ing_strings):
	parsed_ings = []
	units = ["cup", "cups", "ounce", "oz", "gram", "tablespoon", "tbsp", "teaspoon", "tsp"]
	for ing in ing_strings:
		# if string1 equals string2:
		# 	DO_THIS_HERE
		# elif SECOND CASE:
		# else:
		# 	LAST CASE
		parsed_ing = {}
		parsed_ing['name'] = NAME_HERE
		parsed_ing['amount'] = AMOUNT_HERE
		parsed_ing['unit'] = UNIT_HERE
		parsed_ings.append()

	return parsed_ings

def main():
	test_url = "http://allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/"
	parse_ings(fetch_ings(test_url))
  
if __name__== "__main__":
  main()