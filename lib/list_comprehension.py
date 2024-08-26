#!/usr/bin/env python3

num_list = [0,1,2,3,5,7,8,9]
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [word + '!' for word in sentence_list  ]