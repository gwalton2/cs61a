import requests
from bs4 import BeautifulSoup, SoupStrainer
from decimal import Decimal
def get_stock(ticker):
	url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	company = soup.find('h1', attrs={'data-reactid': '7'}).text
	price = soup.find('span', attrs={'data-reactid': '36'}).text
	percent_change = soup.find('span', attrs={'data-reactid': '37'}).text
	print('current price:', price)
	print('Today', company, 'changed by', percent_change)


