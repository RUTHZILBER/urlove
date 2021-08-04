from pymongo import MongoClient
import certifi
from random import randint
from pprint import pprint



def insert_to_db(db, table_name, sourse_urls, exchanged_urls):
    for i in range(4):
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
    insert_to_db(db, table_name, sourse_urls, exchanged_urls)


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
    print('sorry, I\'m too tired')