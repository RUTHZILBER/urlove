from random import random
import PySimpleGUI as sg
import numpy as np
import re
import string

def is_valid_url(url_address):
    url_parts=url_address.split('://')
    if len(url_parts)!=2:
        return False
    if re.match("[0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&+,.-/=@_|~0]", url_parts[1]):
        return True
    return False


if __name__=='__main__':
    urli='https://github.com'
    print(is_valid_url(urli))



