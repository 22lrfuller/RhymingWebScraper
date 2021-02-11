from RhymeZoneScrape import *
from RapLyricScrape import *
from RapToPoS import *

userIn = "FIRSTRUN"

# Help function
def printHelp():
	print("\n===============COMMANDS===============")
	print("lyric - enter a song name, returns song lyrics")
	print("rhyme - enter a word, returns a table of rhyming words")
	print("help - displays this message")
	print("quit - quits the program\n")

# Printing commands initially
printHelp()

# Looping through 
while (userIn.lower() != "quit" or userIn.lower() != "q"):
	if (userIn == "lyric"):
		lyricScrape(True)

	elif (userIn == "rhyme"):
		rhymeScrape(True)

	elif (userIn == "help"):
		printHelp()

	elif (userIn == "quit"):
		break

	elif (userIn != "FIRSTRUN"):
			print("Input was not understood, please try again.")

	userIn = input(": ").lower()
	print()