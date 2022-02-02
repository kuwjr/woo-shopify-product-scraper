from requests_html import HTMLSession
import csv
import time

s = HTMLSession()

# Method to visit /shop page
def get_links(url):
    r = s.get(url)
    allProductLinks = r.html.find('.woocommerce-LoopProduct-link')

    links = []
    for productLink in allProductLinks:
        links.append(productLink.find('a', first=True).attrs['href'])
    
    return links

# Method to visit single product and extract data
def get_productdata(link):
    r = s.get(link)
    title = r.html.find('.product_title', first=True).text
    mint_installment = r.html.find('.product-price-installments > b', first=True).text
    price = r.html.find('.woocommerce-Price-amount.amount bdi', first=True).text  
    short_desc = r.html.find('.woocommerce-product-details__short-description', first=True).text
    
    # search for `product_cat-*`
    cat = r.html.find('.product_cat-*', first=True)
    print("price: ", cat)
    # image_link = r.html.find('.woocommerce-product-gallery__image', first=True).attrs['href']
    # tag = r.html.find('a[rel=tag]', first=True).text
    # sku = r.html.find('span.sku', first=True).full_text


# execution
url = 'https://theparfumerie.lk/shop/'
links = get_links(url)

results = []
for link in links:
    results.append(get_productdata(link))
    time.sleep(1)