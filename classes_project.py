# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:24:46 2022

@author: laksh
"""

class bookshelf:
  def __init__(self, name, author, price, publishing_year):
    self.book_name = name
    self.book_author = author
    self.book_price = price
    self.book_publishing_year = publishing_year
  def add_book(self):
    print("Book name:", self.book_name)
    print("Book author:", self.book_author)
    print("Book price:", self.book_price)
    print("Book publishing year:", self.book_publishing_year)
  def years_since(self):
    years1 = 2022
    years1 -= int(self.book_publishing_year)
    print("This book is", years1, "years old.")
    print("done")
    
name1 = input("Book name: \n")
author1 = input("Enter author: \n")
price1 = input("Enter price: \n")
publishing_year1 = str(input("Enter publishing year: \n"))
classes = bookshelf(name1, author1, price1, publishing_year1)
classes.add_book()
classes.years_since()