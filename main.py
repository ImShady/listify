from bs4 import BeautifulSoup
import requests

r = requests.get("http://allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/")

raw_data = r.text

soup = BeautifulSoup(raw_data, "html.parser")

for item in soup.find_all('span', {"class": "recipe-ingred_txt added"}):
    print(item.text)