# Algorithm for a palindrome

strings = "racecar"


def is_palindrome(strings: str):
    start_index = 0
    end_index = len(strings) - 1

    for x in strings:
        if strings[start_index] != strings[end_index]:
            return False
    return True


print(is_palindrome(strings))
