import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyshorteners
import pyperclip

# Creating the soup using html.parser

mec_url = "https://www.mec.ca/en/products/climbing/climbing-footwear/climbing-shoes?promotions=clearance"
mec_page = requests.get(mec_url)
mec_soup = BeautifulSoup(mec_page.content, "html.parser")
df = pd.DataFrame(columns=["Shoe","Sale Price","Original Price","Discount","URL","Shipping Cost","Store"])
#Parse specific MEC.ca related content tags
results = mec_soup.find(id="main-content")
mec_sale_elements = results.find_all("li", class_="Hits_searchHitsItem__XaIFr")
#Loop through each sale element for relevant information
for sale_element in mec_sale_elements:
    shoe_name_element = sale_element.find("a", class_="Hit_hitTitle__dl_OY")
    price_element = sale_element.find("span", class_="Hit_hitPrices__IHAvd").find("span")
    og_price_element = sale_element.find("span", class_="Hit_hitPrices__IHAvd").find("span", class_="Hit_hitOldPrice__7i8ik")
    link_element = "mec.ca" + sale_element.find("a")["href"]
    new_row = {"Shoe" : shoe_name_element,
               "Sale Price" : float(price_element.text.strip()[1:]),
               "Original Price" : float(og_price_element.text.strip()[1:]),
               "Discount" : str(round((float(og_price_element.text.strip()[1:])-float(price_element.text.strip()[1:]))/float(og_price_element.text.strip()[1:]),2)*100)+"%",
               "URL" : link_element,
               "Shipping Cost" : 0,
               "Store" : "MEC"
              }
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df],ignore_index=True)

# # Creating the soup using html.parser
# mec_url = "https://www.monodsports.com/collections/rock-shoes?sort_by=best-selling&filter.p.m.custom.on_sale=Yes"
# mec_page = requests.get(mec_url)
# mec_soup = BeautifulSoup(mec_page.content, "html.parser")
# #Parse specific MEC.ca related content tags
# results = mec_soup.find("div", class_="collection__products collection-items--4 collection-items--mobile--one-half")
# mec_sale_elements = results.find("div", class_="grid")









type_tiny = pyshorteners.Shortener() 
df["URL"] = df["URL"].apply(lambda x: type_tiny.tinyurl.short(x))
df["Post-Tax Price"] = (df["Sale Price"]+df["Shipping Cost"])*1.13

df.sort_values(by="Discount",ascending=False)