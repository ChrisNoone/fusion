import random
from time import sleep

from numpy.ma import count
#
# str = [1,2,3,4,5,1,2,3]
# resoult = {}
# print(str.count(5555))
# for i in str:
#     resoult[i] = str.count(i)
#     print(resoult[i])
# print(resoult)
# print(resoult[i])
# list = []
# for i in range(2):
#     s = random.choice(range(0, 5))
#     print(s)
#     list.append(s)
# print(list)
# s = 111
# s0 = []
# for i in range(3):
#     s0.extend(s)
#     print(s0)
#     print(s0.count(0))
# date = 'a23da234'
# print(date[:4])
# c0 = 1
# b0 = 2
# c0 = 3
# b0 = 4
# for i in range(1000000000000000):
#     if (c0 == 1 and b0 == 2) or (c0 == 3 and b0 == 4):
#         pass
#         # print('万号正确')
#     else:
#         print('--万号错误')

# s3 = 'abc_12345'
# s4 = 'abc_12345'
# s5 = 'abc_12345'
#
# a0 = int(s3[7:]) + int(s4[7:]) + int(s5[7:])
# print(a0)


import numpy as np

# a = [1, 1, 2]
# # 先转化为numpy.ndarray
# arr = np.array(a)
#
# # 是否全部为1,False
# print((arr == 1).all())
#
# # 是否含有1,True
# print((arr == 1).any())
# if ((arr == 3).any()):
#     print('22222')
#
# a0 = ' abc1123232131'
# a1 = ' abc1122132131'
# a2 = ' abc11321321311'
# b0 = 'abc'
# m0 = [a0[13:], a1[13:], a2[13]]
# arr = np.array(m0)
# print(arr[0:])
# # 是否含有1，True
# if (arr == b0[2:]).any():
#     print('2222222222222222')
# else:
#     print('333')


# a0 = '1123232134214123331'
# a1 = '1122132232321131'
# a2 = '1132132313211311'
# m0 = [a0[13:], a1[13:], a2[13:]]
# print(m0[0])
# ss = sum(m0)
# print(ss)
# int = 20
# print(int)
#
# float =2.3
# print(float)
# import numpy as np
# a = ['1', '2', '3']
# b = ['2', '3', '4']
# c = ['3', '4', '5']
# print(np.sum([a, b, c], axis = 0))
# print(np.su,([a])



import types

#
# import urllib2
# import json
# duan = "--------------------------"	#在控制台断行区别的
# # 利用urllib2获取网络数据
#
#
# def registerUrl():
#     try:
#         url = "https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=bjpk10"
#         data = urllib2.urlopen(url).read()
#         return data
#     except Exception as e:
#         print(e)
#
#
# # 写入文件
# def jsonFile(fileData):
#     file = open("d:\json.txt","w")
#     file.write(fileData)
#     file.close()
#
# # 解析从网络上获取的JSON数据
# def praserJsonFile(jsonData):
#     value = json.loads(jsonData)
#     rootlist = value.keys()
#     print(rootlist)
#     print(duan)
#     for rootkey in rootlist:
#         print(rootkey)
#     print(duan)
#     subvalue = value[rootkey]
#     print(subvalue)
#     print(duan)
#     for subkey in subvalue:
#         print(subkey,subvalue[subkey])
#
# if __name__ == "__main__":
#     # xinput = raw_input()
#     # x = 130
#     # xvalue = cmp(x,xinput)
#     # print xvalue
#     # print x/100.0
#
#     data = registerUrl()
#     # jsonFile(data)
#
#     praserJsonFile(data)


# coding = utf-8
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "https://www.google.com.my/imghp?hl=zh-CN&tab=wi&ogbl"
driver.get(url)

#  鼠标拖放操作
'''登录流程'''
driver.find_element_by_link_text('登录').click()
driver.find_element_by_css_selector('input[type="email"]').send_keys("189636082kosun@gmail.com")
driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
sleep(1)
driver.find_elements_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")[0].send_keys('111')

