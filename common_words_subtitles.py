from collections import Counter
from googletrans import Translator

# Getting the file text
print("\n \n   Subtranslater - translates and sorts subtitles by uses. \n \n")
path = input("Enter the path for the subtitles: ")
text = open(path, 'r', encoding="utf-8").read()
listed  = text.split()

# Printing overview
print("Overview:")
c = Counter(listed).most_common()
counter = list(reversed(c))
for idx, word in enumerate(counter):
    if idx > (len(counter) - 20):
        print(word)

# Saving the file
if (input("\nSave the file y/n: ") == "y"):
    with open(r"C:\Users\Walter\Desktop\learn_words.txt", "w", encoding="utf-8") as f:
        for word in list(c):
            # Adjusting word
            new_word = str(word).replace("(", "").replace(")", "").replace("'", "")

            # Exception for this
            if "-->" in new_word:
                continue
            splitted = new_word.split(",")
            german_word = splitted[0]
            count = splitted[1]

            # Translating word
            translator = Translator()
            czech_word = translator.translate(german_word, src="de", dest="cs").text

            new_line = f"{count}.   {german_word}   {czech_word}"
            f.write(new_line)
            f.write('\n')

print("Learn guide saved on desktop \n Happy learning :)")
