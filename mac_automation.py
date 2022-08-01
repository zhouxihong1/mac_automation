#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        : mac_automation.py
@Contact     : https://github.com/zxih/mac_automation
@Version     : 1.0
@Modify Time : 2022/7/26 22:34
@Author      : zxh
@Desciption  : None
@License     : (C)Copyright 2022-Inf
"""
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# caps = {}
# caps["appium:automationName"] = "Mac2"
# caps["platformName"] = "mac"
# caps["appium:bundleId"] = "xxx"
# caps["appium:noReset"] = True
# # caps["appium:newCommandTimeout"] = 2000
# caps["appium:connectHardwareKeyboard"] = True


# driver = webdriver.Remote("http://192.168.1.2:4723", caps)


class MacAutomation:

    def __init__(self, mac_ip="192.168.1.2", port=4723, caps=None):
        if caps is None:
            caps = {'appium:automationName': 'Mac2', 'platformName': 'mac',
                    'appium:bundleId': 'xxx', 'appium:noReset': True,
                    'appium:connectHardwareKeyboard': True, "appium:newCommandTimeout": 2000}
        self.driver = webdriver.Remote("http://{}:{}".format(mac_ip, port), caps)
        if self.driver is not None:
            print("非首次连接,先退出之前连接")
            self.quit()
        self.driver = webdriver.Remote("http://{}:{}".format(mac_ip, port), caps)

    def active_window(self, delay=0, bundle_id='xxx'):
        """
        激活当前应用程序 -> 由于链接跳转或者第三方应用被链式打开,此时需要重新激活当前应用程序,然后继续自动化操作
        :param bundle_id: bundleId为要激活的程序id
        :param delay: 延时,单位是秒,默认没有延时,解决有些窗体延时出现挡住主窗体问题
        :return:
        """
        time.sleep(delay)
        self.driver.execute_script("macos: activateApp", {"bundleId": bundle_id})
        # self.__init__()  # 重新初始化

    def quit(self):
        """
        退出driver
        :return:
        """
        self.driver.quit()

    def is_element_exist(self, value, by=AppiumBy.XPATH, max_time=5, is_elements=False):
        """
        判断指定元素在指定时间内是否存在
        :param by: 通过何种方式查找,默认是XPATH
        :param value: 查找的selector是什么
        :param max_time: 最大的查找时间，单位是秒,默认是5s
        :param is_elements: 是否查找一组元素,默认是FALSE
        :return:
        """
        times = 10
        interval = max_time/times
        ele = False
        for i in range(times):
            try:
                if i > int(times/2):
                    self.active_window()  # 新增查找时间超过1/2 最大次数时,会将窗体激活,解决有些窗体延时出现挡住当前窗体找不到
                if is_elements:
                    element = self.driver.find_elements(by=by, value=value)
                else:
                    element = self.driver.find_element(by=by, value=value)
            except Exception as e:
                # print(e)
                print("未找到,休眠{}s后,继续查找;共耗时{}s".format(interval, interval*(i+1)))
                time.sleep(interval)
            else:
                ele = element
                break
        else:
            print("达到最大查找时间{}s,停止查找".format(max_time))
        return ele

    def find_element(self, value, by=AppiumBy.XPATH, max_time=10):
        """
        查找元素
        :param by: 通过何种方式查找,默认是XPATH
        :param value: 查找的selector是什么
        :param max_time: 最大的查找时间，单位是秒,默认是10s
        :return:
        """
        element = self.is_element_exist(value=value, by=by, max_time=max_time, is_elements=False)
        return element

    def find_elements(self, value, by=AppiumBy.XPATH, max_time=10):
        """
        查找一类元素
        :param by: 通过何种方式查找,默认是XPATH
        :param value: 查找的selector是什么
        :param max_time: 最大的查找时间，单位是秒,默认是10s
        :return:
        """
        element = self.is_element_exist(value=value, by=by, max_time=max_time, is_elements=True)
        return element

    def click_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        为了解决element点击时出问题的方法
        :param element: 标准元素
        :param radio_x: 元素的偏移量x,默认居中,0.5
        :param radio_y: 元素的偏移量y,默认居中,0.5
        :return:
        """
        ele_rect = element.rect
        print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.driver.execute_script('macos: click', {"x": x, "y": y})
        time.sleep(0.3)

    def right_click_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        为了解决右击元素出现的问题
        :param element: 标准元素
        :param radio_x: 元素的偏移量x,默认居中,0.5
        :param radio_y: 元素的偏移量y,默认居中,0.5
        :return:
        """
        ele_rect = element.rect
        print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.driver.execute_script('macos: rightClick', {"x": x, "y": y})
        time.sleep(0.3)

    def double_click_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        为了解决没有双击元素的方法
        :param element: 标准元素
        :param radio_x: 元素的偏移量x,默认居中,0.5
        :param radio_y: 元素的偏移量y,默认居中,0.5
        :return:
        """
        ele_rect = element.rect
        print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.driver.execute_script('macos: doubleClick', {"x": x, "y": y})
        time.sleep(0.3)

    def hover_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        为了解决没有悬停元素的方法
        :param element: 标准元素
        :param radio_x: 元素的偏移量x,默认居中,0.5
        :param radio_y: 元素的偏移量y,默认居中,0.5
        :return:
        """
        ele_rect = element.rect
        print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.driver.execute_script('macos: hover', {"x": x, "y": y})
        time.sleep(0.3)

    def send_keys(self, key_list, element=None):
        """
        全局发送字符,如果未指定element,则直接发送键盘字符
        :param key_list: 发送字符的list元素,如果指定了字符串,则会在内部转换
        :param element: 标准元素
        :return:
        """
        if element:
            self.click_element(element)
        if isinstance(key_list, str):
            key_list = list(key_list)
        self.driver.execute_script('macos: keys', {'keys': key_list})

    def clear_keys(self, element=None):
        """
        使用command+a+delete的形式，清空任意位置的所有内容
        :param element: 标准元素
        :return:
        """
        if element:
            self.click_element(element)
        self.driver.execute_script('macos: keys', {'keys': [{
            'key': 'a',
            'modifierFlags': 1 << 4}, 'XCUIKeyboardKeyDelete']})

    def quit_window(self, element=None):
        """
        使用command+q的形式, 退出窗体
        :param element: 标准元素
        :return:
        """
        if element:
            self.click_element(element)
        self.driver.execute_script('macos: keys', {'keys': [{
            'key': 'q',
            'modifierFlags': 1 << 4}]})

    def switch_window(self, element=None):
        """
        切换主界面
        :param element: 标准元素
        :return:
        """
        if element:
            self.click_element(element)
        self.driver.execute_script('macos: keys', {'keys': [{
            'key': "XCUIKeyboardKeyTab",
            'modifierFlags': 1 << 4}]})


if __name__ == '__main__':
    ma = MacAutomation()
    ma.switch_window()
