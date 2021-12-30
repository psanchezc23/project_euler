import os
import time


FIRST_LOWER_CASE = ord("a")
LAST_LOWER_CASE = ord("z")


def _decode_letter(letter_ascii, code_ascii):
    return letter_ascii ^ code_ascii


def _valid_message(decoded_message):
    if "*" in decoded_message:
        return False
    elif " " not in decoded_message:
        return False
    elif "~" in decoded_message:
        return False
    elif "{" in decoded_message:
        return False
    elif "}" in decoded_message:
        return False
    elif "#" in decoded_message:
        return False
    elif "|" in decoded_message:
        return False
    elif "@" in decoded_message:
        return False
    elif "<" in decoded_message:
        return False
    elif "`" in decoded_message:
        return False
    elif "\"\"" in decoded_message:
        return False
    elif "'\"" in decoded_message:
        return False
    elif " \"" not in decoded_message:
        return False
    elif "An " not in decoded_message:
        return False
    return True


def _decode_message(message, c1, c2, c3, n_letters=None):
    """
    function to check if the
    xor(exclusive or) of two ascii
    numbers entered is only letters
    used in common english
    """
    password = {0: c1, 1: c2, 2: c3}
    decoded_message = ""
    for i, letter in enumerate(message[:n_letters]):
        decoded_message += chr(_decode_letter(letter, password[i % 3]))
    return decoded_message


def _get_sum_ascii_message(decoded_message):
    solution = 0
    for letter in decoded_message:
        solution += ord(letter)
    return solution


def exercise_059():
    """
    Each character on a computer is assigned a unique code and the preferred
    standard is ASCII (American Standard Code for Information Interchange).
    For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to
    ASCII, then XOR each byte with a given value, taken from a secret key. The
    advantage with the XOR function is that using the same encryption key on
    the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
    then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text
    message, and the key is made up of random bytes. The user would keep the
    encrypted message and the encryption key in different locations, and
    without both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified
    method is to use a password as a key. If the password is shorter than the
    message, which is likely, the key is repeated cyclically throughout the
    message. The balance for this method is using a sufficiently long password
    key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three
    lower case characters. Using p059_cipher.txt (right click and
    'Save Link/Target As...'), a file containing the encrypted ASCII codes,
    and the knowledge that the plain text must contain common English words,
    decrypt the message and find the sum of the ASCII values in the original
    text.

    :return: Size of the square
    :rtype: int
    """

    file_path = os.path.join(
        os.path.dirname(__file__), "files/exercise_059.txt"
    )
    with open(file_path, "r") as f:
        letters_ascii = f.readlines()[0].split(',')
        letters_ascii = list(map(int, letters_ascii))

    solution = 0
    for c1 in range(97, 123):
        for c2 in range(97, 123):
            for c3 in range(97, 123):
                message = _decode_message(letters_ascii, c1, c2, c3, 100)
                if _valid_message(message):
                    message = _decode_message(letters_ascii, c1, c2, c3)
                    solution = _get_sum_ascii_message(message)
    return solution


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_059())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
