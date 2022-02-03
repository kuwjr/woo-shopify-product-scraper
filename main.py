import time
import csv
from utils import checkCms
from woocommerce import get_links, get_productdata

# load url 
url = 'https://theparfumerie.lk/shop'

# set headers to recreate browser view
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# detect cms
cms = checkCms(url, headers)

if cms == False:
    print("There was an error! Meow!")
else:
    # based on cms, run extraction
    if cms['name'] == 'woocommerce':
        # send web page
        links = get_links(url)

        results = []
        for link in links:
            results.append(get_productdata(link))
            print("\n")
            time.sleep(1)