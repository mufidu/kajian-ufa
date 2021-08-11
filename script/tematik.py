import os

files = os.listdir("../tematik/Audio - Tematik")
files.sort()

for file in files:
    print('-   {}'.format(file))
    print("")
    print('    <audio controls preload="none">')
    print("")
    print('    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("    </audio>")
    print("")

