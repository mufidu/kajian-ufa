import os

files = os.listdir("../silsilah-hati/Audio - Silsilah Hati")
files.sort()

for file in files:
    print('-   {}'.format(file.replace('.mp3', '')))
    print("")
    print('    <audio controls preload="none">')
    print("")
    print('    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("    </audio>")
    print("")