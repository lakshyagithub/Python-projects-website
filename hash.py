# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:46:22 2023

@author: laksh
"""

import hashlib
from simplecrypt import encrypt, decrypt

value_input = input("Please enter some text to convert to SHA256 \n")
value = value_input

def SHA256():
    result = hashlib.sha256(value.encode())
    print("SHA256: ", result)
    
SHA256()