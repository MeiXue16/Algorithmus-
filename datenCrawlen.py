from urllib.request import Request, urlopen, urlretrieve
from urllib.parse import quote, urlencode
#quote('前锋') 对中文字符进行编码
#urlencode( {'wd':'前锋', 'query':'python'} )对中文字符字典编码

import ssl
ssl._create_default_https_context =ssl._create_unverified_context

def search_startups():

    url ='https://startup-mitteldeutschland.de/startups/'
    request = Request(url,
                      headers={
                          'Cookie':'_ga=GA1.1.1264639838.1656255816; __gads=ID=11bf5172a8fed023-22b03c0ce3cd00b6:'
                                   'T=1659532896:RT=1659532896:S=ALNI_MbJBCP_xuzFH_t52bZApd1AVSs2og; _ga_0BXL4J9E2E=GS1.1.1660316184.7.1.1660317171.0',
                          'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like '
                          'Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
                      })
    #response=urlopen(url)
    response = urlopen(request)
    assert response.code ==200
    print('Anfrage erfolgreich')

    bytes_ = response.read()
    bytes_.decode('utf-8')
    #print(response.getheader('Content-Type'))
    #当对象进入上下文时，调用对象的
    #当对象退出上下文
    with open('startups.html','wb' ) as file:
        file.write(bytes_)

# def download_img(url):
#     filename =url[url.rfind('/')+1:]
#     urlretrieve(url, filename)

search_startups()
# download_img('https://spinlab-wp.s3.eu-central-1.amazonaws.com/wp-content/uploads/2017/03/smd_logo3_resized.svg')


