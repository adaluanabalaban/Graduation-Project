import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.ah.nl/producten/aardappel-groente-fruit/groente?page=18" 


page = requests.get(url) #use requests to get the page via HTTP
html = BeautifulSoup(page.content, "html.parser")

product_html = html.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G" )

product_list = []

for item in product_html:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if product_size == None:
       print(product_name)
      
        
df_veggies = pd.DataFrame.from_dict(product_list)
df_veggies.to_csv("AHveggies.csv", index=False) 



url1 = "https://www.ah.nl/producten/aardappel-groente-fruit/fruit?page=7" 


page1 = requests.get(url1) #use requests to get the page via HTTP
html1 = BeautifulSoup(page1.content, "html.parser")

title_html1 = html1.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list1 = []

for item in title_html1:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
  


df_fruits = pd.DataFrame.from_dict(product_list)
df_fruits.to_csv("AHfruits.csv", index=False)



url2 = "https://www.ah.nl/producten/kaas-vleeswaren-tapas/kaas?page=17" 


page2 = requests.get(url2) #use requests to get the page via HTTP
html2 = BeautifulSoup(page2.content, "html.parser")

title_html2 = html2.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list2 = []

for item in title_html2:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
       
df_cheese = pd.DataFrame.from_dict(product_list2)       
df_cheese.to_csv("AHcheese.csv", index=False)



url3 = "https://www.ah.nl/producten/vlees-kip-vis-vega/kalfsvlees-lamsvlees-wild" 


page3 = requests.get(url3) #use requests to get the page via HTTP
html3 = BeautifulSoup(page3.content, "html.parser")

title_html3 = html3.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list3 = []

for item in title_html3:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
       
df_fancymeat = pd.DataFrame.from_dict(product_list3)
df_fancymeat.to_csv("AHfancymeat.csv", index=False)


url4 = "https://www.ah.nl/producten/vlees-kip-vis-vega/vlees?kenmerk=animal_species%3Avarken&page=5" 


page4 = requests.get(url4) #use requests to get the page via HTTP
html4 = BeautifulSoup(page4.content, "html.parser")

title_html4 = html4.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list4 = []

for item in title_html4:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
       
df_pork = pd.DataFrame.from_dict(product_list4)
df_pork.to_csv("AHpork.csv", index=False)


url5 = "https://www.ah.nl/producten/vlees-kip-vis-vega/vlees?kenmerk=animal_species%3Arund&page=5" 


page5 = requests.get(url5) #use requests to get the page via HTTP
html5 = BeautifulSoup(page5.content, "html.parser")

title_html5 = html5.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list5 = []

for item in title_html5:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
       
df_beef = pd.DataFrame.from_dict(product_list5)
df_beef.to_csv("AHbeef.csv", index=False)



url6 = "https://www.ah.nl/producten/vlees-kip-vis-vega/kip?page=4" 


page6 = requests.get(url6) #use requests to get the page via HTTP
html6 = BeautifulSoup(page6.content, "html.parser")

title_html6 = html6.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list6 = []

for item in title_html6:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
       
df_chicken = pd.DataFrame.from_dict(product_list6)
df_chicken.to_csv("AHchicken.csv", index=False)


url7 = "https://www.ah.nl/producten/vlees-kip-vis-vega/schaal-en-schelpdieren?page=1" 


page7 = requests.get(url7) #use requests to get the page via HTTP
html7 = BeautifulSoup(page7.content, "html.parser")

title_html7 = html7.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list7 = []

for item in title_html7:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
       
df_seafood = pd.DataFrame.from_dict(product_list7)
df_seafood.to_csv("AHseafood.csv", index=False)


url8 = "https://www.ah.nl/producten/vlees-kip-vis-vega/vegetarisch-en-vegan?page=5" 


page8 = requests.get(url8) #use requests to get the page via HTTP
html8 = BeautifulSoup(page8.content, "html.parser")

title_html8 = html8.find_all(class_="price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G")

product_list8 = []

for item in title_html8:
    
   parent = item.parent
   product_name = item.parent.parent.parent.get('title')
   
   sibling = item.next_sibling
   product_size = item.next_sibling.contents[0]
   product_list.append({'name': product_name, 'quantity': product_size})

   if not product_size:
       print(product_name)
       
df_veganmeat = pd.DataFrame.from_dict(product_list8)
df_veganmeat.to_csv("AHveganfood.csv", index=False)



url9 = "https://www.ah.nl/producten/zuivel-plantaardig-en-eieren/melk?page=2" 


page9 = requests.get(url9) #use requests to get the page via HTTP
html9 = BeautifulSoup(page9.content, "html.parser")

title_html9 = html9.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list9 = {}



for item in title_html9:
    
   parent = item.parent
   product_name9 = item.parent.get('title')
   product_dict9 = product_list9.get(product_name9) or {}
   product_list9[product_name9] = product_dict9
    
  
#print(product_list7)    

df9 = pd.DataFrame.from_dict(product_list9, orient = 'columns')
df_milk = df9.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_milk.to_csv("AHmilk.csv", index=False)


url10 = "https://www.ah.nl/producten/zuivel-plantaardig-en-eieren/yoghurt-en-kwark?kenmerk=dieet_vegetarisch&page=4" 


page10 = requests.get(url10) #use requests to get the page via HTTP
html10 = BeautifulSoup(page10.content, "html.parser")

title_html10 = html10.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list10 = {}



for item in title_html10:
    
   parent = item.parent
   product_name10 = item.parent.get('title')
   product_dict10 = product_list10.get(product_name10) or {}
   product_list10[product_name10] = product_dict10
    
  
#print(product_list7)    

df10 = pd.DataFrame.from_dict(product_list10, orient = 'columns')
df_yoghurt = df10.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_yoghurt.to_csv("AHyoghurt.csv", index=False)


url11 = "https://www.ah.nl/producten/zuivel-plantaardig-en-eieren/plantaardige-zuivel-alternatieven/plantaardige-drinks?page=1" 


page11 = requests.get(url11) #use requests to get the page via HTTP
html11 = BeautifulSoup(page11.content, "html.parser")

title_html11 = html11.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list11 = {}



for item in title_html11:
    
   parent = item.parent
   product_name11 = item.parent.get('title')
   product_dict11 = product_list11.get(product_name11) or {}
   product_list11[product_name11] = product_dict11
    
  
#print(product_list7)    

df11 = pd.DataFrame.from_dict(product_list11, orient = 'columns')
df_vegmilk = df11.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_vegmilk.to_csv("AHvegmilk.csv", index=False)


url12 = "https://www.ah.nl/producten/zuivel-plantaardig-en-eieren/plantaardige-zuivel-alternatieven/plantaardige-yoghurt" 


page12 = requests.get(url12) #use requests to get the page via HTTP
html12 = BeautifulSoup(page12.content, "html.parser")

title_html12 = html12.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list12 = {}



for item in title_html12:
    
   parent = item.parent
   product_name12 = item.parent.get('title')
   product_dict12 = product_list12.get(product_name12) or {}
   product_list12[product_name12] = product_dict12
    
  
#print(product_list7)    

df12 = pd.DataFrame.from_dict(product_list12, orient = 'columns')
df_vegyoghurt = df12.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_vegyoghurt.to_csv("AHvegyoghurt.csv", index=False)


url13 = "https://www.ah.nl/producten/zuivel-plantaardig-en-eieren/plantaardige-zuivel-alternatieven/plantaardige-kwark" 


page13 = requests.get(url13) #use requests to get the page via HTTP
html13 = BeautifulSoup(page13.content, "html.parser")

title_html13 = html13.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list13 = {}



for item in title_html13:
    
   parent = item.parent
   product_name13 = item.parent.get('title')
   product_dict13 = product_list13.get(product_name13) or {}
   product_list13[product_name13] = product_dict13
    
  
#print(product_list7)    

df13 = pd.DataFrame.from_dict(product_list13, orient = 'columns')
df_vegkwark = df13.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_vegkwark.to_csv("AHvegwkark.csv", index=False)


url14 = "https://www.ah.nl/producten/pasta-rijst-en-wereldkeuken/pasta-rijst-noedels/pasta?page=5" 


page14 = requests.get(url14) #use requests to get the page via HTTP
html14 = BeautifulSoup(page14.content, "html.parser")

title_html14 = html14.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list14 = {}



for item in title_html14:
    
   parent = item.parent
   product_name14 = item.parent.get('title')
   product_dict14 = product_list14.get(product_name14) or {}
   product_list14[product_name14] = product_dict14
    
  
#print(product_list7)    

df14 = pd.DataFrame.from_dict(product_list14, orient = 'columns')
df_pasta = df14.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_pasta.to_csv("AHpasta.csv", index=False)



url15 = "https://www.ah.nl/producten/pasta-rijst-en-wereldkeuken/pasta-rijst-noedels/rijst?page=3" 


page15 = requests.get(url15) #use requests to get the page via HTTP
html15 = BeautifulSoup(page15.content, "html.parser")

title_html15 = html15.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list15 = {}



for item in title_html15:
    
   parent = item.parent
   product_name15 = item.parent.get('title')
   product_dict15 = product_list15.get(product_name15) or {}
   product_list15[product_name15] = product_dict15
    
  
#print(product_list7)    

df15 = pd.DataFrame.from_dict(product_list15, orient = 'columns')
df_rice = df15.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_rice.to_csv("AHrice.csv", index=False)


url16 = "https://www.ah.nl/producten/pasta-rijst-en-wereldkeuken/couscous-bulgur-quinoa-gort" 


page16 = requests.get(url16) #use requests to get the page via HTTP
html16 = BeautifulSoup(page16.content, "html.parser")

title_html16 = html16.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list16 = {}



for item in title_html16:
    
   parent = item.parent
   product_name16 = item.parent.get('title')
   product_dict16 = product_list16.get(product_name16) or {}
   product_list16[product_name16] = product_dict16
    
  
#print(product_list7)    

df16 = pd.DataFrame.from_dict(product_list16, orient = 'columns')
df_couscous = df16.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_couscous.to_csv("AHcouscous.csv", index=False)


url17 = "https://www.ah.nl/producten/pasta-rijst-en-wereldkeuken/olie-en-frituurvet?page=3" 


page17 = requests.get(url17) #use requests to get the page via HTTP
html17 = BeautifulSoup(page17.content, "html.parser")

title_html17 = html17.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list17 = {}



for item in title_html17:
    
   parent = item.parent
   product_name17 = item.parent.get('title')
   product_dict17 = product_list17.get(product_name17) or {}
   product_list17[product_name17] = product_dict17
    
  
#print(product_list7)    

df17 = pd.DataFrame.from_dict(product_list17, orient = 'columns')
df_oil = df17.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_oil.to_csv("AHoil.csv", index=False)


url18 = "https://www.ah.nl/producten/ontbijtgranen-broodbeleg-tussendoor/vleeswaren-beleg?kenmerk=dieet_vegetarisch&kenmerk=dieet_veganistisch" 


page18 = requests.get(url18) #use requests to get the page via HTTP
html18 = BeautifulSoup(page18.content, "html.parser")

title_html18 = html18.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list18 = {}



for item in title_html18:
    
   parent = item.parent
   product_name18 = item.parent.get('title')
   product_dict18 = product_list18.get(product_name18) or {}
   product_list18[product_name18] = product_dict18
    
  
#print(product_list7)    

df18 = pd.DataFrame.from_dict(product_list18, orient = 'columns')
df_vegham = df18.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_vegham.to_csv("AHvegham.csv", index=False)


url19 = "https://www.ah.nl/producten/ontbijtgranen-broodbeleg-tussendoor/vleeswaren-beleg?page=11" 


page19 = requests.get(url19) #use requests to get the page via HTTP
html19 = BeautifulSoup(page19.content, "html.parser")

title_html19 = html19.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list19 = {}



for item in title_html19:
    
   parent = item.parent
   product_name19 = item.parent.get('title')
   product_dict19 = product_list19.get(product_name19) or {}
   product_list19[product_name19] = product_dict19
    
  
#print(product_list7)    

df19 = pd.DataFrame.from_dict(product_list19, orient = 'columns')
df_ham = df19.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_ham.to_csv("AHham.csv", index=False)


url20 = "https://www.ah.nl/zoeken?query=vis&soort=6539&page=3" 


page20 = requests.get(url20) #use requests to get the page via HTTP
html20 = BeautifulSoup(page20.content, "html.parser")

title_html20 = html20.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list20 = {}



for item in title_html20:
    
   parent = item.parent
   product_name20 = item.parent.get('title')
   product_dict20 = product_list20.get(product_name20) or {}
   product_list20[product_name20] = product_dict20
    
  
#print(product_list7)    

df20 = pd.DataFrame.from_dict(product_list20, orient = 'columns')
df_fish = df20.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_fish.to_csv("AHfish.csv", index=False)


url21 = "https://www.ah.nl/zoeken?query=vis&soort=2726&page=4" 


page21 = requests.get(url21) #use requests to get the page via HTTP
html21 = BeautifulSoup(page21.content, "html.parser")

title_html21 = html21.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list21 = {}



for item in title_html21:
    
   parent = item.parent
   product_name21 = item.parent.get('title')
   product_dict21 = product_list21.get(product_name21) or {}
   product_list21[product_name21] = product_dict21
    
  
#print(product_list7)    

df21 = pd.DataFrame.from_dict(product_list21, orient = 'columns')
df_cannedfish = df21.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_cannedfish.to_csv("AHcannedfish.csv", index=False)


url22 = "https://www.ah.nl/producten/frisdrank-sappen-koffie-thee/koffie/snelfilterkoffie?page=1" 


page22 = requests.get(url22) #use requests to get the page via HTTP
html22 = BeautifulSoup(page22.content, "html.parser")

title_html22 = html22.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list22 = {}



for item in title_html22:
    
   parent = item.parent
   product_name22 = item.parent.get('title')
   product_dict22 = product_list22.get(product_name22) or {}
   product_list22[product_name22] = product_dict22
    
  
#print(product_list7)    

df22 = pd.DataFrame.from_dict(product_list22, orient = 'columns')
df_groundcoffee = df22.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_groundcoffee.to_csv("AHcoffeeground.csv", index=False)


url23 = "https://www.ah.nl/producten/frisdrank-sappen-koffie-thee/koffie/koffiebonen?page=3" 


page23 = requests.get(url23) #use requests to get the page via HTTP
html23 = BeautifulSoup(page23.content, "html.parser")

title_html23 = html23.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list23 = {}



for item in title_html23:
    
   parent = item.parent
   product_name23 = item.parent.get('title')
   product_dict23 = product_list23.get(product_name23) or {}
   product_list23[product_name23] = product_dict23
    
  
#print(product_list7)    

df23 = pd.DataFrame.from_dict(product_list23, orient = 'columns')
df_coffeebeans = df23.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_coffeebeans.to_csv("AHcoffeebeans.csv", index=False)


url24 = "https://www.ah.nl/producten/frisdrank-sappen-koffie-thee/koffie/koffiecups?page=6" 


page24 = requests.get(url24) #use requests to get the page via HTTP
html24 = BeautifulSoup(page24.content, "html.parser")

title_html24 = html24.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list24 = {}



for item in title_html24:
    
   parent = item.parent
   product_name24 = item.parent.get('title')
   product_dict24 = product_list24.get(product_name24) or {}
   product_list24[product_name24] = product_dict24
    
  
#print(product_list7)    

df24 = pd.DataFrame.from_dict(product_list24, orient = 'columns')
df_coffeecups = df24.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_coffeecups.to_csv("AHcoffeecups.csv", index=False)


url25 = "https://www.ah.nl/producten/frisdrank-sappen-koffie-thee/thee?page=7" 


page25 = requests.get(url25) #use requests to get the page via HTTP
html25 = BeautifulSoup(page25.content, "html.parser")

title_html25 = html25.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list25 = {}



for item in title_html25:
    
   parent = item.parent
   product_name25 = item.parent.get('title')
   product_dict25 = product_list25.get(product_name25) or {}
   product_list25[product_name25] = product_dict25
    
  
#print(product_list7)    

df25 = pd.DataFrame.from_dict(product_list25, orient = 'columns')
df_tea = df25.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_tea.to_csv("AHtea.csv", index=False)


url26 = "https://www.ah.nl/producten/frisdrank-sappen-koffie-thee/frisdrank?kenmerk=carbonation_intensity%3Abruisend&kenmerk=sugar_free%3Anee&page=6" 


page26 = requests.get(url26) #use requests to get the page via HTTP
html26 = BeautifulSoup(page26.content, "html.parser")

title_html26 = html26.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list26 = {}



for item in title_html26:
    
   parent = item.parent
   product_name26 = item.parent.get('title')
   product_dict26 = product_list26.get(product_name26) or {}
   product_list26[product_name26] = product_dict26
    
  
#print(product_list7)    

df26 = pd.DataFrame.from_dict(product_list26, orient = 'columns')
df_soda = df26.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_soda.to_csv("AHsoda.csv", index=False)


url27 = "https://www.ah.nl/producten/frisdrank-sappen-koffie-thee/frisdrank?kenmerk=carbonation_intensity%3Abruisend&kenmerk=sugar_free%3Aja&page=5" 


page27 = requests.get(url27) #use requests to get the page via HTTP
html27 = BeautifulSoup(page27.content, "html.parser")

title_html27 = html27.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list27 = {}



for item in title_html27:
    
   parent = item.parent
   product_name27 = item.parent.get('title')
   product_dict27 = product_list27.get(product_name27) or {}
   product_list27[product_name27] = product_dict27
    
  
#print(product_list7)    

df27 = pd.DataFrame.from_dict(product_list27, orient = 'columns')
df_sodanosugar = df27.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_sodanosugar.to_csv("AHsodasugarfree.csv", index=False)


url28 = "https://www.ah.nl/producten/wijn-en-bubbels?minPrice=7&maxPrice=10&page=9" 


page28 = requests.get(url28) #use requests to get the page via HTTP
html28 = BeautifulSoup(page28.content, "html.parser")

title_html28 = html28.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list28 = {}



for item in title_html28:
    
   parent = item.parent
   product_name28 = item.parent.get('title')
   product_dict28 = product_list28.get(product_name28) or {}
   product_list28[product_name28] = product_dict28
    
  
#print(product_list7)    

df28 = pd.DataFrame.from_dict(product_list28, orient = 'columns')
df_wine = df28.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_wine.to_csv("AHwine.csv", index=False)


url29 = "https://www.ah.nl/producten/bier-en-aperitieven/bier?page=15" 


page29 = requests.get(url29) #use requests to get the page via HTTP
html29 = BeautifulSoup(page29.content, "html.parser")

title_html29 = html29.find_all(class_="title_root__2b4w2 product-card-portrait_title__14Jej")

product_list29 = {}



for item in title_html29:
    
   parent = item.parent
   product_name29 = item.parent.get('title')
   product_dict29 = product_list29.get(product_name29) or {}
   product_list29[product_name29] = product_dict29
    
  
#print(product_list7)    

df29 = pd.DataFrame.from_dict(product_list29, orient = 'columns')
df_beer = df29.transpose().reset_index().rename({'index':'Product'}, axis = 'columns')

df_beer.to_csv("AHbeer.csv", index=False)

