# program to reverse each word  of a string
def reverse_string(stringg):
    # splitting words
    words = stringg.split()

    # iterating and reversing word
    reverse_word = [nword[::-1] for nword in words]

    # using join method to form sentence
    reverse_string = " ".join(reverse_word)
    return reverse_string


input_string = input("Enter a sentence: ")
print(reverse_string(input_string))
