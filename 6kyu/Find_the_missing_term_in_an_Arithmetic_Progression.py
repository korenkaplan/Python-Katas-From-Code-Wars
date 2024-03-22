"""
5kyu -> Find the missing term in an Arithmetic Progression:
-----------------------------------------------------------
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of
 a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression.
  There is however one hitch: exactly one term from the original series is missing from the set of numbers which have
   been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers.
The missing term will never be the first or last one.
"""



def find_missing(sequence: list[int]):
    # Check if the series is moving up or down
    if sequence[0] < sequence[1]:
        difference = min(sequence[1] - sequence[0], sequence[2] - sequence[1])
    else:
        difference = max(sequence[1] - sequence[0], sequence[2] - sequence[1])

    # Loop through the sequence to find the missing term
    for i in range(len(sequence) - 1):
        current = sequence[i] + difference
        if current != sequence[i + 1]:
            return current


def find_missing_one_liner(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)


series = [1, 5, 7]
print(find_missing(series))
series = [1, 3, 4, 5]
print(find_missing(series))
series = [5, 3, 2, 1]
print(find_missing(series))
