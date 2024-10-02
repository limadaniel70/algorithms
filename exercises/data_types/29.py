text = "This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same type, n, i, j and k are integers and x is an arbitrary object that meets any type and value restrictions imposed by s."
def count_occ(sentence):
    sentence = sentence.lower()
    words = sentence.split(" ")
    return {word : words.count(word) for word in words}
print(count_occ(text))
