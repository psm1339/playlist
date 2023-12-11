import requests
from bs4 import BeautifulSoup

response = requests.get("https://dak.gg/valorant?hl=ko/")

print(response.status_code)

