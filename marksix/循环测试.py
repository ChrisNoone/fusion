# for i in range(2):
#     #if i < 3:
#     print('aaaa')
#     for j in range(5):
#         print('bbbb')
#         print('$$$$$$$')
#     print('----------------')

# for i in range(4):
#     print(i)
#
# else:
#     print("循环完整执行一次。")
# print('---------------------')
#
# for a in range(10):
#     for b in range(10):
#         for c in range(10):
#             for d in range(10):
#                 for e in range(10):
#                     print(a, b, c, d, e)
#                     print('52222')
#                     if e == 2:
#                         print('eeeeee')
#                         break
#                 if d == 0:
#                     print('dddddd')
#                     break
#             if c == 0:
#                 print('ccccccc')
#                 break
#         if b == 0:
#             print('bbbbbbbbbbb')
#             break
#     if a == 2:
#         print("内重循环即将被break")
#         print("aaaaaaaaaaaaaa")
#         break
#     else:
#         print("内重循环完整执行一次。")
#
# else:
#     print(u"外重循环完整执行一次。")


#
#
# # 测试同号
# i=0
# for a in range(5):
#     for b in range(5):
#         for c in range(5):
#             print(a, b, c, )
#             print('52222')
#             if a == b or b == c or a == c:
#
#                 i = i+1
#                 print('次数是' + str(a), str(b), str(c) + str(i))
import linecache
import random
# 生成需要的号码列表
import re
import time

import numpy
from selenium import webdriver

betnums = range(1, 10)
# 将号码列表转换为字符串列表

# i = random.choice(betnums)
# n = range(1, 1000)
# k = range(1, 9)
# k1 = random.choice(k)

# # 循环10次
# for g in range(20):
#     for i in random.choice(str(n)):
#
#         # 通过sample函数从列表中随机选取2个数
#         # 这里随机数要小于上面最长的长度
#         # betnum = random.sample(betnums, 9)
#         betnum = random.sample(betnums, k1)
#         # 转换成需要的格式
#         print(betnum)


# n1 = random.randint(1, 20)
# print('n1:   ' + str(n1))
# k1 = random.randint(1, 9)
# print('k1    ' + str(k1))
# # 循环10次
# for n in range(n1):
#     for kk in range(k1):
#         print('kk    ' + str(kk))
#
#         # for i in range(n1):
#         #     print('nnnnn:    ' + str(i))
#
#         # 通过sample函数从列表中随机选取2个数
#         # 这里随机数要小于上面最长的长度
#         # betnum = random.sample(betnums, 9)
#         betnum = random.sample(betnums, k1)
#         print('随机的位置数目:' + str(k1))
#         # 转换成需要的格式
#         print(betnum)
#         # if k1 == 1:
#         #     print('cccc')
#         #     break
#         #break
    #break

# for i in range(10):
#     a = random.choice(range(1, 10))
#     b = random.choice(range(1, 10))
#     c = random.choice(range(1, 10))
#     print(a, b, c)


#for i in range(10):
    # a = random.randint(1, 9)
    # print(a)
    # b = random.randint(1, 9)
    # c = random.randint(1, 9)
    # a1 = random.sample(range(1, 10), a)
    # b1 = random.sample(range(1, 10), b)
    # c1 = random.sample(range(1, 10), c)
    # print(a1, b1, c1)
#
# for i in range(100):
#     a0 = random.sample(range(0, 10), 9)
#     b0 = random.sample(range(0, 10), 9)
#     c0 = random.sample(range(0, 10), 9)
#     d0 = random.sample(range(0, 10), 9)
#     e0 = random.sample(range(0, 10), 9)
#     # print(a0, b0, c0)
#     a1 = random.choice(a0)
#     b1 = random.choice(b0)
#     c1 = random.choice(c0)
#     d1 = random.choice(d0)
#     e1 = random.choice(e0)
#     # print(a, b, c)
#     a2 = random.sample(range(1, 10), a1)
#     b2 = random.sample(range(1, 10), b1)
#     c2 = random.sample(range(1, 10), c1)
#     d2 = random.sample(range(1, 10), d1)
#     e2 = random.sample(range(1, 10), e1)
#     if a2 == [] or b2 == [] or c2 == []:
#         # print('空')
#         pass
#     else:
#
#         print('组合是：' + str(a2), str(b2), str(c2), str(d2), str(e2))
    # for a in a2:
    #     print('aaaaa:' + str(a))
        # for b in b2:
        #     print('bbbbb: ' + str(b))
        #     for c in c2:
        #         print('cccccc: ' + str(c))

# for i in range(0, 5):
#     for j in range(0, 5):
#         for k in range(0, 5):
#             print(i, j, k)


# for i in range(100):
#     a0 = random.sample(range(0, 4), 9)
#     b0 = random.sample(range(0, 4), 9)
#     c0 = random.sample(range(0, 4), 9)
#     d0 = random.sample(range(0, 4), 9)
#     e0 = random.sample(range(0, 4), 9)
#     # print(a0, b0, c0)
#     a1 = random.choice(a0)
#     b1 = random.choice(b0)
#     c1 = random.choice(c0)
#     d1 = random.choice(d0)
#     e1 = random.choice(e0)
#     # print(a, b, c)
#     a2 = random.sample(range(1, 10), a1)
#     b2 = random.sample(range(1, 10), b1)
#     c2 = random.sample(range(1, 10), c1)
#     d2 = random.sample(range(1, 10), d1)
#     e2 = random.sample(range(1, 10), e1)
#     if a2 == [] or b2 == [] or c2 == []:
#         # print('空')
#         pass
#     else:
#
#         print('组合是：' + str(a2), str(b2), str(c2), str(d2), str(e2))

#任选2个位置并各选1个号码组成一注。
#
# for i in range(100):
#     a0 = random.sample(range(0, 5), 2)
#     b0 = random.sample(range(0, 10), 1)
#     # print(a0, b0, c0)
#     a1 = random.choice(a0)
#     b1 = random.choice(b0)
#
#     # print(a, b, c)
#     a2 = random.sample(range(1, 10), a1)
#     b2 = random.sample(range(1, 10), b1)
#
#     if a2 == [] or b2 == [] :
#         # print('空')
#         pass
#     else:
#
#         print('组合是：' + str(a2), str(b2), )
#
# for i in range(0, 10):
#     print(i)
#     print("%02d" % i)

# 通过切片去掉三位相同的数字
# for i in range(0, 1000):
#     a = "%03d" % i
#     # 取数组第一个数字
#     s0 = a[0]
#     s1 = a[1]
#     s2 = a[2]
#    # print(s0)
#     if s0 == s1 == s2:
#         #pass
#         print('aaaa:' + str(a))
#     else:
#         pass
#


# for i in range(100):
#         a0 = range(0, 5)
#         b0 = range(0, 5)
#         c0 = range(0, 5)
#         d0 = range(0, 5)
#         e0 = range(0, 10000)
#         a1 = random.choice(a0)
#         b1 = random.choice(b0)
#         c1 = random.choice(c0)
#         d1 = random.choice(d0)
#         e1 = random.choice(e0)
#         #
#         e2 = "%04d" % e1
#         #print('输入的文本是e2:    ' + str(e2))
#         #if a1 != b1 and b1 != c1 and c1 != d1 and a1 != c1:
#         if a1 == b1 or a1 == c1 or a1 == d1:
#             #print("ccccccc:" + str(a1) + str(b1) + str(c1) + str(d1))
#             pass
#         else:
#             print("aaa:" + str(a1) + str(b1) + str(c1) + str(d1))
#             pass
#            # self.base_driver.forced_wait(1)
#

# #遍历时间测试
# import time
# import numpy as np
# a = np.random.rand(10000000)
# b = np.random.rand(10000000)
# tic = time.time()
# c = np.dot(a, b)
# toc = time.time()
# print(c)
# print('V:  ', str(1000*(toc-tic)) + 'ms')
#
# c = 0
# tic1 = time.time()
# for i in range(1000000):
#     c += a[i]*b[i]
# toc1 = time.time()
# print(c)
# print('F:  ', str(1000*(toc1-tic1)) + 'ms')


#
#
# list2d = [[1,2,3],[4,5]]
# sum = 0
# for i in list2d:
#     for j in i:
#         sum += j
# print(sum)
#
# import numpy as np
#
#
#
# x = np.array([[1,2,5],[2,3,5],[3,4,5],[2,3,6]])
# # 输出数组的行和列数
# print(x.shape)  # (4, 3)
# # 只输出行数
# print(x.shape[0]) # 4
# # 只输出列数
# print(x.shape[1]) # 3
#


# a = range(0, 5)
# b = range(0, 10)
# print(len(a))
# print(len(b))
# list=[]
# for i in range(10):
#     for j in range(5):
#         list.append(i)
#         list.append(j)
#         break
# print(list)

# from numpy import *
# a1=array([1,2,3])
# a1=mat(a1)

#创建常见的矩阵

# data1=mat(zeros((3,3)))
# # 创建一个3*3的零矩阵，矩阵这里zeros函数的参数是一个tuple类型(3,3)
# print(data1)
# data2=mat(ones((2,4)))
# # 创建一个2*4的1矩阵，默认是浮点型的数据，如果需要时int类型，可以使用dtype=int
# data3=mat(random.rand(2,2))
# # 这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，需要将其转换成#matrix
# data4=mat(random.randint(10,size=(3,3)))
# # 生成一个3*3的0-10之间的随机整数矩阵，如果需要指定下界则可以多加一个参数
# data5=mat(random.randint(2,8,size=(2,5)))
# # 产生一个2-8之间的随机整数矩阵
# print(data5)


#
# a=[]
# for i in range(2):
#     a.append([])
#     for j in range(2):
#         a[i].append(0)
# print(a)
# for i in range(10):
#     for j in range(10):
#         if i >= j:
#             print('11111:' + str(i), str(j))
#             pass
#         else:
#             pass
#             # print(i, j)
#

#
# for i in range(100):
#     d0 = range(0, 100)
#     d1 = random.choice(d0)
#     d2 = "%02d" % d1
#     print(d2)

# for i in range(100):
#     d0 = range(0, 100)
#     d1 = random.choice(d0)
#     d2 = "%02d" % d1
#     # 取数组第一个数字
#     s0 = d2[0]
#     s1 = d2[1]
#     print(d2)
#     if s0 == s1:
#         pass
#     else:
#         print("数据是：" + str(d2))

# a = random.choice(range(0, 11))
# b = random.choice(range(0, 11))
# c = random.choice(range(0, 11))
# d = random.choice(range(0, 11))
# e = random.choice(range(0, 11))
# f = random.choice(range(0, 11))
#
# s = [a,b,c,d,e,f]
#
# for i in range(1000):
#     a = random.choice(range(0, 28))
#     if a <= 14:
#         print("第一排：  " + str(a))
#
#     else:
#         pass
#         print("第二排：  " + str(a-14))


# for i in range(100):
#     d0 = range(0, 12)
#     d1 = random.choice(d0)
#     d2 = random.choice(d0)
#     d3 = random.choice(d0)
#     a2 = "%02d" % d1
#     a3 = "%02d" % d2
#     a4 = "%02d" % d3
#     print('1111111：   ' + str(a2))
#     print('2222222：   ' + str(a3))
#     print('3333333：   ' + str(a4))
#     #if s0 == s1 or s1 == s2 or s1 == s2 or s0 != 11 or s1 != 11 or s2 != 11:
#     if a2 == a3 or a2 == a4 or a3 == a4:
#         # print('有相同号码的数字是：   ' + str(s0) + str(s1) + str(s2))
#         pass
#     else:
#         print("输入的数字是：    " + str(a2) + ' ' + str(a3) + ' ' + str(a4))




#
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             for m in range(10):
#                 for n in range(10):
#                     if i > j or i > k or i > m or i > n or j > k or j > m or j > n or k > m or k > n or m > n:
#                         # print(i, j, k, m, n)
#                         pass
#                     else:
#                         print(i, j, k, m, n)

#
# for i in range(100000):
#     d0 = range(0, 100000)
#     d1 = random.choice(d0)
#     d2 = "%05d" % d1
#     print(d2)
#
# for i in range(10):
#     a0 = random.choice(range(1, 50))
#     a1 = random.choice(range(1, 50))
#     a2 = random.choice(range(1, 50))
#     a3 = random.choice(range(1, 50))
#     if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
#         pass
#     else:
#         if a0 <= 10:
#             print('第一列0: ' + str(a0))
#         if 10 < a0 <= 20:
#             print('第一列1: ' + str(a0))
#         if 20 < a0 <= 30:
#             print('第一列2: ' + str(a0))
#         if 30 < a0 <= 40:
#             print('第一列3: ' + str(a0))
#         if 40 < a0 <= 49:
#             print('第一列4: ' + str(a0))
#
#         if a1 <= 10:
#             print('第二列0: ' + str(a1))
#         if 10 < a1 <= 20:
#             print('第二列1: ' + str(a1))
#         if 20 < a1 <= 30:
#             print('第二列2: ' + str(a1))
#         if 30 < a1 <= 40:
#             print('第二列3: ' + str(a1))
#         if 40 < a1 <= 49:
#             print('第二列4: ' + str(a1))
#
#         if a2 <= 10:
#             print('第三列0: ' + str(a2))
#         if 10 < a2 <= 20:
#             print('第三列1: ' + str(a2))
#         if 20 < a2 <= 30:
#             print('第三列2: ' + str(a2))
#         if 30 < a2 <= 40:
#             print('第三列3: ' + str(a2))
#         if 40 < a2 <= 49:
#             print('第三列4: ' + str(a2))
#
#         if a3 <= 10:
#             print('第四列0: ' + str(a3))
#         if 10 < a3 <= 20:
#             print('第四列1: ' + str(a3))
#         if 20 < a3 <= 30:
#             print('第四列2: ' + str(a3))
#         if 30 < a3 <= 40:
#             print('第四列3: ' + str(a3))
#         if 40 < a3 <= 49:
#             print('第四列4: ' + str(a3))
#         print('----------------')
#         print('----------------')
#         print('----------------')


# for i in range(10):
#     a3 = random.choice(range(0, 5))
#     print(a3)
# s = random.sample(range(0, 4), 3)
# s1 = s[0]
# s2 = s[1]
# s3 = s[2]
#
# print(s)
# print(s1)
# print(s2)
# print(s3)

# for i in range(100):
# #     s = random.choice(range(0, 5))
# #     print(s)


# for i  in range(100):
#     s0 = random.choice(range(0, 20))
#     a0 = random.choice(range(0, 5))
#     a1 = random.choice(range(0, 5))
#     a2 = random.choice(range(0, 5))
#     a3 = random.choice(range(0, 5))
#     b0 = random.choice(range(0, 5))
#     c0 = random.choice(range(0, 5))
#     # 数组1000随机抽取
#     d0 = random.choice(range(0, 100))
#     d1 = random.choice(range(999, 10000))
#     d2 = random.choice(range(0, 1000))
#     # 数组不够三位补够三位
#     m = "%03d" % d2
#     # 切片取数组第一个数字
#     m0 = m[0]
#     m1 = m[1]
#     m2 = m[2]
#     #print(' # 五个位置，相同三位数字')
#     if m0 == m1 and m0 == m2 and m1 == m2:
#         print('m0: ' + str(m))
#         print('m0: ' + str(m0))
#         print('m0: ' + str(m1))
#         print('m0: ' + str(m2))

# for i in range(100):
#     s = random.choice(range(111, 667))
#     s0 = "%03d" % s
#     s1 = s0[0]
#     s2 = s0[1]
#     s3 = s0[2]
#     print(s1)
#     print(s2)
#     print(s3)
#
#     x = "%s1%s2%s3" % s
#     print(x)
# b = [1, 2, 3, 4]
# print(b[1])
# for i in range(len(b)):
#     for j in range(len(b)):
#         for k in range(len(b)):
#             if b[i] != b[j] and b[i] != b[k] and b[j] != b[k]:
#                 print(b[i], b[j], b[k])

# b = [16, 17, 18, 19]
# for x in range(11111):
#     b1 = random.choice(range(0, 30))
#     for i in range(len(b)):
#         if b[i] == b1:
#             print(b[i])
# #             print('aaaa')
# for i in range(100):
#     s0 = random.choice(range(0, 667))
#     # s1 = "%3d" % s0
#     s2 = s0[i]
#     print('aaa:   ' + str(2))
#     a = int(re.sub("\D", "", s2))
#
#     if a == 6:
#         print(a)
#     else:
#         print('33333')
"""
    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
    print('从二同号1个号码：  ' + ' ' + str(i) + ' ' + str(s))
    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
"""
# for i in range(100):
#     a0 = random.choice(range(0, 11))
#     print(a0)
# for j in range(10):
#     print(j)
# s0 = random.choice(range(1, 100))
# s1 = [1, 5, 10, 20, s0]
# s2 = random.choice(range(0, 5))
# print(s1[s2])

# # 具体操作时可通过ActionChains中的move_by_offset来实现滑动块的移动，具体代码如下
# # 导入ActionChains模块
# from selenium.webdriver.common.action_chains import ActionChains
#
# browser = webdriver.Firefox()
# # url为目标WEB的链接
# browser.get('https://fusion.spmobileapi.net/dglobby#/play/46')
#
# time.sleep(5)
#
# # 通过ID定位到进度条
# brightnessLine = browser.find_element_by_xpath('x, //*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[2]/div')
# # 通过title属性获取当前的值
# brightnessLine.get_attribute("aria-valuenow")
# # 通过ID定位到滑动块
# brightnessSlider = browser.find_element_by_xpath('x, //*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[2]/div/div[4]"')
#
# ActionChains(browser).click_and_hold(brightnessSlider).move_by_offset(0, 7).release().perform()
# #通过move_by_offset()移动滑块，-6表示在水平方向上往左移动6个像素，7表示在垂直方向上往上移动7个像素


# s1 = [17, 18, 19, 20, 27, 28, 29, 30, 37, 38, 39, 40, 47, 48, 49, 50, 57, 58, 59, 60]
#
# for i in range(10):
#
#     s0 = random.choice(range(11, 67))
#     # 循环抽取s1的元素
#     for j in range(len(s1)):
#         if s0 == s1[j]:
#             print('s0:  ' + str(s1[j]))
#         else:
#             pass
# #
# for i in range(1000):
#
#     s0 = random.choice(range(11, 67))
#     a0 = random.choice(range(1, 6))
#     a1 = random.choice(range(1, 6))
#     if a0 == a1:
#         pass
#     else:
#         print(str(a0) + '' + str(a1))
# for i in range(1000):
#     s0 = random.choice(range(1, 6))
#     a0 = random.choice(range(1, 6))
#     a1 = random.choice(range(1, 6))
#     a2 = random.choice(range(1, 6))
#     if a0 == a1 or a0 == a2 or a1 == a2:
#         ss = str(a1) + str(a1) + str(a2)
#         print(ss)
# def sort_result(self, result_list):
#     # unittest does not seems to run in any particular order.
#     # Here at least we want to group them together by class.
#     rmap = {}
#     classes = []
#     for n, t, o, e, pra in result_list:
#         cls = t.__class__
#         if not cls in rmap:
#             rmap[cls] = []
#             classes.append(cls)
#         rmap[cls].append((n, t, o, e, pra))
#     r = [(cls, rmap[cls]) for cls in classes]
#     return r

'''
# 统计文件多少行方法一
# count = len(open("/fusion/yaml/计划站项目.txt", 'r').readlines())
# print(count)
#
# 统计文件多少行方法一
count = 0
for index, line in enumerate(open("/fusion/fusion_automate_report_20190512_181106.html", 'r', encoding='utf8')):
    count += 1
print(count)
'''
'''
name = ['a1', 'a2', 'a3']
seq =['seq11111', 'seqs22222', 'seq33333']
f = open("/fusion/1.txt", "w+")
f.write("name\tseq\n")
for i in range(0, len(name)):
    f.write(name[i] + "\t" + seq[i] + "\n")
f.close()

'''
'''
# 读取指定几行文件再写入新的文件
# 旧文件路径
file_path = '/fusion/fusion_automate_report_20190512_181106.html'
path = '/fusion/1.txt'
path1 = '/fusion/2.txt'
data = []
# #读取
with open(file_path, encoding='utf-8', ) as txtfile:
    line = txtfile.readlines()
    for i, rows in enumerate(line):
        if i in range(311, len(line)):  # 指定数据哪几行
            print(rows)
            data.append(rows)
print("length", len(data))
txtfile.close()
# #写入
with open(path, "w", ) as f:
    for i in range(len(data)):
        f.writelines(data[i])
f.close()

count = 0
for index, line in enumerate(open("/fusion/1.txt", 'r')):
    count += 1
print('count行数：' + str(count))



f = open('/fusion/1.txt')
lines = f.readlines()
f.close()
# 从第二行开始
l_list = lines[1:]
for l in l_list:

    if l.find(' ') == -1:
        with open(path1, "w", ) as f:
            for i in range(len(data)):
                f.writelines(data[i])
        f.close()
    else:
        # 如果找到，则跳出循环
        break
'''
#
# # #读取
# with open(file_path, encoding='utf-8', ) as txtfile:
#     line = txtfile.readlines()
#     for i, rows in enumerate(line):
#         if i in range(0, len(line)):  # 指定数据哪几行
#             print(rows)
#             data.append(rows)
# print("length", len(data))
# txtfile.close()
# # #写入
# with open(path1, "w", ) as f:
#     for i in range(len(data)):
#         f.writelines(data[i])
# f.close()
#
# count = 0
# for index, line in enumerate(open("/fusion/2.txt", 'r')):
#     count += 1
# print('count行数：' + str(count))


a = 4
b = 4
c = 2
d = 4

for i in range(10):
    # if (a > 6 or b > 1) and (c > 1 or d > 1):
    #     print('正确1')
    # else:
    #     print('错误1')
    if (a > 1 and b > 1) and (c > 1 and d > 1):
        print('正确2')
    else:
        print('错误2')


