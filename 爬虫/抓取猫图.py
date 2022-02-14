import urllib.request

response = urllib.request.urlopen("http://placekitten.com/500/500")
cat_img = response.read()

with open("cat_500_500.jpg","wb") as f:
    f.write(cat_img)

print(response.geturl())#http://placekitten.com/500/500 获取url
print(response.info())#查看该网站的各种信息，访问时间，服务器等..
print(response.getcode())#200  表示正常
