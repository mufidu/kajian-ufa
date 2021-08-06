import os

files = os.listdir("../tematik/Audio - Tematik")
files.sort()

for file in files:
    print(file)
    print('<audio controls preload="metadata">')
    print('<source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("Your browser does not support the audio element.")
    print("</audio>")
    print("")