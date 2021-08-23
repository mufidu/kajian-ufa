import os

files = os.listdir("../tadabbur/Audio - Tadabbur Quran")
files.sort()

for file in files:
    print('-   {}'.format(file.replace('.mp3', '')))
    print("")
    print('    <audio controls preload="none">')
    print("")
    print('    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("    </audio>")
    print("")

