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

        driver.find_element_by_partial_link_text("时间模板").click()
        time.sleep(2)
        # 选中默认时间
        if driver.find_element_by_id("default1").is_selected() == False:
            print driver.find_element_by_id("default1").is_selected()
            driver.find_element_by_id("default1").click()
            print driver.find_element_by_id("default1").is_selected()

        # 取消选择默认
        if driver.find_element_by_id("default1").is_selected():
            print driver.find_element_by_id("default1").is_selected()
            driver.find_element_by_id("default1").click()
            print driver.find_element_by_id("default1").is_selected()
            driver.find_element_by_id("exptype1").click()
            driver.find_element_by_xpath("//*[@id='deliveryTime']/div[4]/div[2]/table[2]/tbody/tr[1]/td[2]/input[2]").clear()
            driver.find_element_by_xpath("//*[@id='deliveryTime']/div[4]/div[2]/table[2]/tbody/tr[1]/td[2]/input[2]").send_keys("8")
            # js = "document.getElementByName('deliverStart').removeAttribute('readonly')"
            js = "$('input[name=deliverStart]').removeAttr('readonly')"
            driver.execute_script(js)

            driver.find_element_by_name("deliverStart").send_keys("20:00")
            js = "$('input[name=deliverEnd]').removeAttr('readonly')"
            driver.execute_script(js)
            driver.find_element_by_name("deliverEnd").send_keys("23:00")



        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='deliveryTime']/p/button").click()



        time.sleep(5)
    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()