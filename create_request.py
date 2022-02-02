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

    # get title if available
    title = False
    v = r.html.find('.product_title', first=True)
    if v is not None:
        title = v.text

    # get mintpay installment if found
    mint_installment = False
    v = r.html.find('.product-price-installments > b', first=True)
    if v is not None:
        mint_installment = v.text

    # get product price if found
    price = False
    v = r.html.find('.woocommerce-Price-amount.amount', first=True)
    if v is not None:
        price = v.text
    
    # there are 2 types of classes for short_desc
    sd1 = r.html.find('.woocommerce-product-details__short-description', first=True)
    sd2 = r.html.find('.product-short-description', first=True, clean=True)

    short_desc = False

    if sd1 is not None:
        short_desc = sd1.text

    if sd2 is not None:
        short_desc = sd2.text

    # search for `product_cat-*`
    v = r.html.find('.product.type-product', first=True).attrs['class']
    categories = []
    for cat in v:
        if cat.startswith("product_cat-"):
            categories.append(cat.split("product_cat-", 1)[1])

    # get image link
    image_link = False
    v = r.html.find('.woocommerce-product-gallery__image', first=True).attrs['data-thumb']
    if v is not None:
        image_link = v.split("?", 1)[0] # using split to remove query strings

    # add details to product dict
    product = {
        'name': title,
        'price': price,
        'mint_installment': mint_installment,
        'description': short_desc,
        'categories': categories,
        'image': image_link
    }

    print("PRODUCT: ", product)

# execution
url = 'https://themes.woocommerce.com/storefront/shop/'
links = get_links(url)

results = []
for link in links:
    results.append(get_productdata(link))
    time.sleep(1)