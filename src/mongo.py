from pymongo import MongoClient

class MongoDatabase :
  def __init__(self) :
      self.client = MongoClient('mongodb+srv://admin:admin@sister.1h74c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

  def getDomainFeederData(self) :
    database = self.client.get_database('DistributedCrawler')
    records = database.get_collection('DomainFeeder')

    return list(records.find({}))
