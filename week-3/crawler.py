import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
def getData(url):

  

    request=req.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")


    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") 
    titles=root.find_all("div",class_="title")
    
    with open("movie.txt","a",encoding="utf-8") as file:
        
        for title in titles:
                
            if title.a !=None and title.a.string[0:3].__contains__('負雷'):
                file.write(title.a.string+"\n")
                    
           

        nextLink=root.find("a",string="‹ 上頁")
        return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/movie/index.html"   
count=0
while count<10:
    pageURL="http://www.ptt.cc"+getData(pageURL) 
    count+=1