import contextlib
import csv
import logging
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum, unique
from unittest import TestCase as TC, SkipTest
from unittest.case import _ShouldStop
from unittest.suite import _DebugResult, _isnotsuite

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BoxDriver(object):
    """
    a simple demo of selenium framework tool
    """

    """
    私有全局变量
    """
    _base_driver = None
    _by_char = None

    """
    构造方法
    """
    
    

    def __init__(self, browser_type=0, download_path="c:\\Users\\tester\\Downloads", by_char=",", profile=None):
        """
        构造方法：实例化 BoxDriver 时候使用
        :param browser_type: 浏览器类型
        :param by_char: 分隔符，默认使用","
        :param profile:
            可选择的参数，如果不传递，就是None
            如果传递一个 profile，就会按照预先的设定启动火狐
            去掉遮挡元素的提示框等
        """
        self._by_char = by_char
        if browser_type == 0 or browser_type == Browser.Chrome:

            profile = webdriver.ChromeOptions()
            # profile.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

            # download.default_directory：设置下载路径
            # profile.default_content_settings.popups：设置为 0 禁止弹出窗口
            prefs = {'profile.default_content_settings.popups': 0,
                     'download.default_directory': download_path}
            profile.add_experimental_option('prefs', prefs)

            driver = webdriver.Chrome(chrome_options=profile)
            # driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe', chrome_options=options)


        elif browser_type == 1 or browser_type == Browser.Firefox:
            # if profile is not None:
                # profile = FirefoxProfile(profile)

            profile = webdriver.FirefoxProfile()
            # 指定下载路径
            profile.set_preference('browser.download.dir', download_path)
            # 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
            profile.set_preference('browser.download.folderList', 2)
            # 在开始下载时是否显示下载管理器
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            # 对所给出文件类型不再弹出框进行询问
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

            driver = webdriver.Firefox(firefox_profile=profile)

        elif browser_type == Browser.Ie:
            driver = webdriver.Ie()
        elif browser_type == 'APP':
            desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '4.4.2',
                # apk 包名
                'appPackage': 'com.youkastation.app',
                # apk 的 launcherActivity
                'appActivity':
                    'com.youkastation.app.youkas.activity.AnimWelActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True
            }
            driver = webdriver_app.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            driver = webdriver.PhantomJS()
        try:
            self._base_driver = driver
            self._by_char = by_char
        except Exception:
            raise NameError("Browser %s Not Found! " % browser_type)

    """
    私有方法
    """

    def _convert_selector_to_locator(self, selector):
        """
        转换自定义的 selector 为 Selenium 支持的 locator
        :param selector: 定位字符，字符串类型，"i ,  xxx "   ,不能"i","xxx"
        "su"
        :return: locator
        """
        if self._by_char not in selector:
            return By.ID, selector

        selector_by = selector.split(self._by_char)[0].strip()
        selector_value = selector.split(self._by_char)[1].strip()
        if selector_by == "i" or selector_by == 'id':
            locator = (By.ID, selector_value)
        elif selector_by == "n" or selector_by == 'name':
            locator = (By.NAME, selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            locator = (By.TAG_NAME, selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise NameError("Please enter a valid selector of targeting elements.")

        return locator

    def _locate_element(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            element = self._base_driver.find_element(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return element

    def _locate_elements(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            elements = self._base_driver.find_elements(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return elements

    """
    cookie 相关方法
    """

    def clear_cookies(self):
        """
        clear all cookies after driver init
        """
        self._base_driver.delete_all_cookies()

    def add_cookies(self, cookies):
        """
        Add cookie by dict
        :param cookies:
        :return:
        """
        self._base_driver.add_cookie(cookie_dict=cookies)

    def add_cookie(self, cookie_dict):
        """
        Add single cookie by dict
        添加 单个 cookie
        如果该 cookie 已经存在，就先删除后，再添加
        :param cookie_dict: 字典类型，有两个key：name 和 value
        :return:
        """
        cookie_name = cookie_dict["name"]
        cookie_value = self._base_driver.get_cookie(cookie_name)
        if cookie_value is not None:
            self._base_driver.delete_cookie(cookie_name)

        self._base_driver.add_cookie(cookie_dict)

    def remove_cookie(self, name):
        """
        移除指定 name 的cookie
        :param name: 
        :return: 
        """
        # 检查 cookie 是否存在，存在就移除
        old_cookie_value = self._base_driver.get_cookie(name)
        if old_cookie_value is not None:
            self._base_driver.delete_cookie(name)

    """
    浏览器本身相关方法
    """

    def refresh(self, url=None):
        """
        刷新页面
        如果 url 是空值，就刷新当前页面，否则就刷新指定页面
        :param url: 默认值是空的
        :return:
        """
        if url is None:
            self._base_driver.refresh()
        else:
            self._base_driver.get(url)

    def maximize_window(self):
        """
        最大化当前浏览器的窗口
        :return:
        """
        self._base_driver.maximize_window()


    def navigate(self, url):
        """
        打开 URL
        :param url:
        :return:
        """
        self._base_driver.get(url)

    def quit(self):
        """
        退出驱动
        :return:
        """
        self._base_driver.quit()

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self._base_driver.close()

    def back(self):
        """
        后退浏览器
        :return:
        """
        self._base_driver.back()

    def forward(self):
        """
        后退浏览器
        :return:
        """
        self._base_driver.forward()



    """
    基本元素相关方法
    """

    def type(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self._locate_element(selector)
        el.clear()
        el.send_keys(text)

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        el = self._locate_element(selector)
        el.click()

    def click_last_one(self, selector):
        # 点击倒数第一个
        eles = self._locate_elements(selector)
        eles[-1].click()

    def click_first(self, selector):
        # 点击数组第一个，通常是默认
        eles = self._locate_elements(selector)
        eles[0].click()

    def click_second(self, selector):
        # 点击数组第二个，
        eles = self._locate_elements(selector)
        eles[1].click()

    def click_by_enter(self, selector):
        """
        It can type any text / image can be located  with ENTER key

        Usage:
        driver.click_by_enter("i,el")
        """
        el = self._locate_element(selector)
        el.send_keys(Keys.ENTER)

    def click_by_text(self, text):
        """
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        """
        self._locate_element('p%s' % self._by_char + text).click()

    def submit(self, selector):
        """
        Submit the specified form.

        Usage:
        driver.submit("i,el")
        """
        el = self._locate_element(selector)
        el.submit()

    def move_to(self, selector):
        """
        to move mouse pointer to selector
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        ActionChains(self._base_driver).move_to_element(el).perform()

    def right_click(self, selector):
        """
        to click the selector by the right button of mouse
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        ActionChains(self._base_driver).context_click(el).perform()

    def count_elements(self, selector):
        """
        数一下元素的个数
        :param selector: 定位符
        :return:
        """
        els = self._locate_elements(selector)
        return len(els)

    def drag_element(self, source, target):
        """
        拖拽元素
        :param source:
        :param target:
        :return:
        """

        el_source = self._locate_element(source)
        el_target = self._locate_element(target)

        if self._base_driver.w3c:
            ActionChains(self._base_driver).drag_and_drop(el_source, el_target).perform()
        else:
            ActionChains(self._base_driver).click_and_hold(el_source).perform()
            ActionChains(self._base_driver).move_to_element(el_target).perform()
            ActionChains(self._base_driver).release(el_target).perform()

    def lost_focus(self):
        """
        当前元素丢失焦点
        :return:
        """
        ActionChains(self._base_driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()

    """
    <select> 元素相关
    """

    def select_by_index(self, selector, index):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_index(index)

    def get_selected_text(self, selector):
        """
        获取 Select 元素的选择的内容
        :param selector: 选择字符 "i, xxx"
        :return: 字符串
        """
        el = self._locate_element(selector)
        selected_opt = Select(el).first_selected_option()
        return selected_opt.text

    def select_by_visible_text(self, selector, text):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_visible_text(text)

    def select_by_value(self, selector, value):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_value(value)

    """
    JavaScript 相关
    """

    def execute_js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self._base_driver.execute_script(script)

    """
    元素属性相关方法
    """

    def get_value(self, selector):
        """
        返回元素的 value
        :param selector: 定位字符串
        :return:
        """
        el = self._locate_element(selector)
        return el.get_attribute("value")

    def get_attribute(self, selector, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self._locate_element(selector)
        return el.get_attribute(attribute)

    def get_text(self, selector):
        """
        Get element text information.

        Usage:
        driver.get_text("i,el")
        """
        el = self._locate_element(selector)
        return el.text

    def get_displayed(self, selector):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("i,el")
        """
        el = self._locate_element(selector)
        return el.is_displayed()

    def get_exist(self, selector):
        '''
        该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
        :param self:
        :param selector: 元素定位，如'id,account'
        :return: 布尔值
        '''
        flag = True
        try:
            self._locate_element(selector)
            return flag
        except:
            flag = False
            return flag

    def get_enabled(self,selector):
        '''
        判断页面元素是否可点击
        :param selector: 元素定位
        :return: 布尔值
        '''
        if self._locate_element(selector).is_enabled():
            return True
        else:
            return False

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self._base_driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self._base_driver.current_url

    def get_selected(self, selector):
        """
        to return the selected status of an WebElement
        :param selector: selector to locate
        :return: True False
        """
        el = self._locate_element(selector)
        return el.is_selected()

    def get_text_list(self, selector):
        """
        根据selector 获取多个元素，取得元素的text 列表
        :param selector:
        :return: list
        """

        el_list = self._locate_elements(selector)

        results = []
        for el in el_list:
            results.append(el.text)

        return results

    """
    窗口相关方法
    """

    def accept_alert(self):
        '''
            Accept warning box.

            Usage:
            driver.accept_alert()
            '''
        self._base_driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        '''
        self._base_driver.switch_to.alert.dismiss()

    def switch_to_parent_frame(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self._base_driver.switch_to.parent_frame()

    def switch_to_frame(self, selector):
            """
            Switch to the specified frame.

            Usage:
            driver.switch_to_frame("i,el")
            """
            el = self._locate_element(selector)
            self._base_driver.switch_to.frame(el)



    def switch_to_default(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self._base_driver.switch_to.default_content()

    def switch_to_window_by_title(self, title):
        for handle in self._base_driver.window_handles:
            self._base_driver.switch_to.window(handle)
            if self._base_driver.title == title:
                break

            self._base_driver.switch_to.default_content()

    def open_new_window(self, selector):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self._base_driver.current_window_handle
        el = self._locate_element(selector)
        el.click()
        all_handles = self._base_driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self._base_driver._switch_to.window(handle)

    def switch_to_window_by_index(self, index):
        '''
        切换到新窗口
        :param index:需要切换到第几个窗口，从左往右数，数到第几个就是几
        :return:
        '''
        all_handles = self._base_driver.window_handles
        num = index - 1
        print('frame')
        handle = all_handles[num]
        self._base_driver.switch_to.window(handle)

    def save_window_snapshot(self, file_name):
        """
        save screen snapshot
        :param file_name: the image file name and path
        :return:
        """
        driver = self._base_driver
        driver.save_screenshot(file_name)

    def save_window_snapshot_by_io(self):
        """
        保存截图为文件流
        :return:
        """
        return self._base_driver.get_screenshot_as_base64()

    def save_element_snapshot_by_io(self, selector):
        """
        控件截图
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        return el.screenshot_as_base64

    """
    等待方法
    """

    def forced_wait(self, seconds):
        """
        强制等待
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    def implicitly_wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        :param seconds 等待时间 秒
        隐式等待

        Usage:
        driver.implicitly_wait(10)
        """
        self._base_driver.implicitly_wait(seconds)

    def explicitly_wait(self, selector, seconds):
        """
        显式等待
        :param selector: 定位字符
        :param seconds: 最长等待时间，秒
        :return:
        """
        locator = self._convert_selector_to_locator(selector)

        WebDriverWait(self._base_driver, seconds).until(expected_conditions.presence_of_element_located(locator))

    """上传"""
    def upload_input(self,selector,file):
        '''
        上传文件 （ 标签为 input 类型，此类型最常见，最简单）
        :param selector: 上传按钮定位
        :param file: 将要上传的文件（绝对路径）
        :return: 无
        '''
        self._locate_element(selector).send_keys(file)

    def upload_not_input(self,file,browser_type='Chrome'):
        '''
        上传文件 （ 标签不是 input 类型，使用 win32gui,得先安装 pywin32 依赖包）
                                                pip install pywin32
        :param browser_type: 浏览器类型（Chrome浏览器和Firefox浏览器的有区别）
        :param file: 将要上传的文件（绝对路径）
        单个文件：file1 = 'C:\\Users\\list_tuple_dict_test.py'
        同时上传多个文件：file2 = '"C:\\Users\\list_tuple_dict_test.py" "C:\\Users\\class_def.py"'
        :return: 无
        '''
        # Chrome 浏览器是'打开'
        # 对话框
        # 下载个 Spy++ 工具，定位“打开”窗口，定位到窗口的类(L):#32770, '打开'为窗口标题
        dialog = None
        if browser_type == 'Chrome':
            dialog = win32gui.FindWindow('#32770', u'打开')
        elif browser_type == 'Firefox':
            # Firefox 浏览器是'文件上传'
            # 对话框
            dialog = win32gui.FindWindow('#32770', u'文件上传')
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        # 确定按钮Button
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        # 往输入框输入绝对地址
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)
        # 按button
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        # 获取属性
        # print(upload.get_attribute('value'))


    """
    表单数据提交:
        页面校验
        数据库校验
        某条记录选择，编辑，删除
    """
    def del_edit_choose_the_row(self, selector_of_next_page, selector_of_trs_td, selector_of_del_edit_choose,expected_td_value):
        """
        页面表单，选中/编辑/删除 指定内容的行（带多页翻页功能）
        :param selector_of_next_page: ‘下一页’定位，如：'l,下页'
        :param selector_of_trs_td: 所有行的某一列的定位，如 ranzhi 成员列表中，获取所有行的“真实姓名”那列：'x,/html/body/div/div/div/div[2]/div/div/table/tbody//tr/td[2]'
        :param selector_of_del_edit_choose: 指定要操作(删除/编辑/选择)的列，如 ranzhi 成员列表中,获取期望删除的列：'x,/html/body/div/div/div/div[2]/div/div/table/tbody/tr[%d]/td[11]/a[3]'
        :param expected_td_value: 期望的列内容，如ranzhi 成员列表中期望的“真实姓名”: '华仔'
        :return:无
        """

        td_values = self.get_text_list(selector_of_trs_td)
        for i in range(len(td_values)):
            if td_values[i] == expected_td_value:
                print('%s在第%d行显示(首页)！' % (td_values[i], i + 1))
                self.forced_wait(2)
                self.click(selector_of_del_edit_choose % (i + 1))
                break
        try:
            while (self.get_enabled(selector_of_next_page)):
                self.click(selector_of_next_page)
                self.forced_wait(2)
                td_values = self.get_text_list(selector_of_trs_td)
                for i in range(len(td_values)):
                    if td_values[i] == expected_td_value:
                        print('%s在第%d行显示(非首页)' % (td_values[i], i + 1))
                        self.forced_wait(3)
                        self.click(selector_of_del_edit_choose % (i + 1))
                continue
        except Exception as e:
            print('%s 操作成功！' % expected_td_value)

    def assert_new_record_exist_in_table(self, selector_of_next_page, selector_of_trs_td, expected_td_value):
        '''
        此方法针对页面列表（带多页翻页功能），都可以判断新增记录是否添加成功！
        若新增成功，则返回 True 布尔值；否则返回 False 布尔值
        :param selector_of_next_page: "下一页"定位，如：
        :param selector_of_trs_td:所有行的某一列的定位，如： 'l,下页''x,/html/body/div/div[2]/div/div[1]/div/table/tbody//tr/td[2]'
        :param expected_td_value:期望的列内容,如：'华仔'
        :return: 布尔值
        '''
        # first_count_per_page = self.count_elements(selector_of_real_record)
        # print('当前设置为每页显示 %s 条记录' % first_count_per_page)
        real_records = self.get_text_list(selector_of_trs_td)
        for real_record in real_records:
            if real_record == expected_td_value:
                return True
        # count_per_page_whiles = 0
        try:

            while (self.get_enabled(selector_of_next_page)):
                self.click(selector_of_next_page)
                self.forced_wait(2)
                # count_per_page_while = driver.count_elements("x,//tbody//tr/td[2]")
                # count_per_page_whiles += count_per_page_while
                next_page_real_records = self.get_text_list(selector_of_trs_td)
                for next_page_real_record in next_page_real_records:
                    if next_page_real_record == expected_td_value:
                        # self.log.info('记录新增成功！新增记录 %s 不是在第一页被找到！'%expect_new_record)
                        return True
                continue
        except Exception as e:
            # count_page_real_show = count_per_page_whiles + first_count_per_page
            # print("页面实际显示记录条数：%s" % count_page_real_show)
            # 页面统计总数 VS 页面实际显示记录总数
            # assert count_page_real_show == int(total_num)
            # print("‘页面实际显示记录总数’ 与 ‘页面统计显示记录总数’ 相同！")

            # raise NameError("页面表单中无此数据，原因：(1)请查询待验证的数据是否输入正确？(2)或者'下页'翻页定位是否正确？")
            print("页面表单中无此数据，原因：(1)请查询待验证的数据是否输入正确？(2)或者'下页'翻页定位是否正确？")
            return False

    def assert_new_record_exist_mysql(self, db_yaml_path, db_yaml_name,sql_file_path, select_field_num,expected_td_value):
        '''
        数据库校验，True为数据库中存在该数据
        :param db_yaml_path: 数据库的yaml格式的配置文件路径
        :param db_yaml_name: 数据库的yaml格式的配置文件中设置的数据库名（默认是在'DbConfig'下面）
        :param sql_file_path: sql文件路径
        :param select_field_num: 查询语句中第几个字段（默认0表示第1个字段）
        :param expected_td_value: 期望要断言的值
        :return: True / False
        '''
        ydata = YamlHelper().get_config_dict(db_yaml_path)
        host = ydata['DbConfig'][db_yaml_name]['host']
        port = ydata['DbConfig'][db_yaml_name]['port']
        user = ydata['DbConfig'][db_yaml_name]['user']
        pwd = ydata['DbConfig'][db_yaml_name]['pwd']
        db = ydata['DbConfig'][db_yaml_name]['db']

        db_helper = DbHelper(host, port, user, pwd, db)
        sql = db_helper.read_sql(sql_file_path)
        result = db_helper.execute(sql)['data']
        db_helper.close()
        try:
            for i in result:
                if i[select_field_num] == expected_td_value:
                    return True
        except Exception:
            return False

class BasePage(object):
    """
    测试系统的最基础的页面类，是所有其他页面的基类
    """
    # 变量
    base_driver = None

    # 方法
    def __init__(self, driver: BoxDriver, logger=None):
        """
        构造方法
        :param driver: 指定了参数类型，BoxDriver
        """
        self.base_driver = driver

        self.logger = logger

    def open(self, url):
        """
        打开页面
        :param url:
        :return:
        """
        self.base_driver.navigate(url)
        self.base_driver.maximize_window()
        self.base_driver.forced_wait(2)

    def log(self, msg):
        """
        记录日志
        :param msg:
        :return:
        """
        if self.logger is not None:
            self.logger.info(msg)

class CsvHelper(object):

    def read_data(self, f,encoding="utf-8-sig"):
        """
        读csv文件作为普通list
        :param f:
        :return:
        """
        data_ret = []
        with open(f, encoding=encoding, mode='r') as csv_file:
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                data_ret.append(row)

        return data_ret

    def read_data_as_dict(self, f, encoding="utf-8-sig"):
        """
        读csv文件作为普通list
        :param f:
        :return:
        """
        data_ret = []
        with open(f, encoding=encoding, mode='r') as csv_file:
            csv_dict = csv.DictReader(csv_file)
            for row in csv_dict:
                data_ret.append(row)

        return data_ret

class DbHelper(object):
    """
    MySQ 数据库帮助类
    """

    # 使用方法
    # 1. 实例化对象
    # 2. 查询，得到结果
    # 3. 关闭对象
    """
    db_helper = MysqlDbHelper("localhost", 3306, 'root', '', 'tpshop2.0.5', "utf8")
    for i in range(10000):

        result = db_helper.execute("select * from tp_goods order by 1 desc limit 1000;")
        print("第%d次，结果是%r" % (i, result))

    db_helper.close()
    """

    connect = None

    def __init__(self, host, port, user, password, database, charset='utf8'):
        """
        构造方法
        :param host: 数据库的主机地址
        :param port: 数据库的端口号
        :param user: 用户名
        :param password: 密码
        :param database: 选择的数据库
        :param charset: 字符集
        """
        self.connect = pymysql.connect(host=host, port=port,
                                       user=user, password=password,
                                       db=database, charset=charset)

    def read_sql(self, file, encoding="utf8"):
        """
        从 文件中读取 SQL 脚本
        :param file: 文件名 + 文件路径
        :return:
        """
        sql_file = open(file, "r", encoding=encoding)
        sql = sql_file.read()
        sql_file.close()
        return sql

    def execute(self, sql):
        """
        执行 SQL 脚本查询并返回结果
        :param sql: 需要查询的 SQL 语句
        :return: 字典类型
            data 是数据，本身也是个字典类型
            count 是行数
        """
        cursor = self.connect.cursor()

        row_count = cursor.execute(sql)
        rows_data = cursor.fetchall()
        result = {
            "count": row_count,
            "data": rows_data
        }

        cursor.close()
        return result

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.connect.close()

class YamlHelper(object):

    def get_config_dict(self, f):
        """
        获取所有配置
        :param f:
        :return:
        """
        with open(f, mode='r', encoding='utf8') as file_config:
            config_dict = yaml.load(file_config.read())
            return config_dict

class Email(object):

    def email_attachment(self,report_file):
        '''配置发送附件测试报告到邮箱'''
        '''发件相关参数'''
        try:
            # 发件服务器
            smtpserver = 'smtp.163.com'
            port = 25

            '''
            更改如下3项即可：
                1、 sender：发件人的邮箱，为163邮箱；
                2、 pwd：发送邮箱的密码
                    注意：此密码不是登录密码，而是网络授权码
                3、 receiver: 收件人的邮箱
            '''

            sender = 'w18617013450@163.com'
            psw = 'w123456'
            receiver = '13807083044@163.com'

            msg = MIMEMultipart()
            msg['from'] = sender
            msg['to'] = ';'.join(receiver)
            msg['subject'] = '这个是ranzhi项目自动化测试报告主题'
            '''读取测试报告内容'''
            with open(report_file, 'rb') as rp:
                ranzhi_mail_body = rp.read()
            '''正文'''
            body = MIMEText(ranzhi_mail_body, 'html', 'utf8')
            msg.attach(body)
            '''附件'''
            att = MIMEText(ranzhi_mail_body, 'base64', 'utf8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment;filename = "%s"' % report_file
            msg.attach(att)
            '''发送邮件'''
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver, port)
            smtp.login(sender, psw)
            smtp.sendmail(sender, receiver.split(';'), msg.as_string())  # 发送
            smtp.close()
            print("邮件发送成功!")
        except Exception as e:
            print(e)
            print("邮件发送失败!")

@unique
class Browser(Enum):
    """
    定义支持的浏览器，支持Chrome，Firefox，Ie
    """
    Chrome = 0
    Firefox = 1
    Ie = 2

class TestLogger:
    def __init__(self, log_path):
        # log_path：日志存放路径
        # 文件命名

        self.file_name = log_path
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]: %(message)s')

    def info(self, message):
        """
        添加信息日志
        :param message:
        :return:
        """
        self._console("info", message)

    def warning(self, message):
        """
        添加警告日志
        :param message:
        :return:
        """
        self._console("warning", message)

    def error(self, message):
        """
        添加错误日志
        :param message:
        :return:
        """
        self._console("error", message)

    def _console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.file_name, 'a', encoding='utf8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个SteamHandler,用于输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)

        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码为了避免日志输出重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

# TODO：参数化
'''
参数化 :
    paramunittest
    ddt
'''


class TestCase(TC):
    """
    测试用例类

    """
    images = None
    base_driver = None
    logger = None

    def __init__(self, methodName='runTest', logger_file=None):
        """
        重写构造方法
        """
        super().__init__(methodName)
        if self.images is None:
            self.images = []
        if logger_file is not None:
            self.logger = TestLogger(logger_file)
        else:
            test_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            self.logger = TestLogger("test_log_%s.log" % test_time)

    def set_up(self):
        """
        ddd
        :return:
        """
        pass

    def tear_down(self):
        """
        dddd
        :return:
        """
        pass

    def run(self, result=None):
        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
                getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, self, skip_why)
            finally:
                result.stopTest(self)
            return
        expecting_failure_method = getattr(testMethod,
                                           "__unittest_expecting_failure__", False)
        expecting_failure_class = getattr(self,
                                          "__unittest_expecting_failure__", False)
        expecting_failure = expecting_failure_class or expecting_failure_method
        outcome = _Outcome(result)
        try:

            self._outcome = outcome

            with outcome.testPartExecutor(self):
                self.set_up()
            if outcome.success:
                outcome.expecting_failure = expecting_failure
                with outcome.testPartExecutor(self, isTest=True):
                    testMethod()
                outcome.expecting_failure = False

                # 尝试异常继续运行
                with outcome.testPartExecutor(self):
                    self.tear_down()

            for test, reason in outcome.skipped:
                self._addSkip(result, test, reason)
            self._feedErrorsToResult(result, outcome.errors)
            if outcome.success:
                if expecting_failure:
                    if outcome.expectedFailure:
                        self.snapshot()
                        self._addExpectedFailure(result, outcome.expectedFailure)
                    else:
                        self._addUnexpectedSuccess(result)
                else:
                    result.addSuccess(self)

            self.doCleanups()
            return result
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()

            # explicitly break reference cycles:
            # outcome.errors -> frame -> outcome -> outcome.errors
            # outcome.expectedFailure -> frame -> outcome -> outcome.expectedFailure
            outcome.errors.clear()
            outcome.expectedFailure = None

            # clear the outcome, no more needed
            self._outcome = None

    def snapshot(self):
        """
        截图
        :return:
        """
        self.images.append(self.base_driver.save_window_snapshot_by_io())

    def log(self, msg):
        """
        添加日志
        :param msg:
        :return:
        """
        if self.logger is not None:
            self.logger.info(msg)

    def read_csv_as_dict(self, file_name):
        """
        读 CSV 作为 DICT 类型
        :type file_name: csv 文件路径 和名字
        :return:
        """
        return CsvHelper().read_data_as_dict(file_name)

    def shortDescription(self):
        """Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        """
        doc = self._testMethodDoc
        return doc and doc.split("\n")[0].strip() or None
        # 用[1]报错，数组超出界限，报告是空的，改为[0]就可以了
        # return doc and doc.split("\n")[0].strip() or None

class _Outcome(object):
    def __init__(self, result=None):
        self.expecting_failure = False
        self.result = result
        self.result_supports_subtests = hasattr(result, "addSubTest")
        self.success = True
        self.skipped = []
        self.expectedFailure = None
        self.errors = []

    @contextlib.contextmanager
    def testPartExecutor(self, test_case, isTest=False):
        old_success = self.success
        self.success = True
        try:
            yield
        except KeyboardInterrupt:
            raise
        except SkipTest as e:
            self.success = False
            self.skipped.append((test_case, str(e)))
        except _ShouldStop:
            pass
        except:
            exc_info = sys.exc_info()
            if self.expecting_failure:
                self.expectedFailure = exc_info
            else:
                self.success = False
                # test_case.images.append(test_case.base_driver.save_window_snapshot_by_io())

                self.errors.append((test_case, exc_info))
            # explicitly break a reference cycle:
            # exc_info -> frame -> exc_info
            exc_info = None
        else:
            if self.result_supports_subtests and self.success:
                self.errors.append((test_case, None))
        finally:
            self.success = self.success and old_success

"""
A TestRunner for use with the Python unit testing framework. It generates a HTML report to show the result at a glance.

The simplest way to use this is to invoke its main method. E.g.

    import unittest
    import HtmlTestRunner

    ... define your tests ...

    if __name__ == '__main__':
        HtmlTestRunner.main()


For more customization options, instantiates a HtmlTestRunner object.
HtmlTestRunner is a counterpart to unittest's TextTestRunner. E.g.

    # output to a file
    fp = file('my_report.html', 'wb')
    runner = HtmlTestRunner.HtmlTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HtmlTestRunner.'
                )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test
    runner.run(my_test_suite)


------------------------------------------------------------------------
Copyright (c) 2004-2007, Wai Yip Tung
Copyright (c) 2016, Eason Han
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name Wai Yip Tung nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

__author__ = "Wai Yip Tung && Eason Han"
__version__ = "0.8.4"

import datetime
import io
import sys
import unittest
from xml.sax import saxutils


def to_unicode(s):
    try:
        return s
    except UnicodeDecodeError:
        # s is non ascii byte string
        return s.decode('unicode_escape')

class OutputRedirect(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(to_unicode(s))

    def writelines(self, lines):
        lines = map(to_unicode, lines)
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()

stdout_redirect = OutputRedirect(sys.stdout)
stderr_redirect = OutputRedirect(sys.stderr)

# ----------------------------------------------------------------------
# Template

class _TemplateReport(object):
    """
    Define a HTML template for report customerization and generation.

    Overall structure of an HTML report

    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: 'pass',
        1: 'fail',
        2: 'error',
    }

    DEFAULT_TITLE = 'Unit Test Report'
    DEFAULT_DESCRIPTION = ''

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<!DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css">
    %(stylesheet)s

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="http://cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="http://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

function show_img(obj) {
    var obj1 = obj.nextElementSibling
    obj1.style.display='block'
    var index = 0;//每张图片的下标，
    var len = obj1.getElementsByTagName('img').length;
    var imgyuan = obj1.getElementsByClassName('imgyuan')[0]
    //var start=setInterval(autoPlay,500);
    obj1.onmouseover=function(){//当鼠标光标停在图片上，则停止轮播
        clearInterval(start);
    }
    obj1.onmouseout=function(){//当鼠标光标停在图片上，则开始轮播
        start=setInterval(autoPlay,1000);
    }    
    for (var i = 0; i < len; i++) {
        var font = document.createElement('font')
        imgyuan.appendChild(font)
    }
    var lis = obj1.getElementsByTagName('font');//得到所有圆圈
    changeImg(0)
    var funny = function (i) {
        lis[i].onmouseover = function () {
            index=i
            changeImg(i)
        }
    }
    for (var i = 0; i < lis.length; i++) {
        funny(i);
    }

    function autoPlay(){
        if(index>len-1){
            index=0;
            clearInterval(start); //运行一轮后停止
        }
        changeImg(index++);
    }
    imgyuan.style.width= 25*len +"px";
    //对应圆圈和图片同步
    function changeImg(index) {
        var list = obj1.getElementsByTagName('img');
        var list1 = obj1.getElementsByTagName('font');
        for (i = 0; i < list.length; i++) {
            list[i].style.display = 'none';
            list1[i].style.backgroundColor = 'white';
        }
        list[index].style.display = 'block';
        list1[index].style.backgroundColor = 'blue';
    }

}
function hide_img(obj){
    obj.parentElement.style.display = "none";
    obj.parentElement.getElementsByClassName('imgyuan')[0].innerHTML = "";
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

<div class="container">
    %(heading)s
    %(report)s
    %(ending)s
</div>

</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending)

    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">

.img{
	height: 100%;
	border-collapse: collapse;
    border: 2px solid #777;
}

.screenshots {
    z-index: 100;
	position:absolute;
	height: 80%;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
	display: none;
}

.imgyuan{
    height: 20px;
    border-radius: 12px;
    background-color: red;
    padding-left: 13px;
    margin: 0 auto;
    position: relative;
    top: -40px;
    background-color: rgba(1, 150, 0, 0.3);
}
.imgyuan font{
    border:1px solid white;
    width:11px; 
    height:11px;
    border-radius:50%;
    margin-right: 9px;
    margin-top: 4px;
    display: block;
    float: left;
    background-color: white;
}
.close_shots {
    background-image: url(data:image/png;base64,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/GMzLdsAAD+3aVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzA2NyA3OS4xNTc3NDcsIDIwMTUvMDMvMzAtMjM6NDA6NDIgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgICAgICAgICB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIgogICAgICAgICAgICB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIKICAgICAgICAgICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICAgICAgICAgICB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPHhtcE1NOkRvY3VtZW50SUQ+YWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjk4NDVkYzlhLTM2NTEtMTFlOC1hMDRjLWMzZmRjNzFmNjFkZDwveG1wTU06RG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDo3YzQ4OTMyZS0wM2FjLTIxNDctYTJiZi1iNmViOWU4ZDY2Y2Q8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+MEIzOTNDRjk1RDQ0RDlGMDNFQjEzQkZEQ0UxRDA5MjM8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOmQ0ZjMzNDFjLTRkYjctZjc0YS1iZTAxLWYxMGEwMzNhNjg4ZDwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAxOC0wNC0wMlQxNjo0MToxMCswODowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE0LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDphY3Rpb24+Y29udmVydGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpwYXJhbWV0ZXJzPmZyb20gaW1hZ2UvanBlZyB0byBpbWFnZS9wbmc8L3N0RXZ0OnBhcmFtZXRlcnM+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5kZXJpdmVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpwYXJhbWV0ZXJzPmNvbnZlcnRlZCBmcm9tIGltYWdlL2pwZWcgdG8gaW1hZ2UvcG5nPC9zdEV2dDpwYXJhbWV0ZXJzPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDphY3Rpb24+c2F2ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0Omluc3RhbmNlSUQ+eG1wLmlpZDo3YzQ4OTMyZS0wM2FjLTIxNDctYTJiZi1iNmViOWU4ZDY2Y2Q8L3N0RXZ0Omluc3RhbmNlSUQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDp3aGVuPjIwMTgtMDQtMDJUMTY6NDE6MTArMDg6MDA8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNC4wIChXaW5kb3dzKTwvc3RFdnQ6c29mdHdhcmVBZ2VudD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmNoYW5nZWQ+Lzwvc3RFdnQ6Y2hhbmdlZD4KICAgICAgICAgICAgICAgPC9yZGY6bGk+CiAgICAgICAgICAgIDwvcmRmOlNlcT4KICAgICAgICAgPC94bXBNTTpIaXN0b3J5PgogICAgICAgICA8eG1wTU06RGVyaXZlZEZyb20gcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICA8c3RSZWY6aW5zdGFuY2VJRD54bXAuaWlkOmQ0ZjMzNDFjLTRkYjctZjc0YS1iZTAxLWYxMGEwMzNhNjg4ZDwvc3RSZWY6aW5zdGFuY2VJRD4KICAgICAgICAgICAgPHN0UmVmOmRvY3VtZW50SUQ+MEIzOTNDRjk1RDQ0RDlGMDNFQjEzQkZEQ0UxRDA5MjM8L3N0UmVmOmRvY3VtZW50SUQ+CiAgICAgICAgICAgIDxzdFJlZjpvcmlnaW5hbERvY3VtZW50SUQ+MEIzOTNDRjk1RDQ0RDlGMDNFQjEzQkZEQ0UxRDA5MjM8L3N0UmVmOm9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPC94bXBNTTpEZXJpdmVkRnJvbT4KICAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9wbmc8L2RjOmZvcm1hdD4KICAgICAgICAgPHBob3Rvc2hvcDpDb2xvck1vZGU+MzwvcGhvdG9zaG9wOkNvbG9yTW9kZT4KICAgICAgICAgPHBob3Rvc2hvcDpJQ0NQcm9maWxlPnNSR0IgSUVDNjE5NjYtMi4xPC9waG90b3Nob3A6SUNDUHJvZmlsZT4KICAgICAgICAgPHhtcDpDcmVhdGVEYXRlPjIwMTgtMDQtMDJUMTY6MjM6NTUrMDg6MDA8L3htcDpDcmVhdGVEYXRlPgogICAgICAgICA8eG1wOk1vZGlmeURhdGU+MjAxOC0wNC0wMlQxNjo0MToxMCswODowMDwveG1wOk1vZGlmeURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMTgtMDQtMDJUMTY6NDE6MTArMDg6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6Q3JlYXRvclRvb2w+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE0LjAgKFdpbmRvd3MpPC94bXA6Q3JlYXRvclRvb2w+CiAgICAgICAgIDx0aWZmOkltYWdlV2lkdGg+MjU0PC90aWZmOkltYWdlV2lkdGg+CiAgICAgICAgIDx0aWZmOkltYWdlTGVuZ3RoPjI1NDwvdGlmZjpJbWFnZUxlbmd0aD4KICAgICAgICAgPHRpZmY6Qml0c1BlclNhbXBsZT4KICAgICAgICAgICAgPHJkZjpTZXE+CiAgICAgICAgICAgICAgIDxyZGY6bGk+ODwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpPjg8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaT44PC9yZGY6bGk+CiAgICAgICAgICAgIDwvcmRmOlNlcT4KICAgICAgICAgPC90aWZmOkJpdHNQZXJTYW1wbGU+CiAgICAgICAgIDx0aWZmOlBob3RvbWV0cmljSW50ZXJwcmV0YXRpb24+MjwvdGlmZjpQaG90b21ldHJpY0ludGVycHJldGF0aW9uPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8dGlmZjpTYW1wbGVzUGVyUGl4ZWw+MzwvdGlmZjpTYW1wbGVzUGVyUGl4ZWw+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpFeGlmVmVyc2lvbj4wMjIxPC9leGlmOkV4aWZWZXJzaW9uPgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjE1MDwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4xNTA8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAg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);
    background-size: 22px 22px;
    -moz-background-size: 22px 22px;
    background-repeat: no-repeat;
    position: absolute;
    top: 5px;
    right: 5px;
    height: 22px;
    z-index: 99;
    width: 22px;
}


/* -- css div popup ------------------------------------------------------------------------ */
.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #99CCFF;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 10pt;
    width: 500px;
}

/* -- report ------------------------------------------------------------------------ */

#show_detail_line .label {
    font-size: 85%;
    cursor: pointer;
}

#show_detail_line {
    margin: 2em auto 1em auto;
}

#total_row  { font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }

</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """<div class='heading'>
<h1>%(title)s</h1>
%(parameters)s
<p class='description'>%(description)s</p>
</div>

"""  # variables: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p><strong>%(name)s:</strong> %(value)s</p>
"""  # variables: (name, value)

    # ------------------------------------------------------------------------
    # Report
    #

    REPORT_TMPL = """
<p id='show_detail_line'>
<span class="label label-primary" onclick="showCase(0)">Summary</span>
<span class="label label-danger" onclick="showCase(1)">Failed</span>
<span class="label label-default" onclick="showCase(2)">All</span>
</p>
<table id='result_table' class="table">
    <thead>
        <tr id='header_row'>
            <th>Test Suite/Test Case 测试套件/用例</td>
            <th>Count 个数</td>
            <th>Pass 通过</td>
            <th>Fail 不通过</td>
            <th>Error 测试程序异常</td>
            <th>View 查看</td>
        </tr>
    </thead>
    <tbody>
        %(test_list)s
    </tbody>
    <tfoot>
        <tr id='total_row'>
            <td>Total 总共</td>
            <td>%(count)s</td>
            <td class="text text-success">%(Pass)s</td>
            <td class="text text-danger">%(fail)s</td>
            <td class="text text-warning">%(error)s</td>
            <td>&nbsp;</td>
        </tr>
    </tfoot>
</table>
"""  # variables: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td><a class="btn btn-xs btn-primary"href="javascript:showClassDetail('%(cid)s',%(count)s)">Detail 详情</a></td>
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='4' align='center'>

        <!--css div popup start-->
        <a class="popup_link btn btn-xs btn-default" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
            %(status)s</a>

        <div id='div_%(tid)s' class="popup_window">
            <div style='text-align: right;cursor:pointer'>
            <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
               [x]</a>
            </div>
            <pre>
            %(script)s
            </pre>
        </div>
        <!--css div popup end-->

    </td>
    <td colspan='1' align='center'>%(img)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>%(status)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #

    IMG_TMPL = r"""
            <a href="#"  onclick="show_img(this)">Snapshot 截图</a>
        <div align="center" class="screenshots"  style="display:none">
            <a class="close_shots"  href="#"   onclick="hide_img(this)"></a>
            %(images)s
            <div class="imgyuan"></div>
        </div>
        """

    ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""


# -------------------- The end of the Template class -------------------

TestResult = unittest.TestResult

class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        super().__init__(verbosity=verbosity)
        self.outputBuffer = io.StringIO()
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        stdout_redirect.fp = self.outputBuffer
        stderr_redirect.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirect
        sys.stderr = stderr_redirect

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        if getattr(test, 'logger', TestLogger):
            test.logger.info("测试用例执行成功")
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        if getattr(test, 'logger', TestLogger):
            test.logger.error("测试用例执行异常：%s" % str(err))

        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))

        # if not getattr(test, "base_driver", ""):
        #     pass
        # else:
        #     try:
        #         driver = getattr(test, "base_driver")
        #         test.images.append(driver.save_window_snapshot_by_io())
        #     except Exception as e:
        #         pass

        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        if getattr(test, 'logger', TestLogger):
            test.logger.error("测试用例执行失败：%s" % str(err))
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))

        # if not getattr(test, "base_driver", ""):
        #     pass
        # else:
        #     try:
        #         driver = getattr(test, "base_driver")
        #         test.images.append(driver.save_window_snapshot_by_io())
        #     except Exception as e:
        #         pass

        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

class TestRunner(_TemplateReport):
    """
    HtmlTestRunner
    """
    file_name = None

    def __init__(self, file_name, verbosity=1, title=None, description=None):
        """
        initialize
        :param stream:
        :param verbosity:
        :param title:
        :param description:
        """

        self.file_name = file_name
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

    def run(self, test):
        """
        Run the given test case or test suite.
        :param test:
        :return:
        """
        with open(self.file_name, mode="wb") as stream:
            self.stream = stream
            result = _TestResult(self.verbosity)
            test(result)
            self.stopTime = datetime.datetime.now()
            self.generate_report(test, result)
            print('Time Elapsed 花费时间: %s' % (self.stopTime - self.startTime))

        return result

    def sort_result(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def get_report_attributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []
        if result.success_count: status.append(
            '<span class="text text-success">Pass <strong>%s</strong></span>' % result.success_count)
        if result.failure_count: status.append(
            '<span class="text text-danger">Failure <strong>%s</strong></span>' % result.failure_count)
        if result.error_count:   status.append(
            '<span class="text text-warning">Error <strong>%s</strong></span>' % result.error_count)
        if status:
            status = ' '.join(status)
        else:
            status = 'none'
        return [
            ('Start Time 开始时间', startTime),
            ('Duration 用时', duration),
            ('Status 状态', status),
        ]

    def generate_report(self, test, result):
        report_attrs = self.get_report_attributes(result)
        generator = 'HtmlTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        output = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            ending=ending,
        )
        self.stream.write(output.encode())

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                # name = saxutils.escape(name),
                # value = saxutils.escape(value),
                name=name,
                value=value,
            )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
        )
        return heading

    def _generate_report(self, result):
        rows = []
        sortedResult = self.sort_result(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                else:
                    ne += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name


            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'text text-warning' or nf > 0 and 'text text-danger' or 'text text-success',
                desc=desc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid + 1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
        )
        return report

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            ue = e
        else:
            ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )

        # 处理截图
        if getattr(t, 'images', []):
            # 判断截图列表，如果有则追加
            tmp = u""
            for i, img in enumerate(t.images):
                if i == 0:
                    tmp += """ <img src="data:image/jpg;base64,%s" style="display: block;" class="img"/>\n""" % img
                else:
                    tmp += """ <img src="data:image/jpg;base64,%s" style="display: none;" class="img"/>\n""" % img
            images = self.IMG_TMPL % dict(images=tmp)
        else:
            images = u"""无截图"""

        row = tmpl % dict(
            tid=tid,
            # Class = (n == 0 and 'hiddenRow' or 'none'),
            Class=(n == 0 and 'hiddenRow' or 'text text-success'),
            # style = n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'none'),
            style=n == 2 and 'text text-warning' or (n == 1 and 'text text-danger' or 'text text-success'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
            img=images,
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL

class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HtmlTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HtmlTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = TestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)

class TestSuite(unittest.TestSuite):
    """A test suite is a composite test consisting of a number of TestCases.

    For use, create an instance of TestSuite, then add test case instances.
    When all tests have been added, the suite can be passed to a test
    runner, such as TextTestRunner. It will run the individual test cases
    in the order in which they were added, aggregating the results. When
    subclassing, do not forget to call the base class constructor.
    """

    def run(self, result, debug=False):
        topLevel = False
        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = topLevel = True

        for index, test in enumerate(self):
            if result.shouldStop:
                break

            if _isnotsuite(test):
                self._tearDownPreviousClass(test, result)
                self._handleModuleFixture(test, result)
                self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__

                if (getattr(test.__class__, '_classSetupFailed', False) or
                        getattr(result, '_moduleSetUpFailed', False)):
                    continue

            if not debug:
                test(result)
            else:
                test.debug()

            if self._cleanup:
                self._removeTestAtIndex(index)

        if topLevel:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False
        return result

    def debug(self):
        """Run the tests without collecting errors in a TestResult"""
        debug = _DebugResult()
        self.run(debug, True)

    def add_test(self, test):
        """
        添加单个测试
        :param test: 测试用例的类实例化的对象
        :return:
        """
        self.addTest(test)

    def add_tests(self, tests):
        """
        添加多个测试
        :param tests:
        :return:
        """
        self.addTests(tests)

main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
