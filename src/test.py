import mongo
import thread
import threading

threadId = []
idx = 1

mongoDb = mongo.MongoDatabase()

domainFeeder = mongoDb.getDomainFeederData()

for data in domainFeeder :
  threadId.append(threading.Thread(target=thread.crawlerThread, args=(idx, data['domain'])))
  threadId[idx-1].start()
  idx += 1
  