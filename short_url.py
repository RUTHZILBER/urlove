import string
import math
import random
import re

def split_to_parameters(url_address):
    protocol = re.split('://', url_address, 1)
    protocol[0] = protocol[0] + '://'
    # protocol is : ['https://','github.com/racehli?87']
    query = protocol[1].rpartition('?')
    # query is : ('github.com/racheli','?','87')

    # or : ('','','github.com')
    if query[0]=='' and query[1]=='':
        query=(query[2],query[0],query[1])

    #query is: ('github.com', ''/'?',''/'dfdsfdsf') , and protocol is : ['https://','github.com/racehli?87']
    return (query,protocol)#,url_without_parameters

def ganrate_random_short_url(value):
    valid_url_characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&+,-./=@_|~'
    n=math.ceil(math.log10(len(value)))
    print(n)
    return (''.join(random.SystemRandom().choice(valid_url_characters) for _ in range(n)))

if __name__=='__main__':
    sourse_urls=['https://www.w3schools.com/python/python_mongodb_create_db.asp',
                     'https://www.google.co.il/?gws_rd=ssl',
                     'https://docs.mongodb.com/manual/tutorial/update-documents/',
                     'https://www.google.com/search?q=cloud.mongodb%20add%20new%20database'
                     ]