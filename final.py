# -*- coding:cp949 -*-

import requests,collections,operator,sys,re
from bs4 import BeautifulSoup

with open("sample.txt",'w') as f:
    req=requests.get('https://www.songtexte.com/songtext/freddie-mercury/bohemian-rhapsody-23982857.html')
    hp=BeautifulSoup(req.content,"html.parser")
    lr=hp.find_all(id="lyrics")
    for i in lr:
        f.write(i.get_text())

#--h 옵션
def print_histo(filename):
    with open("sample.txt",'r') as h:
        data=' '.join(re.findall('[a-zA-Z]+',h.read()))
        data=data.lower()
        data=collections.Counter(data.split(' '))
        data=sotred(dict(data).items(),key=operator.itemgetter(1),reverse=True)
        for i in data:
            print '{0} : {1}'.format(i[0],'*'*int(i[1]))

#--t 옵션
def print_top(filename):
    with open("sample.txt",'r') as t:
        data=' '.join(re.findall('[a-zA-Z]+',t.read()))
        data=data.lower()
        data=collections.Counter(data.split(' '))
        data=sorted(dict(data).items(),key=operator.itemgetter(1),reverse=True)
        n=1
        for i in data:
            print '{0}. {1} : {2}'.format(n,i[0],i[1])
            n=n+1
            if n == 6:
                break
            else:
                continue

#--c 옵션
def print_dict(filename):
    with open("sample.txt",'r') as c:
        data=' '.join(re.findall('[a-zA-Z]+',c.read()))
        data=data.lower()
        data=collections.Counter(data.split(' '))
        data=sorted(dict(data).items(),key=operator.itemgetter(1),reverse=True)
        n=dict()
        for i in data:
            n[i[0]]=i[1]
        print n



def main():
    if len(sys.argv) != 3:
        print 'usage: python [파일이름] {-c | -t | -h} [대상파일]'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '-c':
        print_dict(filename)
    elif option =='-t':
        print_top(filename)
    elif option =='-h':
        print_histo(filename)
    else:
        print 'unknown option:'+option
        sys.exit(1)

if __name__ == "__main__":
    main()
