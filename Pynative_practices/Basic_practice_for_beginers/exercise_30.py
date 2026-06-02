text = "apple banana apple cherry banana apple"


def frequency_count(text):
    words = text.split()
    frequency={}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] =1
    print(frequency)

frequency_count(text)