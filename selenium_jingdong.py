#!/usr/bin/python3
# _*_coding:utf-8_*_
'''
例子:爬取京东商品信息
商品名称
价格
数量
店名称
//改进:1.滑动滚轮到页面底部
2.点击下一页
//改进1.显性等待
2.隐性等待
'''
from selenium import webdriver
import time


# 获取页面信息
def get_page(url, name, page):
    # 点击页面
    browser = webdriver.Chrome()
    browser.get(url)
    input = browser.find_element_by_id('key')
    input.send_keys(name)
    button = browser.find_element_by_xpath("//button[@class='button']/i[@class='iconfont']")
    time.sleep(3)
    button.click()
    time.sleep(2)
    # 将滚轮滑到底部
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(10)
    # 获取二级界面的属性
    goods_name = browser.find_elements_by_xpath("//div[@class='p-name p-name-type-2']/a/em")
    goods_price = browser.find_elements_by_xpath("//div[@class='p-price']//i")
    comment_count = browser.find_elements_by_xpath("//div[@class='p-commit']/strong")
    shop_name = browser.find_elements_by_xpath("//span[@class='J_im_icon']/a")
    # 将滚轮滑到底部
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    L = []
    N = []
    P = []
    C = []
    S = []
    for i in goods_name:
        N.append(i.text)
    for m in goods_price:
        P.append(m.text)
    for c in comment_count:
        C.append(c.text)
    for s in shop_name:
        S.append(s.text)
    L.append(N)
    L.append(P)
    L.append(C)
    L.append(S)
    return L


# 保存信息
def save_info(info, name):
    for i in info:
        with open('{}.txt'.format(name), 'a', encoding='utf-8') as f:
            f.write(i + '\n')


# 主函数
def main(name, page):
    # 基础参数
    url = "https://www.jd.com/"
    info = get_page(url, name, page)
    for i in info:
        save_info(i, name)


if __name__ == '__main__':
    name = input('请输入要检索的物品:')
    page = int(input("请输入要爬取的页数:"))
    main(name, page)
