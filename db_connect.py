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

def get_address(address='https://google.com?dfd'):
    db=connect_to_db()
    short_url=search_url(db,address)
    tuple=split_to_parameters(address)
    query=tuple[0]
    protocol=tuple[1]
    # query is: ('github.com', ''/'?',''/'dfdsfdsf') , and protocol is : ['https://','github.com/racehli?87']
    new_url=protocol[0]
    new_url_with_parametrs=''
    past_url=protocol[0]+str(query[0])

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
        if query[1]=='?':
            new_url_with_parametrs=short_url
        else:
           new_url_with_parametrs=short_url+'?'+str(query[2])
    return new_url_with_parametrs

def insert_to_db(db, sourse_urls, exchanged_urls, table_name='translate'):
    for i in range(len(sourse_urls)):
        address = {
            'source_url': sourse_urls[i],
            'exchanged_url': exchanged_urls[i]
        }
        command = str('db.' + table_name + '.insert_one(address)')
        exec(command)
        result = db.translate.find({'sourse_url': 'https://sdff'})
        print(result)

        # result=db.translate.insert_one(address)
        # print(result.inserted_id)

#################################### 'mongodb+srv://r0548593223:0548593223@dbcluster.d4y5f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
def connect_to_db(mongodb_str_access='mongodb+srv://r0548593223:0548593223@dbcluster.d4y5f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'):
    link=mongodb_str_access
# link = 'mongodb+srv://r0548593223:0548593223@dbcluster.d4y5f.mongodb.net/DBCLUSTER?retryWrites=true&w=majority'
# link_sorurce='mongodb+srv://RuthZilber:0548593223@cluster0.2izn1.mongodb.net/Cluster0?retryWrites=true&w=majority'
    ca = certifi.where()
    client = MongoClient(link, tlsCAFile=ca)
    db=client.admin
    my_db_status=db.command("serverStatus")
    #pprint(my_db_status)
    db = client.business
    print('right')
    return db

if __name__=='__main__':
    db=connect_to_db()
    #the db will storage these data:
    #       the data base name: urlovedb, table name: translate => _id, sourse_url, exchanged_url,

    sourse_urls=['https://sdff',
                 'https://www.google.co.il/?gws_rd=ssl',
                 'https://docs.mongodb.com/manual/tutorial/update-documents/',
                 'https://www.google.com/search?q=cloud.mongodb%20add%20new%20database'
                 ]
    exchanged_urls=[
        'https://4i',
        'https://=e?gws_rd=ssl',
        'https://ra',
        'https://Q/?q=cloud.mongodb%20add%20new%20database'
    ]
    table_name='translate'
    #x=search_url(db,'https://www.google.com/search?q=cloud.mongodb%20add%20new%20database')
    print(search_url(db,'https://www.w3schools.com/python/python_mongodb_create_db.asp'))
#fivestarcount = db.reviews.find({'rating': 5}).count()
#print(fivestarcount)
# # Step 2: Create sample data
# names = ['Kitchen', 'Animal', 'State', 'Tastey', 'Big', 'City', 'Fish', 'Pizza', 'Goat', 'Salty', 'Sandwich', 'Lazy',
#          'Fun']
# company_type = ['LLC', 'Inc', 'Company', 'Corporation']
# company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
# for x in range(1, 501):
#     business = {
#         'name': names[randint(0, (len(names) - 1))] + ' ' + names[randint(0, (len(names) - 1))] + ' ' + company_type[
#             randint(0, (len(company_type) - 1))],
#         'rating': randint(1, 5),
#         'cuisine': company_cuisine[randint(0, (len(company_cuisine) - 1))]
#     }
#     # Step 3: Insert business object directly into MongoDB via insert_one
#     result = db.reviews.insert_one(business)
#     # Step 4: Print to the console the ObjectID of the new document
#     print('Created {0} of 500 as {1}'.format(x, result.inserted_id))
# # Step 5: Tell us that you are done
# print('finished creating 500 business reviews')
# # GET DATA FROM DB
# fivestar = db.reviews.find_one({'rating': 5})
# print(fivestar)
# #
# # The result will contain data similar to the following:
# #
# # {u'rating': 5,
# #  u'_id': ObjectId('58e65383ea0b650c867ef195'),
# #  u'name': u'Fish Salty Corporation',
# # u'cuisine': u'Sushi Bar'}
# fivestarcount = db.reviews.find({'rating': 5}).count()
# print(fivestarcount)
# # UPDATE
#ASingleReview = db.reviews.find_one({})
# print('A sample document:')
# pprint(ASingleReview)
# result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 3}})
# print('Number of documents modified : ' + str(result.modified_count))
# UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
# print('The updated document:')
# pprint(UpdatedDocument)
# result = db.restaurants.delete_many({"category": "Bar Food"})
# pprint(result)
#
#
#
#
#
#
#
#
else:
    print('sorry, you didn\'t call me from main')