import contextlib
import csv
import datetime
import io
import logging
import os
import smtplib
import sys
import time
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum, unique
from this import i
from unittest import TestCase as TC, SkipTest
from unittest.case import _ShouldStop
from unittest.suite import _DebugResult, _isnotsuite
from xml.sax import saxutils

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import getAttribute_js
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

    def __init__(self, browser_type=0, download_path="c:\\Users\\tester\\Downloads", by_char=","):
        """
        构造方法：实例化 BoxDriver 时候使用
        :param browser_type: 浏览器类型
        :param by_char: 分隔符，默认使用","
        """
        self._actions = []

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

    def set_window_size(self, m, n):
        """
        最大化当前浏览器的窗口
        :return:
        """
        self._base_driver.set_window_size(m, n)

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

    def types(self, selector, text, n):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        第几个输入
        """
        els = self._locate_elements(selector)
        el = els[int(n)]
        el.clear()
        el.send_keys(text)

    def clear(self, selector):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self._locate_element(selector)
        el.clear()
        el.send_keys()

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        el = self._locate_element(selector)
        el.click()

    def clicks(self, selector, n):
        """
        数组里面点击一个
        n 是第几个

        """
        els = self._locate_elements(selector)
        el = els[int(n)]
        el.click()

    def clicks_by_text(self, selector, text):
        """
        捕捉文本点击
        text 是文本V
        """
        # 定义一个元素
        eles = self._locate_elements(selector)
        # ele 遍历数组每个元素
        for ele in eles:
            if ele.text == text:
                ele.click()

    def clicks_by_index(self, selector, n):
        """
        点击一组元素中第几个
        text 是文本V
        """
        # 定义一个元素
        eles = self._locate_elements(selector)
        # 列表中抽到对应的来点击
        eles[n].click()

    def clicks_mn(self, selector, m, n):
        """
        数组矩阵点击某个
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        # els0 = self._locate_elements(selector)
        # e1 = str(m)
        # e2 = str(n)
        # e = els0[str(e1), str(e2)]
        # e.click()

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

    def click_and_hold(self, on_element=None):
        """
        Holds down the left mouse button on an element.

        :Args:
         - on_element: The element to mouse down.
           If None, clicks on current mouse position.

        """
        # 点击鼠标左键，不松开

        if self._base_driver.w3c:
            ActionBuilder(self._base_driver).pointer_action.click_and_hold(on_element)
            ActionBuilder(self._base_driver).key_action.pause()
            if on_element:
                ActionBuilder(self._base_driver).key_action.pause()
        else:
            if on_element:
                self.move_to_element(on_element)
            self._actions.append(lambda: self._base_driver.execute(
                Command.MOUSE_DOWN, {}))
        return self

    def move_to_element(self, to_element):
        """
        Moving the mouse to the middle of an element.

        :Args:
         - to_element: The WebElement to move to.
        """
        if self._base_driver.w3c:
            ActionBuilder(self._base_driver).pointer_action.move_to(to_element)
            ActionBuilder(self._base_driver).key_action.pause()
        else:
            self._actions.append(lambda: self._base_driver.execute(
                Command.MOVE_TO, {'element': to_element.id}))
        return self

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

    def select_and_click(self, selector, text, n):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        # 选择第二个点击
        el = self._locate_elements(selector)

        # el = self._locate_element(selector)
        Select(el[n]).select_by_visible_text(text)

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
    鼠标时间
    
    """

    def drag_and_drop_by_offset(self, selector, xoffset, yoffset):
        pass
        """
        按住源元素上的鼠标左键，然后移动到目标偏移量并释放鼠标按钮。
        source: 按住鼠标的元素位置
        xoffset: X轴的偏移量
        yoffset: Y轴的偏移量
        """

    def perform(self):
        pass

    """
    JavaScript 相关
    JavaScript 相关
    """

    def execute_js(self, script):
        """
        执行JS脚本

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

    def get_attribute_text(self, selector, attribute, n):
        """
        获取数组中对应第N条数据参数的值
        Gets the value of an element attribute.
m
        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self._locate_elements(selector)
        return el[n].get_attribute(attribute)

    def get_text(self, selector):
        """
        Get element text information.
        获取元素文本信息

        Usage:
        driver.get_text("i,el")
        """
        el = self._locate_element(selector)
        return el.text

    def get_texts(self, selector, n):
        """
        Get element text information.
        获取第n个文本信息

        Usage:
        driver.get_text("i,el")
        """
        el = self._locate_elements(selector)
        return el[n].text

    def get_text_change(self, selector, text):
        """
        获取某一不能清除的文本修改，先退格s
        Get element text information.

        Usage:
        driver.get_text("i,el")

        """
        el = self._locate_element(selector)
        el.clear()
        el.send_keys("\b" + str(text))
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
        """
        该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
        :param self:
        :param selector: 元素定位，如'id,account'
        :return: 布尔值
        """
        flag = True
        try:
            self._locate_element(selector)
            return flag
        except:
            flag = False
            return flag

    def get_enabled(self, selector):
        """
        判断页面元素是否可点击
        :param selector: 元素定位
        :return: 布尔值
        """
        if self._locate_element(selector).is_enabled():
            return True
        else:
            return False

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
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
        """
            Accept warning box.

            Usage:
            driver.accept_alert()
            """
        self._base_driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        """
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
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        """
        original_windows = self._base_driver.current_window_handle
        el = self._locate_element(selector)
        el.click()
        all_handles = self._base_driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self._base_driver._switch_to.window(handle)

    def switch_to_window_by_index(self, index):
        """
        切换到新窗口
        :param index:需要切换到第几个窗口，从左往右数，数到第几个就是几
        :return:
        """
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

    def save_window_snapshot_by_io(self, file_name):
        """
        保存截图为文件流
        :return:
        """
        driver = self._base_driver
        driver.save_screenshot(file_name)
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

    def upload_input(self, selector, file):
        """
        上传文件 （ 标签为 input 类型，此类型最常见，最简单）
        :param selector: 上传按钮定位
        :param file: 将要上传的文件（绝对路径）
        :return: 无
        """
        self._locate_element(selector).send_keys(file)

    def upload_not_input(self, file, browser_type='Chrome'):
        """
        上传文件 （ 标签不是 input 类型，使用 win32gui,得先安装 pywin32 依赖包）
                                                pip install pywin32
        :param browser_type: 浏览器类型（Chrome浏览器和Firefox浏览器的有区别）
        :param file: 将要上传的文件（绝对路径）
        单个文件：file1 = 'C:\\Users\\list_tuple_dict_test.py'
        同时上传多个文件：file2 = '"C:\\Users\\list_tuple_dict_test.py" "C:\\Users\\class_def.py"'
        :return: 无
        """
        # Chrome 浏览器是'打开'
        # 对话框
        # 下载个 Spy++ 工具，定位“打开”窗口，定位到窗口的类(L):#32770, '打开'为窗口标题
        # dialog = None
        # if browser_type == 'Chrome':
        #     dialog = win32gui.FindWindow('#32770', u'打开')
        # elif browser_type == 'Firefox':
        #     # Firefox 浏览器是'文件上传'
        #     # 对话框
        #     dialog = win32gui.FindWindow('#32770', u'文件上传')
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        # # 确定按钮Button
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        # # 往输入框输入绝对地址
        # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)
        # # 按button
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        # 获取属性
        # print(upload.get_attribute('value'))

        """
        表单数据提交:
            页面校验
            数据库校验
            某条记录选择，编辑，删除
        """

    def del_edit_choose_the_row(self, selector_of_next_page, selector_of_trs_td, selector_of_del_edit_choose,
                                expected_td_value):
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
            print(e)
            print('%s 操作成功！' % expected_td_value)

    def assert_new_record_exist_in_table(self, selector_of_next_page, selector_of_trs_td, expected_td_value):
        """
        此方法针对页面列表（带多页翻页功能），都可以判断新增记录是否添加成功！
        若新增成功，则返回 True 布尔值；否则返回 False 布尔值
        :param selector_of_next_page: "下一页"定位，如：
        :param selector_of_trs_td:所有行的某一列的定位，如： 'l,下页''x,/html/body/div/div[2]/div/div[1]/div/table/tbody//tr/td[2]'
        :param expected_td_value:期望的列内容,如：'华仔'
        :return: 布尔值
        """
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
            print(e)
            # count_page_real_show = count_per_page_whiles + first_count_per_page
            # print("页面实际显示记录条数：%s" % count_page_real_show)
            # 页面统计总数 VS 页面实际显示记录总数
            # assert count_page_real_show == int(total_num)
            # print("‘页面实际显示记录总数’ 与 ‘页面统计显示记录总数’ 相同！")

            # raise NameError("页面表单中无此数据，原因：(1)请查询待验证的数据是否输入正确？(2)或者'下页'翻页定位是否正确？")
            print("页面表单中无此数据，原因：(1)请查询待验证的数据是否输入正确？(2)或者'下页'翻页定位是否正确？")
            return False

    def assert_new_record_exist_mysql(self, db_yaml_path, db_yaml_name, sql_file_path, select_field_num,
                                      expected_td_value):
        """
        数据库校验，True为数据库中存在该数据
        :param db_yaml_path: 数据库的yaml格式的配置文件路径
        :param db_yaml_name: 数据库的yaml格式的配置文件中设置的数据库名（默认是在'DbConfig'下面）
        :param sql_file_path: sql文件路径
        :param select_field_num: 查询语句中第几个字段（默认0表示第1个字段）
        :param expected_td_value: 期望要断言的值
        :return: True / False
        """
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
        except Exception as e:
            print(e)
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
        # cur_path = os.path.dirname(os.path.realpath(__file__))
        # self.file_name = os.path.join(os.path.dirname(cur_path),'logs')
        # self.logger = logging.getLogger()
        # self.logger.setLevel(logging.DEBUG)
        # # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]: %(message)s')

        if logger is not None:
            self.logger = TestLogger(logger)
        else:
            test_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            self.logger = TestLogger("test_log_%s.log" % test_time)

        self.base_driver = driver
        self.logger = logger

        self._actions = []
        if self.base_driver:
            self.w3c_actions = ActionBuilder(driver)

    # def infos(self, message):
    #     """
    #     添加信息日志
    #     :param message:
    #     :return:
    #     """
    #     self.logger("info", message)
    #
    # def logger(self, level, message):
    #     # 创建一个FileHandler，用于写到本地
    #     fh = logging.FileHandler(self.file_name, 'a', encoding='utf8')
    #     fh.setLevel(logging.DEBUG)
    #     fh.setFormatter(self.formatter)
    #     self.logger.addHandler(fh)
    #
    #     # 创建一个SteamHandler,用于输出到控制台
    #     ch = logging.StreamHandler(sys.stdout)
    #     ch.setLevel(logging.DEBUG)
    #     ch.setFormatter(self.formatter)
    #
    #     self.logger.addHandler(ch)
    #     if level == 'info':
    #         self.logger.info(message)
    #     elif level == 'debug':
    #         self.logger.debug(message)
    #     elif level == 'warning':
    #         self.logger.warning(message)
    #     elif level == 'error':
    #         self.logger.error(message)
    #     elif level == 'example':
    #         self.logger.error(message)
    #     # 这两行代码为了避免日志输出重复
    #     self.logger.removeHandler(ch)
    #     self.logger.removeHandler(fh)
    #     fh.close()

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

    def logs(self, msg):
        """
        记录日志
        :param msg:
        :return:
        """
        if self.logger is not None:
            self.logger.info(msg)

    def example(self, msg):
        """
        记录日志
        :param msg:
        :return:
        """
        if self.logger is None:
            self.logger.info(msg)
        return

    def info(self, message):
        """
        添加信息日志
        :param message:
        :return:
        """
        self.logger("info", message)


class CsvHelper(object):

    def read_data(self, f, encoding="utf-8-sig"):
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
        # self.connect = pymysql.connect(host=host, port=port,
        #                                user=user, password=password,
        #                                db=database, charset=charset)

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

    def email_attachment(self, report_file):
        ''' 配置发送附件测试报告到邮箱 '''
        ''' 发件相关参数 '''
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

    def example(self, message):
        """
        运行用例日志信息
        :param message:
        :return:
        """
        self._console("example", message)

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
        elif level == 'example':
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


# import datetime
# import io
# import sys
# import unittest
# from xml.sax import saxutils


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
        # 3: 'passrate',
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
    background-image: url(data:image/png;base64)
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
<span class="label label-primary" onclick="showCase(0)">Summary 摘要</span>
<span class="label label-danger" onclick="showCase(1)">Failed 失败</span>
<span class="label label-default" onclick="showCase(2)">All 所有</span>
</p>
<table id='result_table' class="table">
    <thead>
        <tr id='header_row'>
            <th>Lottery 数字彩分类/用例</td>
            <th>Count 个数</td>
            <th>Pass 通过</td>
            <th>Fail 不通过</td>
            <th>Error 测试程序异常</td>
            <th>PassRate 通过率</td>
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
            <td>
            <script>
            document.write(division(%(Pass)s,%(count)s));
            function division(arg1, arg2){
            var t1 = 0, t2 = 0, r1, r2;
            try { 
                t1 = new String(arg1).split(".")[1].length;
            } catch (e) { }
            try { 
                t2 = arg2.toString().split(".")[1].length;
            } catch (e) { }
            r1 = Number(new String(arg1).replace(".", ""));
            r2 = Number(arg2.toString().replace(".", ""));
            //放大倍数后两个数相除后
            var money = r1 / r2;
            //保留2个小数位数
            return money.toFixed(2);
            }
            </script>%%
            </td>
</td></td>
            <td>&nbsp;</td>
        </tr>    
    </tfoot>
    
</table>
<tr id='head_row'>
            <td>报告说明：</td>
            <p>1、测试用例放在Detail里面的pass</p>
            <p>2、测试异常截图在/fusion/pictures文件夹下</p>
        </tr>
        
        

"""  # variables: (test_list, count, Pass, fail, error, passrate)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td><script>
    document.write(division(%(Pass)s,%(count)s));
    function division(arg1, arg2){
    var t1 = 0, t2 = 0, r1, r2;
    try { 
        t1 = new String(arg1).split(".")[1].length;
    } catch (e) { }
    try { 
        t2 = arg2.toString().split(".")[1].length;
    } catch (e) { }
    r1 = Number(new String(arg1).replace(".", ""));
    r2 = Number(arg2.toString().replace(".", ""));
    //放大倍数后两个数相除后
    var money = r1 / r2;
    //保留2个小数位数
    return money.toFixed(2);
}
</script>%%
</td>
    
   
    <td><a class="btn btn-xs btn-primary"href="javascript:showClassDetail('%(cid)s',%(count)s)">Detail 详情</a></td>
</tr>

"""  # variables: (style, desc, count, Pass, fail, error, passrate cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='4' align='center'>

        <!--css div popup start-->
        <a class="popup_link btn btn-xs btn-default" onfocus='this.blur();' 
        href="javascript:showTestDetail('div_%(tid)s')" >
            %(status)s</a>

        <div id='div_%(tid)s' class="popup_window">
            <div style='text-align: right;cursor:pointer'>
            <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
               [x]</a>
            </div>
            <pre> 
            %(script)s
            </pre>
            <script>        
            function save_file{  	
            var fso, tf;
            fso = new ActiveXObject("Scripting.FileSystemObject");
            tf = fso.CreateTextFile("/fusion/2.txt", true);
            tf.WriteLine("Testing 1, 2, 3.") ;
            tf.WriteBlankLines(3) ;
            tf.Write ("This is a test.");
            tf.Close();
            }
            </script>
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
        self.passrate_count = 0
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
        # if result.passrate_count:   status.append(
        #     '<span class="text text-passrate">PassRate <strong>%s</strong></span>' % result.passrate_count)
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
            np = nf = ne = npra = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                if n == 1:
                    nf += 1
                if n == 2:
                    ne += 1
                # else:
                #     npra += 1

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
                # passrate=npra,
                cid='c%s' % (cid + 1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            # count=str(result.success_count + result.failure_count + result.error_count + result.passrate_count),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
            passrate=str(result.passrate_count),
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
            # images = u"""无截图"""
            images = u"""捕捉到图片文件夹路径：/fusion/pictures"""

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


def context_click(on_element=None):
    pass
    """
    鼠标右键点击
    如果参数不写，那么点的是当前鼠标位置
    如果参数写定位到的元素对象element，那就是点这个元素
    """


def click(on_element=None):
    pass
    """
    点击:
    如果参数不写，那么点击的是当前鼠标位置
    如果参数写定位到的元素对象element，那就是点这个元素
    """


def click_and_hold(on_element=None):
    pass
    """
    鼠标左键按住某个元素
    如果参数不写，那么点的是当前鼠标位置
    如果参数写定位到的元素对象element，那就是点这个元素
    """


def double_click(on_element=None):
    pass
    """
    双击鼠标
    如果参数不写，那么点的是当前鼠标位置
    如果参数写定位到的元素对象element，那就是点这个元素
    """


def drag_and_drop(source, target):
    pass
    """
    按住源元素上的鼠标左键，然后移动到目标元素并释放鼠标按钮
    source: 按住鼠标的元素位置
    target: 松开鼠标的元素位置
    """


def drag_and_drop_by_offset(source, xoffset, yoffset):
    pass
    """
    按住源元素上的鼠标左键，然后移动到目标偏移量并释放鼠标按钮。
    source: 按住鼠标的元素位置
    xoffset: X轴的偏移量
    yoffset: Y轴的偏移量
    """


def key_down(value, element=None):
    pass
    """
    只发送一个按键，而不释放它。只应用于修饰键（控制、alt和shift）。

    value: 要发送的修饰符键。值在“Keys”类中定义。
    element: 定位的元素
    如果element参数不写就是当前鼠标的位置

     举个例子，按住
    ctrl + c::

    ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    """


def move_by_offset(xoffset, yoffset):
    """
    将鼠标移动到当前鼠标位置的偏移量

    xoffset: X轴
    作为一个正整数或负整数移动到x偏移量
     yoffset: Y轴
    偏移，作为正整数或负整数。
    """

    def move_to_element(self, to_element):
        pass
        """
        鼠标悬停
        - to_element: 定位需要悬停的元素
        """


def move_to_element_with_offset(to_element, xoffset, yoffset):
    pass
    """
    通过指定元素的偏移量移动鼠标。偏移量与元素的左上角相对
    - to_element: 定位需要悬停的元素
    - xoffset: X
    轴偏移量
    - yoffset: Y
    轴偏移量
    """


def release(on_element=None):
    pass
    """
    释放一个元素上的鼠标按钮。

    - 如果参数不写，那么是当前鼠标位置
    - 如果参数写定位到的元素对象element，那就是这个元素.
    """





class ActionChainss(object):
    def __init__(self, driver):
        self._base_driver = driver
        self._actions = []
        if self._base_driver:
            self._actions = ActionBuilder(self._base_driver)

    def perform(self):
        # 执行行为事件
        if self._base_driver:
            self._actions.perform()
        else:
            for action in self._actions:
                action()

    def key_up(self, value, element=None):
        pass

        # 释放按键，配合上面的一起使用

    def send_keys(self, *keys_to_send):
        """"
        发送到当前焦点元素
        要发送的按键。修饰符键常数可以在“Keys”类。

        def send_keys_to_element(self, element, *keys_to_send):
            发送到定位到的元素上
            - element: 定位的元素
            - keys_to_send: 要发送的按键。修饰符键常数可以在“Keys”类。
        """


if __name__ == "__main__":
    main(module=None)
