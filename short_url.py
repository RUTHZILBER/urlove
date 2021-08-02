import string
import math
import random
import re

def split_protocol_dns_query(url_address):
    protocol=re.split('://',url_address,1)
    protocol[0]=protocol[0]+'://'
    query=protocol[1].rpartition('?')
    protocol[1]=query[0]
    protocol.append(query[1]+query[2])
    return protocol[0]+ganrate_random_short_url(protocol[1])+protocol[2]
    #print(protocol)
def ganrate_random_short_url(value):
    n=math.ceil(math.log10(len(value)))
    return (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n)))
print(split_protocol_dns_query('https://ru?th?fdfl'))
#ganrate_random_short_url('https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/23728630#23728630')