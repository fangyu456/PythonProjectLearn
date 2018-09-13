from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
import mycolor


html1 = open('example1.html').read()
html2 = open('example2.html').read()
response1 = HtmlResponse(url='http://example1.com', body=html1, encoding='utf8')
response2 = HtmlResponse(url='http://example2.com', body=html2, encoding='utf8')



le = LinkExtractor()
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('allow 参数 --------'))
pattern = '/intro/.+\.html$'
le = LinkExtractor(allow=pattern)
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('deny 参数 --------'))
print('“示例　提取页面example1.html中所有站外链接（即排除站内链接）”')
pattern1 = pattern1 = '^' + urlparse(response1.url).geturl()
print(pattern1)
le = LinkExtractor(deny=pattern1)
links = le.extract_links(response1)
for link in links:
    print(link)