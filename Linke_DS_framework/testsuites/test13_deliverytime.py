# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_deliverytime import DeliveryTime
import pageobjects


class DeliveryTime1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_deliverytime001(self):
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
        dshomepage.click_menu("时间模板")
        time.sleep(1)
        deliverytime = DeliveryTime(self.driver)
        # 选中与取消默认配送设置
        deliverytime.select_default_dtime()
        time.sleep(1)
        deliverytime.cancel_default_dtime()

        # 选择可选配日期
        deliverytime.click_delivery_option1()
        deliverytime.click_which_day_start1(3)
        deliverytime.type_day_count(9)
        time.sleep(1)

        deliverytime.click_delivery_option2()
        deliverytime.click_which_day_start2(5)
        deliverytime.type_dayDate("2017-08-12")
        time.sleep(1)

        deliverytime.click_delivery_option3()
        deliverytime.type_start_expire("2017-07-15")
        deliverytime.type_end_expire("2017-08-30")
        time.sleep(1)

        deliverytime.select_buy_time_check()
        deliverytime.type_buy_time_check("20:35")
        time.sleep(1)
        deliverytime.cancel_buy_time_check()

        deliverytime.add_deliver_time("08:00", "12:35")
        deliverytime.click_add_time_btn()
        time.sleep(1)
        deliverytime.add_deliver_time("14:55", "19:00")
        deliverytime.click_add_time_btn()
        time.sleep(5)

        deliverytime.click_dtime_submit()





if __name__ == '__main__':
    unittest.main()