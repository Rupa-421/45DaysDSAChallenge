from collections import Counter
def printDuplicates(given_string):
    count=Counter(given_string)
    for char in count:
        if count[char]>1:
            print(char+" count is "+count[char])
