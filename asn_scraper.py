#!/usr/bin/env python

import urllib2
import bs4
import re
import json

SITE = 'http://bgp.he.net'

#return soup given the url
def url_to_soup(url):
    #bgp.he.net is filtered by user-agent
    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib2.urlopen(req).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup

#return list of country pages given soup
def find_pages(page):
    print "Collecting List of Pages..."
    pages = []

    #append any tag with a country link
    for link in page.find_all(href=re.compile('/country')):
        pages.append(link.get('href'))

    return pages

#scrape pages for ASN data and return as dict, given a list of page links
def scrape_pages(links):
    mappings = {}

    print "Scraping Pages for ASN Data..."

    for link in links:
        #create soup
        country_page = url_to_soup(SITE + link)

        #get country abbreviation
        current_country = link.split('/')[2]

        #table row
        for row in country_page.find_all('tr'):
            #table column
            columns = row.find_all('td')

            #assert not empty
            if len(columns) > 0:
                #remove AS from each ASN entry
                current_asn = re.findall(r'\d+', columns[0].string)[0]

                name = columns[1].string
                routes_v4 = columns[3].string
                routes_v6 = columns[5].string

                #add entry to dict
                mappings[current_asn] = {'Country': current_country,
                                         'Name': name,
                                         'Routes v4': routes_v4,
                                         'Routes v6': routes_v6}
    return mappings

#given a dict of the mappings, output to JSON file
def create_json(mapping):

        j = json.dumps(mapping, indent=4, sort_keys=False)
        f = open('data.json', 'w')
        print >> f, j
        f.close()
        print "Outputted to JSON file"
        print "DONE"

#Main Program
#main page
print "AUTOMONOUS SYSTEM NUMBER SCRAPER\n"
print "Creating Soup..."
main_page = url_to_soup(SITE + '/report/world')

#get links to country pages
country_links = find_pages(main_page)

#scrape pages for asn info
asn_mappings = scrape_pages(country_links)

#write to json
create_json(asn_mappings)