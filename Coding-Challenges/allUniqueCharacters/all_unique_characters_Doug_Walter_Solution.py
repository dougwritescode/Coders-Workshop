#!/usr/bin/env python3

def all_unique(string):
    return len(set(string)) == len(string)


assert all_unique('whistle') == True
assert all_unique('painting') == False
