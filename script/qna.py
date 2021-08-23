import os

files = os.listdir("../q-a/Audio - Q _ A")
files.sort()

for file in files:
    print('-   {}'.format(file.replace('.mp3', '').replace(' _ ', '&')))
    print("")
    print('    <audio controls preload="none">')
    print("")
    print('    <source src="https://mufidu.github.io/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("    </audio>")
    print("")