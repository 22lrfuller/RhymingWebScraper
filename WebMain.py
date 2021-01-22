import requests
from bs4 import BeautifulSoup

wordInput = input("Enter a Word: ")
URL = 'https://www.rhymezone.com/r/rhyme.cgi?Word=' + wordInput + '&typeofrhyme=perfect&org1=syl&org2=l&org3=y'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup

jobElems = results.find_all('a', class_='r')
newElems = []

for x in range(len(jobElems) - 1, -1, -1):
	if (str(jobElems[x])[10] == "d"):
		jobElems.pop(x)
		x -= 1
	if (str(jobElems[x])[19] == "r"):
		jobElems.pop(x)
		x -= 1

print()

for elem in jobElems:
	splitter = str(elem).index("\">") + 2
	elem = str(elem)[splitter:len(str(elem)) - 4]
	print(elem)