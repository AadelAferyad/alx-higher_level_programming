#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    n_tuple = ()
    if (length == 0):
        n_tuple += (0,)
        n_tuple += ('N',)
    else:
        n_tuple += (length,)
        n_tuple += (sentence[0],)
    return (n_tuple)
