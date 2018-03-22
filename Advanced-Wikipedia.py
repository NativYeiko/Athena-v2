import wikipedia

while True:
        input = raw_input("Q: ")
        wikipedia.set_lang("fr")
        print wikipedia.summary(input, sentences=2)
