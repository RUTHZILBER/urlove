from random import random
import PySimpleGUI as sg
import numpy as np
import re
#from gui import *
import string

def is_valid_url(url_address):

    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    try:
        is_valid=re.match(regex,url_address) is not None
    except:
        return False
    return is_valid
if __name__=='__main__':
    urli='hdttps://github.com/ruthzilber'
    print(is_valid_url(urli))
    print('--------------------------------------------')



