import datetime, random, time
import pymongo
from pymongo.objectid import ObjectId

couchjumping_db = pymongo.MongoReplicateSetClient(
    '<replset_1_ip>:<port>, <replset_2_ip>:<port>, <replset_3_ip>:<port>',
    replicaSet='<replset_name>'
) .failoverwrite

while True:
    time.sleep(1)
    data = {
        '_id': ObjectId(),
        'time': datetime.utcnow(),
        'oxygen': random.random()
    }

    ''' Try for five minutes to recover from a failed primary '''
    for i in range(60):
        try:
            couchjumping_db.<collection_name>.insert(data)
            print 'data successfully written'
            break ''' Exit the retry loop '''
        except pymongo.errors.AutoReconnect, e:
            print 'Warning', e
            time.sleep(5)
        except pymongo.errors.DuplicateKeyError:
            ''' It worked the first time '''
            pass

    else:
        raise Exception("Couldn't write data !!!")
