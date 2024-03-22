"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""




def get_count(sentence: str):
    vowels = 'aeiou'
    return len(list(filter(lambda x: x in vowels, sentence)))


def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


def getCount(s):
    return sum(c in 'aeiou' for c in s)


def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])


def getCount(inputStr):
    return len([x for x in inputStr if x in 'aeoiu'])