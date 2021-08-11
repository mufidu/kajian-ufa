import os

files = os.listdir("../silsilah-hati/Audio - Silsilah Hati")
files.sort()

for file in files:
    print(file)
    print('<audio controls preload="none">')
    print('<source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("Your browser does not support the audio element.")
    print("</audio>")
    print("")