import re


def is_palindrome(word):
    fordwards = ''.join(re.findall(r'[a-z]+', word.lower()))
    backwards = fordwards[::-1]
    return fordwards == backwards


if __name__ == "__main__":
    print(is_palindrome("biapong"))