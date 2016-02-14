from BeautifulSoup import BeautifulSoup
f = open('/home/kajal/sentiment-project/rawdata/x.html')
x = f.read().decode('utf-8')
raw = BeautifulSoup(x)
print raw