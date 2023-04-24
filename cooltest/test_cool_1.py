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
        print(f"Stop Words Removing Passed\n")
    else:
        print(f"Stop Words Removing Failed\n")
    return func


def test_stemm_lemmatization(func):
    nlp = spacy.load('en_core_web_sm')
    sent = "Natural Language Processing is the best choice for the learning"
    doc = nlp(sent)
    list_tokens_lemma_act = []
    list_tokens_lemma_exp = []
    for token in doc:
        list_tokens_lemma_exp.append(token.lemma_)
    sut = func(sent)
    for token in sut:
        list_tokens_lemma_act.append(token)
    if list_tokens_lemma_exp == list_tokens_lemma_act:
        print(f"Stemming and Lemmatization Passed\n")
    else:
        print(f"Stemming and Lemmatization Failed\n")
    return func


def test_part_of(func):
    nlp = spacy.load('en_core_web_sm')
    sent = "Natural Language Processing is the best choice for the learning"
    doc = nlp(sent)
    word_tags_exp = {}
    for word in doc:
        word_tags_exp[word.text] =  word.pos_
    word_tags_act = func(sent)
    if word_tags_act == word_tags_exp:
        print(f"Parts of Speech Passed\n")
    else:
        print(f"Parts of Speech Failed\n")
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
