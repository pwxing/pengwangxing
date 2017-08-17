#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ssotest.ematong.com/cas/login?service=http://bmtest.ematong.com/shiro-cas"

    def test_XXXXX(self):
        driver = self.driver
        driver.get(self.base_url)
        # 输入用户名密码登录
        driver.find_element_by_id("user2").send_keys("htest")
        driver.find_element_by_id("password2").send_keys("123456")
        driver.find_element_by_id("submit2").click()

        driver.implicitly_wait(10)
        # 主页点击电商
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/a").click()

        driver.find_element_by_partial_link_text("客户管理").click()
        time.sleep(1)
        driver.find_element_by_name("nick").send_keys("pwx")

        driver.find_element_by_name("status").find_element_by_xpath("//option[@value='0']").click()
        driver.find_element_by_partial_link_text("搜索").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text("查看").click()
        time.sleep(1)
        driver.switch_to.frame("kfgmsj")
        # if driver.page_source.
        driver.switch_to.parent_frame()
        # driver.switch_to.default_content()
        # print driver.page_source
        assert u'pwx的购买数据' in driver.page_source
        time.sleep(1)
        # driver.find_element_by_xpath("/html/body/div[3]/div[2]/a").click()
        driver.find_element_by_css_selector("a.g-btn.g-btn-init").click()


        time.sleep(1)

        time.sleep(5)
    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()