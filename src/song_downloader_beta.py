__author__ = 'Shashi'
import os
from bs4 import BeautifulSoup
import urllib2
import re
query=raw_input("Input Movie Name : ")
rename=query
path = "E:\\Summertime Coding\\python\\mp3 downloader\\"+query+"\\"
query=query+" songs.pk"
query = re.sub(r"\s+", '+', query)
url="https://www.google.co.in/search?client=opera&q="+query+"&sourceid=opera&ie=UTF-8&oe=UTF-8"
headers = { 'User-Agent' : 'Mozilla/5.0' }
url = urllib2.Request(url, None, headers)
r = urllib2.urlopen(url)  # request package: use it to request any url.
data = r.read()
soup = BeautifulSoup(data)
href = soup.find('h3').find('a').get('href')
href="https://www.google.co.in"+href
url=href
headers = { 'User-Agent' : 'Mozilla/5.0' }
url = urllib2.Request(url, None, headers)
r = urllib2.urlopen(url)  # request package: use it to request any url.
c=1;
data = r.read()
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    hy=link.get('href')
    if(hy.find("songid"))!=-1:
        print "Requesting Download : ", hy
        headers = { 'User-Agent' : 'Mozilla/5.0' }
        down = urllib2.Request(hy, None, headers)
        resource = urllib2.urlopen(down)
        s=rename+"_"+str(c)+".mp3"
        name=s
        if not os.path.exists(path):
            os.makedirs(path)
        s = os.path.join(path, s)
        print "Downloading Starts, Saving {0}.mp3 to location : {1}".format(name,s)
        meta = resource.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print("Total Bytes: {0}".format(file_size))
        output = open(s,'wb')
        downloaded_bytes = 0
        block_size = 1024*8
        while True:
            buffer = resource.read(block_size)
            if not buffer:
                break
            output.write(buffer)
            downloaded_bytes += block_size
            p=float(downloaded_bytes)/float(file_size)*100
            print "Downloaded %.2f %% \r" %p,
        if downloaded_bytes>=file_size:
            print "Downloaded - 100%% "
        output.close()
        c+=1