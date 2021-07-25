from mpi4py import MPI
import numpy as np
from pandas.core.frame import DataFrame
import frontier
import mongo
import pandas as pd

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

mongoDb = mongo.MongoDatabase()
domainFeeder = mongoDb.getDomainFeederData()

if rank > 1 and rank < 6:
  print("Crawler ", str(rank), " starting...")
  crawler = frontier.URLFrontier(domainFeeder[rank-1]['domain'])
  crawler.crawl()
  result = crawler.getResult()

  # send data to tokenizer
  comm.send(result, dest=6, tag=11)

  #save data to mongo
  mongoDb.insertBulkData('CrawlResult', result)

  print("Crawler ", str(rank), " is all done...")

elif rank == 6:
  print("Starting Tokenizer...")
  status = [None, False, False, False, False, False]
  idx = 1
  data = []

  while idx < 6 :
    if status[idx] :
      # If status is True which mean the data for crawler idx has been fetched
      idx += 1
    else :
      # If status is False which mean the data for crawler idx has not been fetched
      response = comm.recv(source=idx, tag=11)

      if len(response) == 0 :
        # response is empty, go back to idx 1
        idx = 1
      else :
        # response is not empty, add response to data and change status
        print(len(response))
        data.extend(response)
        status[idx] = True
    
  # df variable is a data contain all crawl result
  df = DataFrame(data)
