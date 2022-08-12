# from urllib.request import Request, urlopen
# from urllib.parse import urlencode
import requests
from lxml import etree
import re

url ='https://startup-mitteldeutschland.de/startups/'

headers={
          'Cookie': '_ga=GA1.1.1264639838.1656255816; __gads=ID=11bf5172a8fed023-22b03c0ce3cd00b6:'
                   'T=1659532896:RT=1659532896:S=ALNI_MbJBCP_xuzFH_t52bZApd1AVSs2og; _ga_0BXL4J9E2E=GS1.1.1660316184.7.1.1660317171.0',
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like '
                          'Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

}

# req = Request(url = url,
#               headers= headers)
# response: object =urlopen(req)
response = requests.get(url=url,
                        headers=headers)

html =response.content.decode()
tree = etree.HTML(html)
#result = etree.tostring(tree, encoding='utf-8').decode()
startupsname =tree.xpath('//*[@id="page-7106"]/div/div[1]//a/text()')
print(startupsname)
#result = etree.tostring(startupsname[0], encoding='utf-8').decode()
#print(result)
#href =startupsname[0].xpath('//*[@id="page-7106"]/div/div[1]/ul/li[1]/a')
#print(href)

# p1 =re.compile(r'<div class="startup__list">(.*?)</div>')
# titles = p1.findall(response.text)
# print(titles)