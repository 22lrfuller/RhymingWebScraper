#
# UPDATE COMMENTS
#
import requests
from bs4 import BeautifulSoup
from WordFrequency import freqData

def rhymeScrape(output):
	newElems = []

	# Taking a word and searching it on the website.
	word = input("Enter a Word: ")

	URL = 'https://www.rhymezone.com/r/rhyme.cgi?Word=' + word + '&typeofrhyme=perfect&org1=syl&org2=l&org3=y'
	results = BeautifulSoup(requests.get(URL).content, 'html.parser')

	# Filtering the contents of the page into the tags containing the rhyming words.
	jobElems = results.find_all('a', class_='r')

	# Getting rid of words that are less "good" rhymes to have better end results.
	for x in range(len(jobElems) - 1, -1, -1):
		if (str(jobElems[x])[10] == "d" or str(jobElems[x])[19] == "r"):
			jobElems.pop(x)
			x -= 1

	# Taking the tags in the list and turning them into strings without added html.
	# The words are then cross referenced with data from Google on word frequency.
	# If the word doesn't appear in the data, it is removed, otherwise it is
	# put into a list along with the frequency of that word in the data.
	for x in range(len(jobElems)):
		splitter = str(jobElems[x]).index("\">") + 2
		word = str(jobElems[x])[splitter:len(str(jobElems[x])) - 4]
		if (not ('\xa0' in word) and word in freqData):
			newElems.append([freqData[word], word])

	# Sorting the words by decreasing frequency.
	newElems = sorted(newElems, key = lambda freq: freq[0], reverse = True)

	if (not output):
		for x in range(len(newElems)):
			newElems[x] = newElems[x][1]
		return newElems

	# Determining longest word for string formatting
	longWord = newElems[0]
	for x in range(len(newElems)):
		if (len(newElems[x][1]) > len(longWord)):
			longWord = newElems[x][1]

	# Setting a minimum in case the length of the longest is shorter than "Word"
	longWord = len(longWord) + 2
	if (longWord < 4):
		longWord = 6

	# Printing a table of the words with their rank of frequency
	print("\n-------------" + "-" * (longWord + 1))
	print("| Frequency |" + "Word".center(longWord, " ") + "|")
	print("|    Rank   |" + " " * longWord + "|")
	print("-------------" + "-" * (longWord + 1))

	for x in range(len(newElems)):
		print("|" + str(x + 1).center(11, ' ') + "|", end="")
		print(newElems[x][1].center(longWord, ' ') + "|")

	print("-------------" + "-" * (longWord + 1))
