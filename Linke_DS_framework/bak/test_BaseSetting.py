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

    def test_BaseSetting(self):
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

        driver.find_element_by_partial_link_text("基础设置").click()
        time.sleep(1)
        # 未发货
        lists = driver.find_elements_by_name("undeliverStatus")
        for list in lists:
            list.click()
            time.sleep(2)

        # 已发货
        # driver.find_element_by_name("confirmDeliverStatus").find_element_by_xpath("//option[@value='0']").click()
        driver.find_element_by_css_selector("input[name='confirmDeliverStatus'][value='0']").click()
        time.sleep(2)
        driver.find_element_by_css_selector("input[name='confirmDeliverStatus'][value='1']").click()
        time.sleep(2)

        # 已完成
        driver.find_element_by_css_selector("input[name='finishStatus'][value='0']").click()
        time.sleep(2)
        driver.find_element_by_css_selector("input[name='finishStatus'][value='1']").click()
        time.sleep(2)
        sel = driver.find_element_by_name("finishDay")
        Select(sel).select_by_value("5")
        time.sleep(2)

        # 退款说明
        driver.find_element_by_name("remark").clear()
        driver.find_element_by_name("remark").send_keys(u"这里是Selenium自动生成退款说明")
        time.sleep(2)
        driver.find_element_by_partial_link_text("保存退款申请时效设置").click()
        time.sleep(2)





    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()