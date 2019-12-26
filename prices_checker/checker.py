import urllib.request, urllib.error, urllib.parse

url = 'https://eshop-prices.com/prices?currency=BRL'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
output_filename = 'eshop-prices.html'
test_filename = 'eshop-prices-test.html'
requesting = False

if requesting:
    req = urllib.request.Request(url, data=None, headers={'User-Agent' : user_agent})
    response = urllib.request.urlopen(req)
    content = response.read()
else:
    contents = open(test_filename, "rt", encoding="utf-8")
    content = contents.readlines()
    

file_handle = open(output_filename, "wt", encoding="utf-8")
file_handle.writelines(content[0])
#file_handle.writelines(content[22:])

    #25792:])


file_handle.close()



