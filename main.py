from random import random
import PySimpleGUI as sg

def insert_new_url_to_db():
    print('inserted new url to data base succesfully')
def ganrate_short_url():
    print('ganrate url short characters')

def shortening_url(value=""):
    try:
        source_url=str(value)
        if len(source_url)==0:
            print('not value')
        else:
            short_url=ganrate_short_url()
            insert_new_url_to_db(source_url,short_url)
            return short_url
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
        event, values = window.read()
        if event==sg.WIN_CLOSED or event=='Cancel':
            break
        shortening_url(value[0])
        #print(values[0])
    window.close()

