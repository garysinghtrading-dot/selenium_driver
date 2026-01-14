import random
import requests
from bs4 import BeautifulSoup

class GetAnchorTagUrl:
	def __init__(self):
		self.urls = [
      "https://www.accountplusfinance.com/education",
      "https://www.accountplusfinance.com/insights",
      "https://www.accountplusfinance.com/ideas",
    ] # list of urls to start from
		self.base_url = "http://www.accountplusfinance.com"

	def set_start_url(self):
		rand_int = random.randint(0, len(self.urls)-1)
		return self.urls[rand_int]

	def make_request_set_anchor_tag(self):
		start_url = self.set_start_url()
		response = requests.get(start_url)
		soup = BeautifulSoup(response.content, 'html.parser')
		anchor_tags = soup.find_all("a")
		random_a_tag = random.choice(anchor_tags)
		random_as_tag_href = random_a_tag['href']
		return self.base_url + random_as_tag_href

	def get_starting_url(self):
		created_url = self.make_request_set_anchor_tag()
		return created_url
