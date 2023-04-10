import os
import pickle
import base64
import json
import inspect
import copy
import gzip
import re
import types

import pytest


def test_get_segment(func):
    doc = "Natural. Language. Processing"
    if len(list(func(doc))) == 3:
        print("Pass")
    else:
        print("Failed")
    return func


def test_get_tokens(func):
    doc = "Natural Language Processing is the best choice for the learning"
    if len(list(func(doc))) == 10:
        print("Pass")
    else:
        print("Failed")
    return func


def test_addition_neg(func):
    if func(-3, -2) == -5:
        print("Pass")
    else:
        print("Failed")
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
