# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_basesetting import BaseSetting
import pageobjects


class Base_Setting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_baseSetting(self):
        # self.login()
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("htest","123456")
        time.sleep(1)
        # loginpage.get_windows_img()  # 调用基类截图方法
        # 点击电商按钮
        linkehomepage = LinkeHomePage(self.driver)
        time.sleep(1)
        linkehomepage.send_ds_link_btn()
        time.sleep(1)

        dshomepage = DSPage(self.driver)
        dshomepage.click_menu("基础设置")
        time.sleep(1)
        basesetting = BaseSetting(self.driver)
        basesetting.click_undelivered_non_refund()
        time.sleep(1)
        basesetting.click_undelivered_refund()

        basesetting.click_delivered_non_refund()
        time.sleep(1)
        basesetting.click_delivered_refund()

        basesetting.click_take_goods_non_refund()
        time.sleep(2)
        basesetting.click_take_goods_refund()
        basesetting.select_refund_num(4)

        basesetting.type_refund_remark("selenium001")
        basesetting.click_refund_time_btn()
        time.sleep(2)
        # 付款时间设置
        basesetting.type_pay_time_day(1)
        basesetting.type_pay_time_hour(2)
        basesetting.type_pay_time_min(3)
        basesetting.click_pay_time_submit()
        time.sleep(2)
        # 收货时间设置
        basesetting.type_take_time_day(4)
        basesetting.type_take_time_hour(5)
        basesetting.click_take_time_submit()


        # pagemanage.click_menu("自定义页面")
        # pagemanage.click_menu("主页")
        time.sleep(1)








if __name__ == '__main__':
    unittest.main()