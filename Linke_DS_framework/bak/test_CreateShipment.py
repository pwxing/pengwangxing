#coding=utf-8
from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ssotest.ematong.com/cas/login?service=http://bmtest.ematong.com/shiro-cas"

    def test_CreateShipment(self):
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

        driver.find_element_by_partial_link_text("运费模板").click()
        driver.find_element_by_partial_link_text("添加运费模板").click()
        driver.switch_to.frame("addTemplete")
        driver.find_element_by_name("templateName").send_keys("Selenium01")
        # 按重量计费
        # driver.find_element_by_name("billing").find_element_by_xpath("//option[@value='2']").click()
        driver.find_element_by_xpath("//*[@id='shipmentTemplate']/div/table/tbody/tr[3]/td/label[2]/input").click()
        time.sleep(2)
        # 按件计费
        # driver.find_element_by_name("billing").find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_xpath("//*[@id='shipmentTemplate']/div/table/tbody/tr[3]/td/label[1]/input").click()
        time.sleep(1)
        # 首件
        driver.find_element_by_id("first").send_keys("1")
        # 首费
        driver.find_element_by_xpath("//*[@id='shipmentTemplate']/div/div[3]/div[2]/table[1]/tbody/tr/td/input[2]").send_keys("5")
        # 续件
        driver.find_element_by_id("append").send_keys("3")
        # 续费
        driver.find_element_by_xpath("//*[@id='shipmentTemplate']/div/div[3]/div[2]/table[1]/tbody/tr/td/input[4]").send_keys("8")
        driver.switch_to.default_content()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click()
        time.sleep(3)

    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()