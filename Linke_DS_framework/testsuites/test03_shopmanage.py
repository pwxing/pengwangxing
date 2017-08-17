# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_shopmanage import ShopManage
import pageobjects


class ShopManageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_ds_menu001(self):
        # self.login()
        loginpage = LoginPage(self.driver)
        loginpage.login()
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        # 点击电商按钮
        linkehomepage = LinkeHomePage(self.driver)
        time.sleep(1)
        linkehomepage.send_ds_link_btn()
        time.sleep(1)

        shopmanage = ShopManage(self.driver)
        print shopmanage.get_y_order_text()
        print shopmanage.get_y_amount_text()
        print shopmanage.get_no_send_text()
        print shopmanage.get_prepare_goods_text()
        print shopmanage.get_refund_text()
        shopmanage.click_y_order()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        shopmanage.click_ds_info()
        time.sleep(1)
        shopmanage.click_ds_info()

        # 查询时间
        shopmanage.type_select_query_time(u"近一周")
        time.sleep(2)
        shopmanage.type_select_query_time(u"近一月")
        time.sleep(2)
        shopmanage.type_select_query_time(u"昨天")
        time.sleep(2)
        shopmanage.type_select_query_time(u"自定义时间")
        time.sleep(2)
        shopmanage.type_cus_time("2017-07-20", "2017-07-25")
        time.sleep(1)
        shopmanage.click_query_btn()
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()