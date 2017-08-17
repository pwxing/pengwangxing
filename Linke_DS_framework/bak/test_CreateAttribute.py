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

    def test_CreateAttribute(self):
        driver = self.driver
        driver.get(self.base_url)

        # driver.maximize_window()
        # driver.set_window_size(400,800)
        driver.find_element_by_id("user2").send_keys("htest")
        driver.find_element_by_id("password2").send_keys("123456")
        driver.find_element_by_id("submit2").click()
        # 休眠2秒
        # time.sleep(2)
        # 智能等待
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/a").click()
        # driver.save_screenshot('pic\screenshot.png')
        # driver.save_screenshot('pic\screenshot.png')

        driver.find_element_by_partial_link_text("属性模板").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text("模板列表").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text("添加模板").click()
        # 自定义
        driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div[1]/div[5]/span[2]").click()
        # 服装
        driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div[1]/div[5]/span[3]").click()
        # 食品
        driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div[1]/div[5]/span[4]").click()
        time.sleep(1)
        # 珠宝
        driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div[1]/div[5]/span[5]").click()
        # 美鞋
        driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div[1]/div[5]/span[6]").click()
        # 化妆品
        driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div[1]/div[5]/span[7]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div[1]/div[5]/span[2]").click()
        time.sleep(1)
        driver.find_element_by_id("addmodeltemplate").click()
        driver.find_element_by_name("attributeName").send_keys("selenium001")
        driver.find_element_by_name("options[0].optionName").send_keys("0")
        driver.find_element_by_name("options[1].optionName").send_keys("1")
        driver.find_element_by_name("options[2].optionName").send_keys("2")
        driver.find_element_by_name("options[3].optionName").send_keys("3")
        driver.find_element_by_name("options[4].optionName").send_keys("4")
        # 保存按钮
        # driver.find_element_by_xpath("//*[@id='zdy']/form/p/a[2]").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text("模板列表").click()
        driver.find_element_by_xpath("//*[@id='contentDiv']/div[1]/div/a[1]").click()
        driver.find_element_by_xpath("//*[@id='edit']/form/table/tbody/tr/td[2]/input[9]").clear()
        driver.find_element_by_xpath("//*[@id='edit']/form/table/tbody/tr/td[2]/input[9]").send_keys("5")
        driver.find_element_by_xpath("//*[@id='edit']/form/p/a[2]").click()

    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()