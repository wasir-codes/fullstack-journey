def word_frequency(input_text):
    splitted = input_text.split()
    counts = {}
    for word in splitted:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts

text = input("Enter your text: ")
result =  word_frequency(text)
print(result)
