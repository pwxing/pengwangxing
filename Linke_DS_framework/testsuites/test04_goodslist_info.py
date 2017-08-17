# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_goodspage import GoodsPage
import pageobjects


class GoodsListInfoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_goodslist_info001(self):
        # self.login()
        loginpage = LoginPage(self.driver)
        loginpage.login()
        time.sleep(1)
        # loginpage.get_windows_img()  # 调用基类截图方法
        # 点击电商按钮
        linkehomepage = LinkeHomePage(self.driver)
        time.sleep(1)
        linkehomepage.send_ds_link_btn()
        time.sleep(1)

        dshomepage = DSPage(self.driver)
        dshomepage.click_menu("商品管理")
        time.sleep(1)
        goodspage = GoodsPage(self.driver)
        goodspage.click_menu("商品列表")
        time.sleep(1)

    def test_goodslist_info002(self):
        goodspage = GoodsPage(self.driver)
        # print goodspage.get_goods_list_name()
        # print self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/table/tbody/tr[1]/td[3]/p").text
        # print self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/table/tbody/tr[1]/td[3]/b").text()

        # print self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/table/tbody/tr[1]/td[4]").text
        # print self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div/table/tbody/tr/td[4]").text

        goodspage.print_goods_info_by_index(5)
        # goods_info_list = self.driver.find_elements_by_class_name("info")
        time.sleep(1)
        # goods_info_list = self.driver.find_elements_by_css_selector(".info")
     
        # print "abc",len(goods_stock_list)
        # print "abc", len(goods_info_list)
        # print goods_info_list[1]
        # print "xxx"
        # print goods_info_list[2].text

        # for i in goods_info_list:
        #     print i.text

if __name__ == '__main__':
    unittest.main()