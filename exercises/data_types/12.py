text = "brasil"
if len(text) < 3:
    print(text)
else:
    if text[-3:] == "ing":
        text += "ly"
        print(text)
    else:
        text += "ing"
        print(text)
