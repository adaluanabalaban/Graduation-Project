import requests
import pandas as pd
from bs4 import BeautifulSoup

#paste the url go scrape products
url = 'https://www.ah.nl/producten/kaas-vleeswaren-tapas/kaas/plantaardig-alternatief-voor-kaas' 


page = requests.get(url) #use requests to get the page via HTTP
html = BeautifulSoup(page.content, "html.parser")


product_html = html.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G" )

product_list = []

for item in product_html:
    

  parent = item.parent
  product_name = item.parent.parent.parent.get('title')
   
  sibling = item.next_sibling
  product_size = item.next_sibling.contents[0]
  print(product_size)
  
  product_list.append({'name': product_name, 'quantity': product_size})
  

  if not product_size:
      print(product_name)
      

df = pd.DataFrame.from_dict(product_list)
#export to csv the products 
df.to_csv("vegancheese.csv", index=False)

#THIS CODE WAS REPEATED FOR EVERY ITEM CAETGORY 