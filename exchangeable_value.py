sentence = "It got dark as the sun set."
index = 6
new_sentence = sentence.replace(".", "")
split_sentence = new_sentence.split(" ")
print(split_sentence)
new_word = split_sentence[index] + "en"
print(new_word)
