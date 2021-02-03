import requests
from bs4 import BeautifulSoup
import re

def lyricScrape(song, output):
	if (song == None):
		# Searching the song on the website and getting the conents of the page
		song = input("Enter the song name: ")

	song = song.replace(" ", "+")
	URL = 'https://search.azlyrics.com/search.php?q=' + song
	results = BeautifulSoup(requests.get(URL).content, 'html.parser')

	# Filtering the content and finding the top link of the page
	jobElems = results.find_all('td', class_='text-left visitedlyr')
	URL = str(jobElems[0])[str(jobElems[0]).find("<a href=\"") + 9:str(jobElems[0]).find("\"><b>\"")]

	# Filtering the contents of the new page with the lyrics
	results = BeautifulSoup(requests.get(URL).content, 'html.parser')
	results = str(results)[str(results).find("licensing agreement. Sorry about that. -->") + 43:str(results).find("<!-- MxM banner -->")]

	# Using a regex to get rid of the excess html tags and manually removing
	# the ampersands that are also part of html.
	regex = re.compile('<.*?>')
	noHtml = re.sub(regex, '', results).replace('&amp;', '&').strip()

	if (not output):
		return noHtml

	# Finding the longest line of lyrics to use for formatting
	barLen = len(max(noHtml.splitlines(), key=len))

	# Splitting the string into lines and adding an extra space
	# before the first line and after the last.
	noHtml = noHtml.splitlines()
	noHtml.insert(0, "")
	noHtml.append("")

	# Printing the lyrics in a box
	print("+" + "=" * (barLen + 2) + "+")
	for x in range(len(noHtml)):
		print("|" + noHtml[x].center(barLen + 2, " ") + "|")
	print("+" + "=" * (barLen + 2) + "+")
	return None