
#Руденко Филипп
#
import requests
from bs4 import BeautifulSoup

def getstih(url, encoding = "utf-8"):
    resp = requests.get(url)
    alltext = resp.text
    
    soup = BeautifulSoup(resp.content, "html.parser")

    fo = open("stih0000" + str(indf) + ".txt", "w", encoding = "utf-8")

        #33333333333333333333333333333333
    
    for i in range(len(mas)):
        indent = ""
        if i == 0:
            teg1 = "header"
            class1 = "head-content-poema"
            teg2 = "h1"
        elif i == 1:
            teg1 = "div"
            class1 = "tema-stih"
            teg2 = "a"
            indent = "\n"
        elif i == 2:
            teg1 = "article"
            class1 = "block-poema"
            teg2 = "p"
        textstih = soup.find(teg1, class_ = class1)
        content3 = textstih.find_all(teg2)
        for line in content3:
            fo.write((line.text) + indent + "\n")
        
        #33333333333333333333333333333333
        
    fo.close()

f = open("input.txt")
mas = f.read().split("\n")
indf = 0
for url in mas:
    print(" ")
    if url != "":
        indf +=1
        getstih(url)
f.close()  
