import xml.etree.cElementTree as ET
import requests
from bs4 import BeautifulSoup
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
urlList = {}
# Run through the links of sitemap and the urls within it
def links(url):
    xmlDict = {}
    r = requests.get(url)
    xml = r.text
    soup = BeautifulSoup(xml, 'lxml')
    sitemapTags = soup.find_all("sitemap")
    print("The number of sitemaps are {0}".format(len(sitemapTags)))
    for sitemap in sitemapTags:
        xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text
        print(xmlDict)
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
    tree.write("Output.xml")
    return urlList
# provide the link here
links("https://wiprodigital.com/sitemap.xml")
