# asn-scraper 
ASNs (Autonomous System Numbers) are one of the building blocks of the
Internet. This project is to create a mapping from each ASN in use to the
company that owns it. For example, ASN 36375 is used by the University of
Michigan - http://bgp.he.net/AS36375

Starting at http://bgp.he.net/report/world, the program will crawl and scrape the linked country
reports to make a structure mapping each ASN to info about that ASN.  
  
Sample structure:  

&nbsp;&nbsp;&nbsp;&nbsp;{3320: {'Country': 'DE',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Name': 'Deutsche Telekom AG',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Routes v4': 13547,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Routes v6': 268},  
&nbsp;&nbsp;&nbsp;&nbsp;36375: {'Country': 'US',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Name': 'University of Michigan',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Routes v4': 14,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Routes v6': 1}}  

When done, the collected data will be outputted to a json file.
