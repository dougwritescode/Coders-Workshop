#!/usr/bin/env python3

def check_permutation(str1, str2):
    str1Letters = sorted(str1)
    str2Letters = sorted(str2)
    sameLetters = str1Letters == str2Letters
    return sameLetters


print(check_permutation("god", "dog"))  # True
print(check_permutation("god ", "dog"))  # False
print(check_permutation("God", "Dog"))  # False
print(check_permutation("hello", "goodbye"))  # False
