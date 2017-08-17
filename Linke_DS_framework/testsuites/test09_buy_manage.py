# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_buymanage import BuyManage
import pageobjects


class Buy_Manage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_pageManage(self):
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
        dshomepage.click_menu("客户管理")
        time.sleep(1)
        buymanage = BuyManage(self.driver)
        buymanage.type_nick_name("pwx")
        buymanage.select_order_status(1)
        buymanage.type_create_time_begin("2015-01-23 16:25")
        buymanage.type_create_time_end("2017-07-03 16:25")
        buymanage.click_menu("搜索")
        buymanage.click_menu("查看")
        time.sleep(1)
        self.driver.switch_to.frame(BuyManage.order_frame)
        time.sleep(1)
        self.driver.switch_to.parent_frame()
        # driver.switch_to.default_content()
        # print driver.page_source
        assert u'pwx的购买数据' in self.driver.page_source
        time.sleep(1)
        # driver.find_element_by_xpath("/html/body/div[3]/div[2]/a").click()
        buymanage.click_order_detail_btn()




if __name__ == '__main__':
    unittest.main()