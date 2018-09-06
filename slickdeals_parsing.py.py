import requests
from bs4 import BeautifulSoup as bs

page = requests.get('https://slickdeals.net/')
soup = bs(page.text, 'html.parser')


item_store = soup.find_all('a', {'class': 'itemStore'})
item_store_values = [x.get_text() for x in item_store]
for value in item_store_values:
	print(value)
# Put values into data frame.

item_title = soup.find_all('a', {'class': 'itemTitle'})
item_title_values = [x.get_text() for x in item_title]
for value in item_title_values:
	print(value)
	print()
# Put values into data frame.

item_price = soup.find_all('div', {'class': 'itemPrice'})
item_price_values = [x.get_text() for x in item_price]
for value in item_price_values:
	print(value)
# Put values into data frame.

# Save data into excel sheet. 