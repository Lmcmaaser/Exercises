# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

# for word in sentence:
#     chunk = word.split(' ')
#     print(chunk)


sentence = input('Please enter a sentence that contains no numbers: ')
try:
    count = 0
    letter = []
    words = sentence.split() #returns a list of each word
    wordCount = len(sentence.split()) #returns an integer
    print(words, wordCount)
    for word in words:
        letter = len(word)
        print(letter) #returns length of each word, yay! is an int
        print(type(letter))

        # for i in letter:
        #     print(i) #TypeError: 'int' object is not iterable
    # total = sum(letter)
    # print(total)

except ValueError:
    print('The sentence cannot have numbers in it')
    quit()
