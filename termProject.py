from urllib.request import urlopen
from urllib.parse import urlencode,unquote,quote_plus
import urllib
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter import font

def getCount():
    testCase = "http://openapi.seoul.go.kr:8088/5147657862716c63313231784f514f77/xml/lostArticleInfo/1/1/"
    return int(ET.ElementTree(file=urllib.request.urlopen(testCase)).getroot().findtext('list_total_count'))

end = getCount() +1
start = end - 50
mylists = []

def myPrint():
    global start
    global end
    global mylists
    global mylist
    yIdx = 0
    url = "http://openapi.seoul.go.kr:8088/5147657862716c63313231784f514f77/xml/lostArticleInfo/" + str(
        start) + "/" + str(end) + "/"

    tree = ET.ElementTree(file=urllib.request.urlopen(url))
    root = tree.getroot()
    for a in root.findall('row'):
        if len(mylists) <= yIdx:
            mylists.append([])

        mylists[yIdx].append(a.findtext('GET_NAME'))
        mylists[yIdx].append(a.findtext('REG_DATE'))
        yIdx += 1
    for i in range(0,len(mylists)-1,1):
        mylist.insert(i, mylists[i])

    print(mylists)

root = Tk()
root.title('분실물 찾기 서비스')
root.geometry('600x800')
mylist = Listbox(root, selectmode = 'extended')
mylist.place(x= 20, y = 50, width = 200, height = 400)

strings = ""
textbox = ttk.Entry(root, textvariable = strings)
textbox.place(x = 20, y = 20, width = 200)

searchButton = Button(root, text="검색", overrelief = "solid", command = myPrint, repeatdelay = 1000, repeatinterval = 100)
searchButton.place(x = 220, y = 20, width = 50, height = 20)


Label1 = Label(root, text="분실 일자:", relief = 'solid')
Label1.place( x = 250, y = 80, width = 300, height = 40)

Label2 = Label(root, text="분실 품명:", relief = 'solid')
Label2.place( x = 250, y = 150, width = 300, height = 40)

Label3 = Label(root, text="분실 장소:", relief = 'solid')
Label3.place( x = 250, y = 220, width = 300, height = 40)

Label4 = Label(root, text="분실 정보", relief = 'solid')
Label4.place( x = 250, y = 300, width = 300, height = 150)

Label5 = Label(root, text="이미지", relief = 'solid')
Label5.place( x = 20, y = 500, width = 560, height = 250)

TempFont = font.Font(root, size=18, weight='bold', family='Consolas')
MainText = Label(root, font=TempFont, text="[분실물 찾기 서비스]")
MainText.place(x=350)

root.mainloop()