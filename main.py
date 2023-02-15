import glob
import os
import time

from Common.LogConfig import RunLogChart


def ma(name):
    RunLogChart(name)
    with open('DMS-常温分析.html', "a") as f:
        str = """<!doctype html>
    <html lang="zh-CN">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>DMS-常温分析</title>
        </head>
        <body>
            <div>
            <iframe frameborder="0" src="list.html" width="100%" height="3250px"></iframe>
                <iframe frameborder="0" src="cpu.html" width="100%" height="625px"></iframe>
            </div>
        </body>
    </html>"""
        f.write(str)


while True:
    name = input("请输入要解析的DMS-LOG文件名称")
    if name == "exit":
        break
    if name == "1":
        name = os.listdir(os.getcwd())
        for i in name:
            if i[-3:] == "log":
                print("找到文件",i,",开始解析")
                ma(i)
                print("请打开 DMS-常温分析.html 文件查看")
                time.sleep(6)
                break
        else:
            print("未找到以log结尾的文件，3S后退出")
            time.sleep(3)
        break
    if isinstance(name, str) and glob.glob(name):
        ma(name)
        print("请打开 DMS-常温分析.html 文件查看")
        time.sleep(6)
    else:
        print("请输入正确的地址，或者输入1，来默认读取第一个log后缀文件,或者输入exit退出")
