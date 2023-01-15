# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:31:20 2023

@author: laksh
"""

from googletrans import Translator

trans = Translator()
translated = trans.translate("नमस्ते")

print(translated)
print(translated.text)
print(trans.LANGUAGES)