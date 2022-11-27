def sorting(string):
    letter = string.lower()
    letter = letter.replace(" ", "")
    letter = list(letter)
    n = len(string)
    for i in range(n):
        for j in range(0, n - i - 1):
            if letter[j] > letter[j + 1]:
                letter[j], letter[j + 1] = letter[j + 1], letter[j]
    return "".join(letter)


def is_anagram(first_string, second_string):
    first = sorting(first_string)
    second = sorting(second_string)
    return (first, second, first == second)
