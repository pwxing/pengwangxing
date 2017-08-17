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

    def test_createGoods(self):
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
        driver.find_element_by_partial_link_text("商品管理").click()
        driver.find_element_by_partial_link_text("发布商品").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='category1']/p[2]").click()
        driver.find_element_by_xpath("//*[@id='category2']/p[1]").click()
        driver.find_element_by_xpath("//*[@id='category3']/p[3]").click()
        # select = driver.find_element_by_id("selectGoodsType1")
        driver.find_element_by_id("selectGoodsType1").find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_id("add_goodsname").send_keys("Selenium_python001")
        driver.find_element_by_id("add_goodsCode").send_keys("11111")
        driver.find_element_by_id("add_remark").send_keys("22222")
        driver.find_element_by_xpath("//*[@id='upload_ls']/dd[1]/div[1]/img[2]").click()
        driver.implicitly_wait(10)
        # driver.switch_to_window("上传图片")
        driver.switch_to_frame("_uploadPic_iframe")
        driver.find_element_by_partial_link_text("图库选择").click()
        driver.implicitly_wait(10)
        # 图库的确定按钮
        driver.find_element_by_xpath("//*[@id='upload-list']/div[3]/div[1]/img").click()
        driver.switch_to_default_content()
        driver.implicitly_wait(10)

        driver.find_element_by_xpath("/html/body/div[4]/div[2]/a[1]").click()
        driver.find_element_by_xpath("//*[@id='ejsxTb2']/tbody/tr/td[1]/input").send_keys("111")
        driver.find_element_by_xpath("//*[@id='ejsxTb2']/tbody/tr/td[4]/input").send_keys("333")

        # 配送方式
        # driver.execute_script("window.scrollBy(0，400)", "")
        time.sleep(2)
        print "123"
        # driver.execute_script("window.scrollBy(0，document.body.scrollHeight)","")
        driver.find_element_by_name("expressDeliverys[0].deliveryType").click()
        print "456"
        # driver.find_element_by_xpath("//*[@id='page_block_4']/div[4]/table[2]/tbody[1]/tr/td/label/input").click()

        driver.find_element_by_xpath("//*[@id='page_block_4']/div[4]/table[2]/tbody[2]/tr[1]/td[3]/label/input").click()
        time.sleep(2)
        # 商品保存按钮
        driver.find_element_by_id("submitBtn").click()
        time.sleep(5)

        # self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()