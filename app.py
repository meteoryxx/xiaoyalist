import datetime
import subprocess
from flask import Flask, render_template
import json
import schedule
import time
import getip


app = Flask(__name__)


def updateurl():
    # 这里应该是你的更新逻辑
    # 例如，你可以从某个URL获取新的IP列表，并将其保存到ip.json文件中
    getip.print_with_timestamp("获取IP")
    getip.get_ips()
    subprocess.run(["nginx", "-s", "reload"])
    pass


@app.route('/')
def index():
    # 读取ip.json文件
    with open('ip.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 从数据中提取IP地址列表和延迟信息，并转换为毫秒
    ip_list = [(item['ip'], round(item['delay'] )) for item in data['ips']]

    # 按延迟时间排序，最短的放在最前面
    ip_list.sort(key=lambda x: x[1])

    # 渲染模板并传递IP列表和延迟信息
    return render_template('index.html', ips=ip_list)

def run_scheduler():
    # 设置定时任务，每12小时执行一次updateurl()方法
    schedule.every(12).hours.do(updateurl)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # 在后台线程中运行定时任务
    from threading import Thread
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.start()
    #打开先执行一次
    updateurl()
    # 运行Flask应用
    app.run(host='0.0.0.0', port=5000)
