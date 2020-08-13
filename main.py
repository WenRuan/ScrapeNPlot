import requests
from bs4 import BeautifulSoup

#####Scraping the website

#Request information
base = 'http://books.toscrape.com/'
baseURL = 'http://books.toscrape.com/index.html'
site = requests.get(baseURL)

Bookstore = BeautifulSoup(site.content, 'html.parser')


class Genre:

	def __init__(self, name, link):
		self.name = name
		self.link = link


genreArr = []


#Scrape the Genre and add correlating URL to each genre
GenreSection = Bookstore.find('div', class_='side_categories')
GenreNav = GenreSection.find('ul', class_='nav')
GenreList = GenreNav.find('ul')
GenreItem = GenreList.find_all('li')
for genreItem in GenreItem:
	name = genreItem.find('a')
	genre = Genre(name.text.strip(), name['href'])
	genreArr.append(genre)




#Go through each genre and grab information from the books
print('For' + ' ' + genreArr[0].name + ' ' + 'genre:')
page = base + genreArr[0].link
site = requests.get(page)

soup = BeautifulSoup(site.content, 'html.parser')

Section = soup.find('section')
Product = Section.find_all('article', class_= 'product_pod')
for info in Product:
	title = info.find('a')

print(title.text.strip())







