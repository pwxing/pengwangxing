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

    def test_CreateRegion(self):
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

        driver.find_element_by_partial_link_text("配送模板").click()
        driver.find_element_by_partial_link_text("添加配送区域").click()
        driver.switch_to.frame("addTemplete")
        driver.find_element_by_name("templateName").send_keys("Selenium01")

        driver.find_element_by_xpath("//*[@id='tregionTemplate']/div/table/tbody/tr[1]/td/label[2]/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='tregionTemplate']/div/table/tbody/tr[1]/td/label[1]/input").click()
        # 添加区域按钮
        driver.find_element_by_id("show-city").click()
        time.sleep(1)
        driver.switch_to.frame("city")
        sel = driver.find_element_by_id("province1")
        sel = driver.find_element_by_xpath("/html/body/contextpath/div/div[2]/div/select")

        Select(sel).select_by_visible_text("北京市")
        time.sleep(2)
        Select(sel).select_by_index("5")
        time.sleep(2)
        Select(sel).select_by_value("330000")
        sel2 = driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div/select")
        time.sleep(2)
        Select(sel2).select_by_index("3")
        time.sleep(1)
        driver.find_element_by_id("checkallarea").click()
        # 切换到上一个frame
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click()
        # driver.switch_to.frame("addTemplete")

        time.sleep(1)
        # 切换到主frame
        driver.switch_to.default_content()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click()
        time.sleep(1)

    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()