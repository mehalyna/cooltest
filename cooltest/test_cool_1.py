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


def test_addition_poz():
    assert addition(3, 2) == 5


def test_addition_poz_neg():
    assert addition.addition(3, -5) == -2


def test_addition_neg():
    assert addition.addition(-3, -2) == -5


def test_addition_zero():
    assert addition.addition(3, 0) == 3
