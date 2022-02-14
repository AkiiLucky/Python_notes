import urllib.request
response = urllib.request.urlopen("https://www.lianaiyx.com/")
html = response.read()
html = html.decode("utf-8")
print(html)




