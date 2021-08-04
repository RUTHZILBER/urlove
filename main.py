from random import random
import PySimpleGUI as sg
import numpy as np
import re
import gui
import string


def insert_new_url_to_db():
    print('inserted new url to data base succesfully')
def ganrate_short_url():
    print('ganrate url short characters')
def url_generator(size=6, chars=string.ascii_lowercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))
def shortening_url(value=""):
    try:
        #arr=np
        source_url=str(value)
        if len(source_url)==0:
            print('not value')
        else:
            #is_valid_url(source_url)
            #short_url=ganrate_short_url()
            #insert_new_url_to_db(source_url,short_url)
            #return short_url
            return 'https://fdsfldfslfjl'
    except ValueError as error:
        print('error')


#if __name__=="__main__":
if 1==1:
    gui.screem_printed()


