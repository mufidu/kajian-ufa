import os

files = os.listdir("../q-a/Audio - Q _ A")
files.sort()

for file in files:
    print(file)
    print('<audio controls preload="none">')
    print('<source src="https://mufidu.github.io/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("Your browser does not support the audio element.")
    print("</audio>")
    print("")