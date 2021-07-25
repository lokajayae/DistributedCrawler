import requests
from bs4 import BeautifulSoup

class URLFrontier :
  def __init__(self, domain, ) :
      self.domain = domain
      self.reviewList = []

  def __getSoup(self, url) :
    r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
  
  def __getReviews(self, soup) :
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
      for item in reviews:
        review = {
          'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
          'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
          'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
          'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
        }
        self.reviewList.append(review)
    except:
      pass

  def crawl(self) :
    for i in range(1,10):
      soup = self.__getSoup(self.domain.format(x=i))
      self.__getReviews(soup)
      if not soup.find('li', {'class': 'a-disabled a-last'}):
          pass
      else:
          break

  def getResult(self) :
    return self.reviewList

