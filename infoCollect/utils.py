import requests,os
import queue

class dictScan():

    # 请求头设置
    headers = {
        'Accept': '*/*',
        'Referer': '',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
        'Connection': 'Keep-Alive',
        'Cache-Control': 'no-cache',
    }

    file_path = "/home/dckdl/PycharmProjects/dcspace/word_list.txt"

    def __init__(self):
        self.pass_list = []

    def getFiles(self):
        '''
        读取web目录字典文件，放入list中
        '''

        with open(dictScan.file_path) as infile:
            while True:
                dirdic = infile.readline().strip()
                if (len(dirdic) == 0): break
                self.pass_list.append(dirdic)
        #排序
        self.pass_list.sort()

    def crawler(self, url):
        for word in self.pass_list:
            result = requests.get(url=url)
