import urllib, urllib2
url = "http://data.bter.com/api/1/ticker/btc_cny"
agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
headers = {"User-agent" : agent}
req = urllib2.Request(url, headers = headers)
res = urllib2.urlopen(req)
res = res.read()
print(res)
