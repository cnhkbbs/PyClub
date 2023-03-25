# -*- coding: utf-8 -*-
# author SBOXM
# github: https://github.com/cnhkbbs/PyClub
# 基于selenium的PTA实验题爬虫
# 使用前请确保你已正确安装并配置驱动
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')  # chrome驱动路径
chrome = webdriver.Chrome(service=service)

# 配置项

name = '123456@qq.com'  # 账号
pwd = '123456'  # 密码
datapath = r'C:\Users\Administrator\Desktop\ '  # 保存路径(需要绝对路径)
safe_time = 3  # 安全间隔时间


def auto_Login():
    chrome.get('https://pintia.cn/auth/login')  # 打开登录页面
    chrome.find_element(By.ID, 'username').send_keys(name)
    chrome.find_element(By.ID, 'password').send_keys(pwd)
    chrome.find_element(By.CLASS_NAME, 'welcome_QBoe0').click()
    login = chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/form')
    login.submit()


def get_problems(url, name):
    time.sleep(1)

    while 1:
        try:
            title = chrome.find_element(By.XPATH,
                                        '/html/body/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/span').text
            anser = chrome.find_element(By.CSS_SELECTOR, 'textarea').get_attribute('value')
            print("当前题目  " + title)
            print("答案\n" + anser)
            # 写入文件
            stars = "************************************************************\n"
            with open(datapath + str(name) + '.txt', 'a', encoding='utf-8') as f:
                f.write(title + "\n")
                f.write(anser + "\n")
                f.write(stars)
        except NoSuchElementException:
            print("元素定位异常，请手动修改XPATH")
            print(NoSuchElementException)

        try:
            chrome.find_element(By.XPATH,
                                '/html/body/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/a/div/div[1]').click()
        except:
            # 捕获点击异常跳出循环
            break
        time.sleep(safe_time)


def main():
    chrome.maximize_window()
    auto_Login()
    countname = 1  # 文件名计数(非必要不动)
    while 1:
        print("键入起始题目地址")
        TargetURL = input()
        chrome.get(TargetURL)
        get_problems(TargetURL, countname)

        print("继续获取题目？  yes/no")
        agin = input()
        if agin == 'no':
            break
        countname += 1


main()
