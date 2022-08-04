#Find the missing letter
#Write a method that takes an array of consecutive (increasing) letters as input and that returns
#the missing letter in the array.
#You will always get an valid array. And it will be always exactly one letter be missing. The length
#of the array will always be at least 2.
#The array will always contain letters in only one case. (Use the English alphabet with 26 letters!)
#Examples (Input --> Output)
#["a","b","c","d","f"] -> "e"
#["O","Q","R","S"] -> "P"

import codewars_test as test
import string

def find_missing_letter(chars):
    if len(chars) < 2:
        return False
    alphabet = list( string.ascii_uppercase ) if chars[0].isupper() else list( string.ascii_lowercase )
    is_started = False
    for letter in alphabet:
        if letter not in chars:
            if is_started:
                return letter
        else:
            is_started = True

test.describe("find_missing_letter tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
test.assert_equals(find_missing_letter(['D','E','G','H']), 'F')
test.assert_equals(find_missing_letter(['i','k','l','m']), 'j')
test.assert_equals(find_missing_letter(['R','T']), 'S')