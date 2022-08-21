import os
import re
import datetime


def walkfile(file_dir):
    # 遍历文件夹获得files
    stockfiles = []
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            stockfiles.append(os.path.join(root, f))
    return stockfiles


def selectfile(stockfiles, now):
    for file in stockfiles:
        time = getdate(file)
        if now == time:
            return file


def getstocks(path):
    # path:D:\工具软件应用\HTZQTDX\T0002\blocknew
    # 获得文件中股票
    f = open(path)
    lines = f.readlines()
    content = [stock.strip() for stock in lines if stock.strip()]
    print(content)
    return content


def getdate(fpath):
    # 返回固定时间格式
    name = os.path.basename(fpath)
    fname = os.path.splitext(name)[0]
    # datestr = ('2021.' + fname).replace('.', '-')
    datestr = ('20' + fname).replace('.', '-')
    time = datetime.datetime.strptime(datestr, '%Y-%m-%d').strftime('%Y-%m-%d')
    print('time:', time)
    return time


def rename(fpath):
    # rename file
    dirname, fname = os.path.split(fpath)
    print(os.path.split(fpath))
    time = getdate(fpath)
    time = time.replace('-', '.')[2:]
    newname = time + '.blk'
    newpath = dirname + '\\' + newname
    print('newpath:', newpath)
    os.rename(fpath, newpath)


def checkfile():
    pattern = re.compile(r'\d+', re.I)
    print()

if __name__ == '__main__':
    # walkfile("D:\工具软件应用\HTZQTDX\T0002\\blocknew")
    n = ['1', '2']