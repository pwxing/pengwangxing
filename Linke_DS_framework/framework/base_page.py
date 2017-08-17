# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
from selenium import webdriver

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类    """

    user = "htest"
    pwd = "123456"
    code = "HY7102$"
    now = time.strftime("%Y_%m_%d_%H_%M_%S")

    def __init__(self, driver):
        self.driver = driver

        # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

        # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

        # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

        # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

            # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

            # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # selector_select_value = selector.split('=>')[2]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        # if selector_select_value != "":
        #     print selector_select_value
        #     element = self.driver.find_element_by_id(selector_value).find_element_by_xpath(selector_select_value)
        return element

        # 输入文本框
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # select框直接赋值
    def type_select(self, selector, text):
        el = self.find_element(selector)
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 选择复选框
    def select_checkbox(self, selector):
        el = self.find_element(selector)
        try:
            if el.is_selected():
                pass
            else:
                el.click()
            logger.info("the checkbox is click.")
        except NameError as e:
            logger.error("Failed to click the checkbox with %s" % e)
            self.get_windows_img()

    # 取消复选框
    def cancel_checkbox(self, selector):
        el = self.find_element(selector)
        try:
            if el.is_selected():
                el.click()
            else:
                pass
            logger.info("the checkbox is cancel.")
        except NameError as e:
            logger.error("Failed to cancel the checkbox with %s" % e)
            self.get_windows_img()

    # 点击元素

    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            # logger.info("The element \' %s \' was clicked." % el.text)
            logger.info("The element  was clicked.")
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 选择select
    def click_select(self, selector, selector2):
        el = self.find_element(selector)
        el = el.find_element_by_xpath(selector2)

        try:
            el.click()
            # logger.info("The element \' %s \' was clicked." % el.text)
            logger.info("The select  was clicked.")
        except NameError as e:
            logger.error("Failed to click the select with %s" % e)

    # 点击链接
    def click_partial_link_text(self, selector):
        el = self.driver.find_element_by_partial_link_text(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % selector)
            # logger.info("The element  was clicked.")
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取网页标题

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 获取网页源
    def get_page_source(self):
        logger.info("Current page_source is ")
        # return self.driver.t

    # 获取元素的text
    def get_element_text(self, selector):
        el = self.find_element(selector)
        logger.info("element_text("+selector+") is "+el.text)
        return el.text

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    # 获取元素是否被选中
    @staticmethod
    def get_element_is_select(self, selector):
        el = self.find_element(selector)
        logger.info(el + " is " + el.is_selected())
        return el.is_selected()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)


    @staticmethod
    def assert_page_source(self, text):
        assert text in self.driver.page_source

    # 获取异常即使断言失败，用例也算成功，除非最后加一句exit()
    @staticmethod
    def assert_page_source1(self, text):
        try:
            assert text in self.driver.page_source
            # 调用页面对象继承基类中的获取页面源码
            print 'Test Pass.'
        except Exception as e:
            print 'Test Fail.', format(e)
            exit()