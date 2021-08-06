import os

files = os.listdir("../tadabbur/Audio - Tadabbur Quran")
files.sort()

for file in files:
    print(file)
    print('<audio controls preload="metadata">')
    print('<source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("Your browser does not support the audio element.")
    print("</audio>")
    print("")