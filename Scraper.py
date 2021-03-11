import urllib.request
from urllib.request import Request, urlopen


import csv
def scrapeLinks(category):
    fetching = True
    baseUrl = "https://egypt.souq.com/eg-en/"+category+"//l/?sortby=sr&section=2&page="
    page=1
    while fetching:
        fp = urllib.request.urlopen(baseUrl+str(page))
        mybytesHomepage = fp.read()

        souqHomePage = mybytesHomepage.decode("utf8")
        fp.close()
        shopAllArray = souqHomePage.split('" class="view-product-details sPrimaryLink secondary button expand white tiny">View full product details</a>')
        links = []
        for i in range(0,len(shopAllArray)-1):
            if shopAllArray[i].split('<a href="')[-1].startswith('https://'):
                links.append(shopAllArray[i].split('<a href="')[-1])
        with open(category+'_links.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(0,len(links)):
                writer.writerow([links[i]])
        page += 1
        print(links)
        if len(links)<60:
            fetching = False

def noonScrapeLinks():
    fetching = True
    baseUrl = "https://www.noon.com/egypt-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905?limit=150"
    page=1
    while fetching:
        if page==1:
            fp = urllib.request.urlopen(baseUrl)
        else:
            fp = urllib.request.urlopen(baseUrl+'&page='+str(page))
        mybytesHomepage = fp.read()
        souqHomePage = mybytesHomepage.decode("utf8")
        fp.close()
        shopAllArray = souqHomePage.split('<div class="productContainer"><a href="')
        links = []
        for i in range(0,len(shopAllArray)):
            if shopAllArray[i].split('"')[0].startswith('/egypt-en'):
                links.append(shopAllArray[i].split('"')[0])
        with open('noon_mobile_links.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(0,len(links)):
                writer.writerow(['https://www.noon.com'+links[i]])
        page += 1
        print(links)
        if len(links)<150:
            fetching = False


def jumiaScrapeLinks():
    fetching = True
    baseUrl = "https://www.jumia.com.eg/mobile-phones/"
    page=1
    while fetching:
        if page==1:
            req = Request(
                baseUrl,
                headers={'User-Agent': 'Mozilla/5.0'})
            fp = urlopen(req).read()
        else:
            req = Request(
                baseUrl+'?page='+str(page)+'#catalog-listing',
                headers={'User-Agent': 'Mozilla/5.0'})
            fp = urlopen(req).read()
        souqHomePage = fp.decode("utf8")
        shopAllArray = souqHomePage.split('<a class="core" href="')
        links = []
        for i in range(0,len(shopAllArray)):
            if shopAllArray[i].split('"')[0].endswith('.html'):
                links.append(shopAllArray[i].split('"')[0])
        with open('jumia_mobile_links.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(0,len(links)):
                writer.writerow(['https://www.jumia.com.eg'+links[i]])
        page += 1
        print(links)
        if len(links)<40:
            fetching = False
