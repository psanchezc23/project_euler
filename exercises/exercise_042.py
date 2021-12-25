import time


A_ASCII_VALUE = ord("A")


def exercise_042():
    """
    The nth term of the sequence of triangle numbers is given by,
    tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text
    file containing nearly two-thousand common English words, how many are
    triangle words?

    :return: number of triangle words
    :rtype: int
    """

    with open("./files/exercise_042.txt", "r") as f:
        words = f.readlines()[0].split(",")

    words_sum = dict.fromkeys(words)
    max_sum = 0
    for word in words:
        name = word.replace('"', "")
        word_sum = sum([ord(c) - A_ASCII_VALUE + 1 for c in name])
        max_sum = max(max_sum, word_sum)
        words_sum[word] = word_sum

    triangle_seq = []
    n = 0
    t_n = 0
    while t_n < max_sum:
        t_n = n * (n + 1) / 2
        triangle_seq.append(t_n)
        n += 1

    triangle_words = [
        word for word, word_sum in words_sum.items()
        if word_sum in triangle_seq
    ]

    return len(triangle_words)


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_042())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
