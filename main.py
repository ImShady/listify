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
	units = ["cup", "cups", "ounce", "oz", "gram", "tablespoon", "tablespoons", "tbsp", "teaspoon", "teaspoons","tsp"]
	for ing in ing_strings:
		split_ing = ing.split()
		parsed_ing = {}

		if any(x in split_ing[1] for x in units):
			parsed_ing['amount'] = split_ing[0] 
			parsed_ing['unit'] = split_ing[1]
			parsed_ing['name'] = ' '.join(split_ing[2:])
		else:
			parsed_ing['amount'] = split_ing[0]
			parsed_ing['unit'] = "item"
			parsed_ing['name'] = ' '.join(split_ing[2:])

		parsed_ings.append(parsed_ing)

	return parsed_ings

def main():
	test_url = "http://allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/"
	print(parse_ings(fetch_ings(test_url)))
  
if __name__== "__main__":
  main()