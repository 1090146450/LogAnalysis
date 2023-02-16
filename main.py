import datetime
import os
import time

from Common.LogConfig import RunLogChart


def ma(name, time_da):
    RunLogChart(name, time_da)
    with open(f'DMS-常温分析{time_da}.html', "a") as f:
        str_t = f"""<!doctype html>
    <html lang="zh-CN">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>DMS_常温分析</title>
        </head>
        <body>
            <div>
            <iframe frameborder="0" src="fps_config{time_da}.html" width="100%" height="3250px"></iframe>
                <iframe frameborder="0" src="cpu_config{time_da}.html" width="100%" height="625px"></iframe>
            </div>
        </body>
    </html>"""
        f.write(str_t)


while True:
    time_da = datetime.datetime.now().strftime("%M%S")
    name = input("请输入执行操作:\n"
                 "1:执行第一个.log文件\n"
                 "2:查看并输入.log文件序号运行\n"
                 "0:退出\n")
    log_all = []
    for i in os.listdir(os.getcwd()):
        if i[-3:] == "log":
            log_all.append(i)
    if name == "0":
        break
    elif len(log_all) == 0:
        print("未找到.log文件，3S后退出")
        time.sleep(3)
        break
    elif name == "1":
        print(f"开始执行文件{log_all[0]}......")
        try:
            ma(log_all[0], time_da)
        except Exception as e:
            print(f"执行失败！原因{e}")
            time.sleep(6)
        print(f"执行完毕请查看:DMS-常温分析{time_da}.html")
        time.sleep(6)
        break
    elif name == "2":
        for i in range(len(log_all)):
            print(f"{i}.{log_all[i]}")
        name = input("请输入序号进行运行\n")
        try:
            name = int(name)
        except Exception as e:
            print("请输入数字！")
        if name not in range(len(log_all)):
            print("您输入的序列表错误")
            break
        print(f"开始执行文件{log_all[name]}......")
        try:
            ma(log_all[name], time_da)
        except Exception as e:
            print(f"执行失败！原因{e}")
            time.sleep(6)
        print(f"执行完毕请查看:DMS-常温分析{time_da}.html")
        time.sleep(6)
        break