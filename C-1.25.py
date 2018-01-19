##C-1.25 Write a short Python function that takes a string s, representing a sentence,
##and returns a copy of the string with all punctuation removed. For example,
##if given the string "Let s try, Mike.", this function would return
##"Lets try Mike".


def removePunctuation(sentence):
    result = list(sentence)
    for val in result:
        if val == '.' or val == ',' or val == '"' or val == '\'':
            result.remove(val)

    return ''.join(result)

sentence = "Let's try, Mike."
print(removePunctuation(sentence))

