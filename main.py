from random import random
import PySimpleGUI as sg
import numpy as np
import re
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
        print('wrong')
    return is_valid

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
    print('welcome')
    layout=[
        [sg.Text('Enter a long URL to make a TinyURL'),sg.InputText()],
        [sg.Button('Make Tiny Url')],
        [sg.Text('TinyURL')],
        [sg.Button('Cancel')]
    ]
    #title="", layout=[[]] ,size=(700,600), margins=(100, 100),
    sg.theme('BrightColors')
    window=sg.Window('🎻 URLOVE ❤',layout)
    while True:
        d = np.chararray((3, 3))
        d[0][2]='h'
        print(d[0][2])
        if d[0][2]==b'h':
            print('done')
        else:
            j=d[0][2]
            print('false')
        event, values = window.read()
        if event==sg.WIN_CLOSED or event=='Cancel':
            break
        shortening_url(values[0])
        #print(values[0])
    window.close()

