# ython function that takes a string and returns a dictionary with the frequency of each word
def word_frequency(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.strip(".,!?").lower()
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


# Example usage:
# text = "Hey, It's me Madhu Sudan Ojha. I am Madhu Sudan Ojha"
text = input("Enter your input: ")
result = word_frequency(text)
print(result)
