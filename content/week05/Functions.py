from pathlib import Path
from datetime import datetime, timedelta
import random
import re


# using regex to match the prefix of a filename
def thats_the_way (path):
    return [f.name for f in  Path(path).iterdir() if f.is_file() and re.match(r'^deep.*$',f.name)]


def no_vinnigrete(date_src, date_dst):
    # also excepts non-zero padded days and months. to achieve only zero padded we can use helper bool func with regex
    date_format = "%Y-%m-%d"
    delta = (datetime.strptime(date_dst, date_format) - datetime.strptime(date_src, date_format)).days
    if delta < 0:
        print("Didn't figure how to turn time backwards yet...")
        return
    date_middle = datetime.strptime(date_src,date_format) + timedelta(days = random.randint(0,delta))
    day = date_middle.strftime("%A")
    if day == "Monday":
        print("Ain't gettin' no vinaigrette today :(")
    else:
        print(date_middle.strftime(date_format))


# why use optionals if can just skip writing one of the args and the outcome will be the same?
def get_recipe_price(prices, optionals = [], **kwargs):
    acc = 0
    for key in kwargs:
        if key not in optionals:
            acc += (float(prices[key])/100.0) * kwargs[key]
    return acc


# version without optionals
def get_recipe_price_2(prices, **kwargs):
    acc = 0
    for key in kwargs:
        acc += (float(prices[key])/100.0) * kwargs[key]
    return acc


'''
list comprehension looks tricky but in reality the logic is:
    for lst in lists: (outer loop)
        for item in list: (inner loop)
            item (append the item to the new list)
'''

def join(*lists, sep = None):
    if sep is None:
        return [item for lst in lists for item in lst]
    else:
        return [item for lst in lists for item in (lst + [sep])]


def parsle_tongue():
    chunk_size = 1024
    chars = []
    data = []
    is_sequential = False
    with open('resources\logo.jpg','rb') as file:
        while True:
            chunk = file.read(chunk_size)
            for byte in chunk:
                if byte == ord('!') and is_sequential:
                    if len(chars) >= 5:
                        data.append(''.join(chars))
                    chars.clear()
                    is_sequential = False
                elif ord('a') <= byte <= ord('z'):
                    chars.append(chr(byte))
                    is_sequential = True
                else:
                    is_sequential = False
                    chars.clear()
            if not chunk:
                break
    return data


# could simply use zip but decided to make recursion in a functional programming style using map to strip iterables
def interleave(*iterables):
     if all(not itr for itr in iterables):    # returns if no more items in any of the iterables (in case of uneven iterables)
         return
     for itr in iterables:
        try:
            yield next(iter(itr))
        except StopIteration:
            continue
     yield from interleave(*(map(lambda it: it[1:], iterables)))



