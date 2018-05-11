# importing needed librarie
import xml.etree.cElementTree as ET

import requests
from bs4 import BeautifulSoup

# build the root element of the xml
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
urlList = {}
# Run through the links of sitemap and the urls within it
def links(url):
    xmlDict = {}
    # hitting the urls and getting responses, the responses will be the urls in sitemap
    r = requests.get(url)
    xml = r.text
    soup = BeautifulSoup(xml, 'lxml')
    sitemapTags = soup.find_all("sitemap")
    print("The number of sitemaps are {0}".format(len(sitemapTags)))
    #going through the various links and initializing it to a dictionary so each url in sitemap has many urls
    for sitemap in sitemapTags:
        xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text
        print(xmlDict)
    #each url sitemap will return many urls which is then build into an xml
    for i in xmlDict:
        r = requests.get(i)
        xml = r.text
        soup = BeautifulSoup(xml, 'lxml')
        sitemapTags = soup.find_all("url")
        j = 0
        # build an xml
        for sitemap in sitemapTags:
            j = j + 1
            ET.SubElement(doc, "field" + str(j), name=i).text = sitemap.findNext("loc").text
            tree = ET.ElementTree(root)
    #saving to an output.xml
    tree.write("Output.xml")
    return urlList
# provide the link here
links("https://wiprodigital.com/sitemap.xml")
