from random import random
import PySimpleGUI as sg
import numpy as np
import re
import string
import pyperclip
import traceback
import webbrowser
from short_url import *
from db_connect import *
from validate_utilities import is_valid_url
from db_connect import *

class Main:
    def __init__(self):
        pass
    def run(self):
        screem_printed()

# this project shortens url address, and it is available :
# shorten
# remember last short urls
# copy it
# go to browser with the new url...
# enjoy use this website!!! 💌

def main():
    maini=Main()
    maini.run()

def check_actions(window,db,sg,layout):
    try:
        error_unvalid_url_text='❌❌❌❌ 🈹 press validate url! ❌❌❌ 🎈🧨🧨🧨🧨'
        event, values = window.read()
        if event==sg.WIN_CLOSED or event=='Cancel':
            return -1
        #shortening_url(values[0])
        short_url_present=window['short_url'].get_text()
        long_url=values['long_url']
        if event=='copy_url' and short_url_present!='' and short_url_present!=error_unvalid_url_text: # control c
            print()
            pyperclip.copy(short_url_present)
            spam = pyperclip.paste()

        if event=='make_tiny': # make tinny url
            new_url=''
            if is_valid_url(long_url)==False:
                print('mistake in pressing url')
                new_url=error_unvalid_url_text
            else:
                new_url=get_address(db,long_url)
            window.Element('short_url').Update(new_url)

        if event=='short_url' and short_url_present!='' and short_url_present!=error_unvalid_url_text: #ganrate url
            if is_valid_url(short_url_present)==False:
                print('mistake in pressing url')
            else:
                url=get_address(short_url_present)
                webbrowser.open(url)

        #print(values[0])

        return 1
    except Exception as e:
        #sg.Popup('Not a number')
        tb = traceback.format_exc()
        sg.Print(f'An error happened.  Here is the info:', e, tb)#
        sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)
        return -1

def screem_printed():
    print('welcome')
    #,state='disabled'
    layout=[
        [sg.Text('Enter a long URL to make a TinyURL'),sg.InputText(key='long_url')],
        [sg.Button('Make Tiny Url',key='make_tiny'),sg.Button(key='short_url')],
        [sg.Button(' 🥝 COPY URL 🥝 ',key='copy_url')],
        [sg.Button('Cancel')]
    ]
    #title="", layout=[[]] ,size=(700,600), margins=(100, 100),
    sg.theme('BrightColors')
    window=sg.Window('🎻 URLOVE ❤',layout)
    short_url_text=window['short_url']
    db=connect_to_db(window)
    while True:
        status = check_actions(window, db, sg, layout)
        if status == -1:
            break

    # while True:
    #     try:
    #         error_unvalid_url_text='❌❌❌❌ 🈹 press validate url! ❌❌❌ 🎈🧨🧨🧨🧨'
    #         event, values = window.read()
    #         if event==sg.WIN_CLOSED or event=='Cancel':
    #             break
    #             #return -1
    #         #shortening_url(values[0])
    #         short_url_present=window['short_url'].get_text()
    #         long_url=values['long_url']
    #         if event=='copy_url' and short_url_present!='' and short_url_present!=error_unvalid_url_text: # control c
    #             print()
    #             pyperclip.copy(short_url_present)
    #             spam = pyperclip.paste()
    #
    #         if event=='make_tiny': # make tinny url
    #             new_url=''
    #             if is_valid_url(long_url)==False:
    #                 print('mistake in pressing url')
    #                 new_url=error_unvalid_url_text
    #             else:
    #                 new_url=get_address(db,long_url)
    #             window.Element('short_url').Update(new_url)
    #
    #         if event=='short_url' and short_url_present!='' and short_url_present!=error_unvalid_url_text: #ganrate url
    #             if is_valid_url(short_url_present)==False:
    #                 print('mistake in pressing url')
    #             else:
    #                 url=get_address(short_url_present)
    #                 webbrowser.open(url)
    #
    #         #print(values[0])
    #
    #         #return 1
    #     except Exception as e:
    #         #sg.Popup('Not a number')
    #         tb = traceback.format_exc()
    #         sg.Print(f'An error happened.  Here is the info:', e, tb)#
    #         sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)
    #         #return -1

    window.close()

if __name__=='__main__':
    pass
    #main()


