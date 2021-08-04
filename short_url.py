import string
import math
import random
import re
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

def split_protocol_dns_query(url_address):
    protocol=re.split('://',url_address,1)
    protocol[0]=protocol[0]+'://'
    # protocol is : ['https://','github.com/racehli?87']
    query=protocol[1].rpartition('?')
    # query is : ('github.com/racheli','?','87')
    # or : ('','','github.com')
    if query[0]!='' and query[1]!='':
        protocol[1]=query[0]
        protocol.append(query[1]+query[2])
        new_url=ganrate_random_short_url(protocol[1])
        return (protocol[0]+new_url,protocol[2])
        # ( 'https://github.com' , '?dfljlsdf')
    else:
        new_url=ganrate_random_short_url(protocol[1])
        return protocol[0]+new_url

def ganrate_random_short_url(value):
    valid_url_characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&+,-./=@_|~'
    n=math.ceil(math.log10(len(value)))
    print(n)
    return (''.join(random.SystemRandom().choice(valid_url_characters) for _ in range(n)))
sourse_urls=['https://www.w3schools.com/python/python_mongodb_create_db.asp',
                 'https://www.google.co.il/?gws_rd=ssl',
                 'https://docs.mongodb.com/manual/tutorial/update-documents/',
                 'https://www.google.com/search?q=cloud.mongodb%20add%20new%20database'
                 ]
for i in sourse_urls:
    print(split_protocol_dns_query(i))
print(split_protocol_dns_query('https://stackoverflow.com/questions/22f57441/random-string-generation-with-upper-case-letters-and-digits/23728630#23728630dsf'))
#ganrate_random_short_url('https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/23728630#23728630')