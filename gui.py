from random import random
import PySimpleGUI as sg
import numpy as np
import re
import string
import pyperclip
import traceback
import short_url
import test_urlove
import validate_utilities
import db_connect




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
def screem_printed():
    print('welcome')
    #,state='disabled'
    layout=[
        [sg.Text('Enter a long URL to make a TinyURL'),sg.InputText()],
        [sg.Button('Make Tiny Url',key='make_tiny'),sg.Button(key='short_url')],
        [sg.Button('COPY URL 🥝',key='copy_url')],
        [sg.Button('Cancel')]
    ]
    #title="", layout=[[]] ,size=(700,600), margins=(100, 100),
    sg.theme('BrightColors')
    window=sg.Window('🎻 URLOVE ❤',layout)
    short_url_text=window['short_url']
    while True:
        try:
            event, values = window.read()
            if event==sg.WIN_CLOSED or event=='Cancel':
                break
            shortening_url(values[0])
            short_url_present=window['short_url'].get_text()
            if event=='copy_url' and short_url_present!='': # control c
                print()
                pyperclip.copy(short_url_present)
                spam = pyperclip.paste()
            if event=='make_tiny': # make tinny url
                print('get the new value from function or db')
                new_url='https://github.com/ruthzilber/main?yu&fd+d'
                window.Element('short_url').Update(new_url)
            if event=='short_url' and short_url_present!='':
                print('enter to url link by database')
            #print(values[0])
        except Exception as e:
            #sg.Popup('Not a number')
            tb = traceback.format_exc()
            sg.Print(f'An error happened.  Here is the info:', e, tb)#
            sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)#
    window.close()
screem_printed()

