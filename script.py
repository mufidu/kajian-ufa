import os

files = os.listdir("Audio - Tematik")
for file in files:
    print(file)
    print("![](Audio%20-%20Tematik/{})".format(file.replace(" ", "%20")))