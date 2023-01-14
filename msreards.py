# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:47:15 2023

@author: laksh
"""

import webbrowser
import random

count = 0
while (count < 10):
    count = count+1
    main_url = "https://bing.com/?q="
    word_meaning = " meaning"
    a_to_j = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "Laptop", "PC", "Windows", "Internet"]
    random_letters = random.randint(0, 9)
    random_letter_1 = a_to_j[random_letters]
    random_letter_2 = a_to_j[random_letters]
    random_letter_3 = a_to_j[random_letters]
    random_letter_4 = a_to_j[random_letters]
    all_letters = random_letter_1 + random_letter_2 + random_letter_3 + random_letter_4
    print(all_letters)
    add_url = main_url + str(all_letters) + word_meaning
    webbrowser.open_new_tab(add_url)