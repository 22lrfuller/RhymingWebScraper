#
# ADD COMMENTS
#
import requests
from bs4 import BeautifulSoup
import os
import re
from RapLyricScrape import lyricScrape

def rapPoS(song):
	directory = os.fsencode(os.getcwd() + "\\Rap Lyrics\\")
	dirStr = os.fsencode(os.getcwd() + "\\Rap Lyrics\\")
	dirStr = str(directory)[2:len(directory) - 1].replace("\\\\","\\")

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if (filename.endswith(".txt")):
			lyrics = lyricScrape(song, False)
			lyrics = re.sub(re.compile('\(.*?\)'), '', re.sub(re.compile('\[.*?\]'), '', lyrics))
			lyrics = lyrics.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
			lyrics = lyrics.split("\n")

			while ("" in lyrics):
				lyrics.remove("");

			for x in range(len(lyrics)):
				lyrics[x] = lyrics[x].replace("  ", " ")

			for x in range(len(lyrics) - 1, - 1, -1):
				lyrics[x] = lyrics[x].strip().split(" ")
				while ("" in lyrics[x]):
					lyrics[x] = lyrics[x].remove("");

<<<<<<< Updated upstream
			for x in lyrics:
				print(x)

rapPoS("hop off a jet")
=======
			# openFile = open(filename)
			continue
		else:
			continue
>>>>>>> Stashed changes
