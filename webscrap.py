from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphics+card+for+gaming&cm_sp=KeywordRelated-_-graphics%20card-_-graphics%20card%20for%20gaming-_-INFOCARD'

#opening connection,grabbing the page,Dont Change
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML Parsing
page_soup = soup(page_html, "html.parser")

#Grabs each product. Inspect element for what you want
containers = page_soup.findAll("div",{"class":"item-container"})

#make CSV
filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    
    shipping_container = container.findAll("li",{"class":"price-ship"})
    #strip() removes unintended Spaces
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    #Written File  Replace commas in string with pipe(|)
    #Delimited by new line ("\n")
    f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")

    f.close()