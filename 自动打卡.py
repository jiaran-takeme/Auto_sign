# -*- coding: utf-8 -*-

import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

now = time.localtime() # 时间
nowt = time.strftime("%Y-%m-%d %H:%M:%S", now)  # 设定时间格式

def send_email(content):
    msg = MIMEText(content, 'html', 'utf-8')  # 正文
    msg['From'] = formataddr(["自动打卡","发送的邮箱"])  # 发信人
    msg['Subject'] = "自动打卡"  # 标题

    server = smtplib.SMTP_SSL("服务器地址")
    server.login("发送的邮箱", "授权码")
    server.sendmail("发送的邮箱", "接收的邮箱", msg.as_string())
    server.quit()

try:
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')  # 设置无头启动
    browser = webdriver.Chrome(options=option)  # 调用无头的谷歌浏览器

    #browser = webdriver.Chrome()  # 调用有窗口的浏览器
    #browser.set_window_size(1920, 1080)

    browser.implicitly_wait(10)  # 隐式等待
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")
    print('打开网站了！')

    try:
        browser.find_element(By.XPATH,'//*[@id="details-button"]').click()
        browser.find_element(By.XPATH, '//*[@id="proceed-link"]').click()
    except:
        pass

    browser.find_element(By.NAME,"uid").send_keys("学号")  # 学号
    browser.find_element(By.NAME,"upw").send_keys("密码\n")  # 密码
    print('登陆上去了！')
    
    time.sleep(1)

    browser.switch_to.frame('zzj_top_6s')
    browser.find_element(By.XPATH,'/html/body/form/div/div[11]/div[3]/div[4]/span').click()
    print('打开打卡页面了！')
    time.sleep(6)
    
    try:
        browser.find_element(By.ID, 'btn416a').click()
        print('从上面打的')
    except:
        browser.find_element(By.ID, 'btn416b').click()
        print('从下面打的')
    
    a = browser.find_element(By.XPATH,'//*[@id="bak_0"]/div[2]/div[2]/div[2]/div[2]').text
    result = "success"
    print(result + a)
    browser.quit()
    send_email(result + a)  # 发送邮件

except:
    result = "error"  # 异常处理
    print(result)
    browser.quit()
    send_email(result)  # 发送邮件
   
# 写入日志
with open("打卡日志.txt", 'a') as f:
    f.write(f"{nowt} {result}\n")
    f.close()

