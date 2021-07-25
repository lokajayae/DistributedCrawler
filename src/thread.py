import frontier
import pandas as pd
import logging

def crawlerThread(id, domain) :
  print(f'Thread {id} is starting...')
  crawler = frontier.URLFrontier(domain)
  crawler.crawl()

  df = pd.DataFrame(crawler.getResult())
  # TODO Send data df to MPI
  print(f'Thread {id} is all done...')