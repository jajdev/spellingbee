import re

# load dictionary into array # 
file = open("/usr/share/dict/words", "r")
words = re.sub("[^\w]", " ",  file.read()).split()
file.close()

# algorithm to find all possible spelling bee pantagrams #
spellingBee = []
for word in words:
	if len(word) >= 7:
		characters = set()

		for i in word:
			characters.add(i)

		if len(characters) == 7:
			#print(word + " is a spelling bee word")
			spellingBee.append(word)

print ("There are " + str(len(spellingBee)) + " spelling bee words")

# algorithm to find all possible spelling bee words for today's set #
todaysSet = {'r', 'd', 'p', 'o', 'a', 'u', 'm'}
todaysWords = []
specialLetter = 'r'
for word in words:
	characters = set()
	match = "True"

	for i in word:
		if i not in todaysSet or len(word) < 4:
			match = "False"
			break
		else:
			characters.add(i)

	if match == "True" and specialLetter in characters:
		todaysWords.append(word)

print("There are " + str(len(todaysWords)) + " spelling bee words today and they are:")
for word in todaysWords:
	print(word)

