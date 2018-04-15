from bs4 import BeautifulSoup
import requests
import sys
from ingredient import Ingredient
from link import Link

def main():
	url = Link(sys.argv[1]) # send in URL as a parameter; the line below is useful for testing
	# url = Link("http://allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/")
	for ing in url.parsed_ings:
		print(str(ing.amount) + " " + ing.unit + " " + ing.name)

  
if __name__== "__main__":
  main()