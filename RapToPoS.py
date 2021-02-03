import requests
from bs4 import BeautifulSoup
import os
from RapLyricScrape import lyricScrape

def rapPoS(song):
	directory = os.fsencode(os.getcwd() + "\\Rap Lyrics\\")
	dirStr = os.fsencode(os.getcwd() + "\\Rap Lyrics\\")
	dirStr = str(directory)[2:len(directory) - 1].replace("\\\\","\\")

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if (filename.endswith(".txt")):
			lyrics = lyricScrape(song, True)
			print(lyrics)
			lyrics = lyrics.splitlines()

			for x in range(len(lyrics)):
				lyrics[x] = lyrics[x].split(" ")

			print(lyrics)

			# openFile = open(filename)
			continue
		else:
			continue

rapPoS("hop off a jet")