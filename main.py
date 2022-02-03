import time
import csv
from utils import checkCms
from woocommerce import get_links, get_productdata

urls = ['lk.spaceylon.com', 'zigzag.lk', 'zigmajones.com', 'theparfumerie.lk', 'kikibeauty.lk']

for u in urls:
    # load url 
    url = "https://{0}/shop".format(u)

    # set headers to recreate browser view
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    # detect cms
    cms = checkCms(url, headers)

    print("\n\nMeow:{0}\n\n".format(url))

    if cms == False:
        print("\n\nError:{0}\n\n".format(url))
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