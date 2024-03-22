"""
Write a function that accepts a string, and returns the same string with all even indexed characters in each word
upper-cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based,
so the zero-ith index is even, therefore that character should be upper-cased, and you need to start over for each word.
The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there
are multiple words. Words will be separated by a single space(' ').

"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
"""


def to_weird_case(words: str):
    converted_list = []
    separated_words = words.split(' ')
    for word in separated_words:
        converted_word = ''
        for index, value in enumerate(word):
            if index % 2 == 0:
                converted_word += value.upper()
            else:
                converted_word += value.lower()
        converted_list.append(converted_word)
    return ' '.join(converted_list)


def to_weird_case_one_liner(words: str):
    return ' '.join(
        ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)) for word in words.split())





