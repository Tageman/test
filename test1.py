# coding=utf-8

import sys
import re
import urllib

class YouDao(object):

    def __init__(self,url,word):
        self.url = url
        self.word = word

    def serach_youdao(self):
        response = urllib.urlopen(self.url).read()
        searchSuccess = re.search(r"(?s)<div class=\"trans-container\">\s*<ul>.*?</div>", response)
        if searchSuccess:
            means = re.findall(r"(?m)<li>(.*?)</li>", searchSuccess.group())  # 获取我们想提取的核心单词释义
            print "释义："
            for mean in means:
                print "\t" + mean  # 输出释义
        else:
            print "未查找到释义."


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print 'usage: python test1.py  /需要查找的单词/'
        sys.exit()
    word = ' '
    for x in range(len(sys.argv)-1):
        word = word +' '+ sys.argv[x+1]
    word = word.lstrip()
    print word
    url = "http://dict.youdao.com/search?q=" + word + "&keyfrom=dict.index"
    YouDao(url,word).serach_youdao()