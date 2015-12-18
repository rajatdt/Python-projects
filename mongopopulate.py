import pymongo
from pymongo import mongoclient

''' connect with the database '''

def connect():
    client = mongoclient('10.10.10.100', 23000)
    f = open('testdb').readlines()
    print 'total collections in the database', len(f)
    for x in f:
	    if x[0] == 'user_id':
		    y+=1
		    print x
print 'All data related to user_id', y

''' Read the database from file '''

def populate():
	connect()

	db = client['mydb']
	coll = db['mycollection']

	lst1 = []

	file = open('mydb').readlines()
	for items in file:
		for deeperitems in item:
			if deeperitems[0] == "_id":
				for i in range len(items):
					lst1[i] = deeperitems[i]

print 'total data per collection', len(lst1)
print 'total generated ids', lst1

''' insert data into the collection in bulk '''

def bulkInsert():
	import mydb
	int i

	post = [{"user_id" : "hashed",
			 "user_name": "user"+i}]
	posts = db.posts
	post_id = posts.insert_one(post)

	result = posts.insert_many(new_posts)
	result.inserted_ids

	srt1 = result.insert_ids.sort()

''' populate according to the fields in the documents '''

from pymongo import ASCENDING, DESCENDING
def randomPopulate():
	posts.create.index([("Date", DESCENDING), ("user_id", ASCENDING)])

	for p in posts.find():
		print(p)

''' Authenticate upon connection with the database '''


def computeClientKey(username, plain_text_password) {
    mongo_hashed_password = Hex(MD5(UTF8(username + ':mongo' + plain_text_password)));
    saltedPassword = Hi(Normalize(mongo_hashed_password), salt, i);
    clientKey = HMAC(saltedPassword, "Client Key");

}

'''def dataCollect():
    if mongo_hashed_password == $HexNumber(UTF8(username + ':mongo' + plain_text_password)):
      print 'user password is correct....please proceed to the database'
      <database_name>.<collection_name>.post = {(<user_id_post>: <user_value>)}
