import os
import pickle
import base64
import json
import inspect
import copy
import gzip
import re
import types
import spacy

def test_get_segment(func):
    doc = "Natural. Language. Processing"
    if len(list(func(doc))) == 3:
        print(f"Segmentaition Passed\n")
    else:
        print(f"Segmentaition Failed\n")
    return func


def test_get_tokens(func):
    doc = "Natural Language Processing is the best choice for the learning"
    if len(list(func(doc))) == 10:
        print(f"Tokenization Passed\n")
    else:
        print(f"Tokenization Failed\n")
    return func


def test_remove_stop_words(func):
    nlp = spacy.load("en_core_web_sm")
    sent = "Natural Language Processing is the best choice for the learning"
    from spacy.tokenizer import Tokenizer
    tokenizer = Tokenizer(nlp.vocab)
    tokens = tokenizer(sent)
    if len(list(func(tokens))) == 6:
        print(f"Stop Wordes Removing Passed/n")
    else:
        print(f"Stop Wordes Removing Failed/n")
    return func




def test_addition_zero(func):
    if func(3, 0) == 3:
        print("Pass")
    else:
        print("Failed")
    return func


@test_addition_zero
def addition(param1, param2):
    # Type your code
    return param1 + param2
