import frontier
import pandas as pd

crawler = frontier.URLFrontier("https://www.amazon.co.uk/product-reviews/B07WD58H6R/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}")
crawler.crawl()

df = pd.DataFrame(crawler.getResult())
df.to_excel('sony-headphones.xlsx', index=False)
print('Fin.')