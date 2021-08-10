from pymongo import MongoClient
import certifi
from random import randint
from pprint import pprint
from short_url import *

def search_url(db,address='https://google.com'):
    found_url=db.translate.find_one({'source_url':address},{'exchanged_url':1,'_id':0})
    #check the value, False if not there...
    if found_url==False:
        return None
    else:
        return found_url

def get_address(db,address='https://google.com?dfd'):
    tuple=split_to_parameters(address)
    query = tuple[0]
    protocol = tuple[1]
    # query is: ('github.com', ''/'?',''/'dfdsfdsf') , and protocol is : ['https://','github.com/racehli?87']
    new_url = protocol[0]
    new_url_with_parametrs = ''
    past_url = protocol[0] + str(query[0])

    short_url=search_url(db,past_url)

    if short_url==None:
        random_part=query[0]
        random_part=ganrate_random_short_url(random_part)

        if query[1]=='?':
            new_url=protocol[0]+random_part
            new_url_with_parametrs=new_url+'?'+str(query[2])
        else:
            new_url=new_url_with_parametrs=protocol[0]+random_part
        insert_to_db(db,past_url,new_url)
    else:
        short_url=short_url['exchanged_url']
        if query[1]!='?':
            new_url_with_parametrs=short_url
        else:
           new_url_with_parametrs=short_url+'?'+str(query[2])
    return new_url_with_parametrs

def insert_to_db(db, sourse_url, exchanged_url, table_name='translate'):
    if 1==1:
        address = {
            'source_url': sourse_url,
            'exchanged_url': exchanged_url
        }
        command = str('db.' + table_name + '.insert_one(address)')
        exec(command)

#################################### 'mongodb+srv://r0548593223:0548593223@dbcluster.d4y5f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
def connect_to_db(window,mongodb_str_access='mongodb+srv://r0548593223:0548593223@dbcluster.d4y5f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'):
    link=mongodb_str_access
    ca = certifi.where()
    client = MongoClient(link, tlsCAFile=ca)
    db=client.admin
    my_db_status=db.command("serverStatus")
    #pprint(my_db_status)
    db = client.business
    #print('right')
    return db

if __name__=='__main__':
    db=connect_to_db()
    a=get_address('https://git.com?43')
    #print(a)
    #the db will storage these data:
    #       the data base name: urlovedb, table name: translate => _id, sourse_url, exchanged_url,

    #sourse_urls=['https://sdff',
    #              'https://www.google.co.il/?gws_rd=ssl',
    #              'https://docs.mongodb.com/manual/tutorial/update-documents/',
    #              'https://www.google.com/search?q=cloud.mongodb%20add%20new%20database'
    #              ]
    # exchanged_urls=[
    #     'https://4i',
    #     'https://=e?gws_rd=ssl',
    #     'https://ra',
    #     'https://Q/?q=cloud.mongodb%20add%20new%20database'
    # ]
    # table_name='translate'
    # #x=search_url(db,'https://www.google.com/search?q=cloud.mongodb%20add%20new%20database')
    # print(search_url(db,'https://www.w3schools.com/python/python_mongodb_create_db.asp'))
# fivestar = db.reviews.find_one({'rating': 5})
#ASingleReview = db.reviews.find_one({})
# result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 3}})
# result = db.restaurants.delete_many({"category": "Bar Food"})
else:
    print('sorry, you didn\'t call me from main')