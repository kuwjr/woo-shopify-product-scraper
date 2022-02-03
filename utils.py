from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

def checkCms(url, headers):
    # visit webpage
    page = requests.get(url, headers=headers)
    
    # check if response is successful
    if page.ok == False:
        return False

    soup = BeautifulSoup(page.content, "html.parser")

    # collect all classes
    classes = []
    for element in soup.find_all(class_=True):
        classes.extend(element["class"])

    # check if any of the classes match with CMS names
    for className in classes:
        if className.startswith("woocommerce"):
            return {
                'name': 'woocommerce', 
                'soup': soup
            }
        
        if className.startswith("shopify"):
            return {
                'name': 'shopify',
                'soup': soup
            }

    # if not woocommerce, not shopify
    return False