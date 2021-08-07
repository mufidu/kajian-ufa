import os

files = os.listdir("../tadabbur/Audio - Tadabbur Quran")
files.sort()

for file in files:
    print('-   {}'.format(file))
    print("")
    print('    <audio controls preload="metadata">')
    print("")
    print('    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/{}" type="audio/mpeg">'.format(file.replace(" ", "%20")))
    print("    Maaf, browser Anda tidak mendukung pemutaran audio.")
    print("    </audio>")
    print("")

