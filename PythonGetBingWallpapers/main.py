def urlget(source):
    import bs4 # not import beaut...
    #不像Test需要打开文件与转码
    xmlword = bs4.BeautifulSoup(source,"html.parser")
    xmlword = xmlword.images.url #识别<images><url>
    word = xmlword.get_text()
    return word

def apiget():
    import requests
    xml = requests.get("https://cn.bing.com/HPImageArchive.aspx?n=1")
    xml = xml.text
    return xml

def groupit(halflink):
    urllist = ["https://cn.bing.com"]
    urllist.append(halflink)
    urllist = "".join(urllist)
    return urllist

link = apiget()
link = urlget(link)
link = groupit(link)
print(link)
#Fin