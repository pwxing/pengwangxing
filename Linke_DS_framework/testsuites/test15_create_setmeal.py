# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.act_setmeal import Setmeal
import pageobjects


class ActSetMeal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_create_setmeal001(self):
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
        dshomepage.click_menu("优惠套餐")
        time.sleep(1)
        actsetmeal = Setmeal(self.driver)

        # 输入活动名称
        actsetmeal.type_act_title(u"python自建套餐活动"+actsetmeal.now)
        time.sleep(1)
        # actsetmeal.type_act_remark(u"这里是备注")
        actsetmeal.type_act_time("2017-08-12 01:23:45", "2018-12-30 23:59:59")
        actsetmeal.click_discount_type(2)
        actsetmeal.type_discount_goods_num(1)
        actsetmeal.type_discount_price("50")
        actsetmeal.click_add_discount_btn()
        time.sleep(1)
        actsetmeal.click_minus_discount_btn()
        time.sleep(1)
        actsetmeal.click_delivery_fee(2)
        # 活动显示
        actsetmeal.select_act_square_show(2)
        time.sleep(1)

        # --------------添加主商品
        actsetmeal.click_add_main_goods_btn()
        time.sleep(1)
        self.driver.switch_to.frame(actsetmeal.add_goods_frame)
        actsetmeal.click_goods_type(2)
        actsetmeal.type_goods_name(u"现代风格")
        actsetmeal.click_status(3)
        actsetmeal.choose_goods_join(1)
        actsetmeal.click_query_btn()

        # actsetmeal.choose_goods_index(2)
        time.sleep(1)
        actsetmeal.click_choose_goods()
        time.sleep(1)
        # actsetmeal.choose_goods_id("e70ff346-0bcc-4bad-8ff3-460bcc7bade3")
        self.driver.switch_to_default_content()
        time.sleep(1)
        actsetmeal.click_choose_goods_btn()

        time.sleep(1)
        # 添加搭配商品
        actsetmeal.click_add_other_goods_btn()
        self.driver.switch_to.frame(actsetmeal.add_goods_frame)
        time.sleep(1)
        actsetmeal.type_goods_name(u"台灯")
        actsetmeal.click_query_btn()
        actsetmeal.choose_goods_id("6ec316c4-67ae-4dec-8316-c467ae4deca6")
        time.sleep(1)
        self.driver.switch_to_default_content()
        time.sleep(1)
        actsetmeal.click_choose_goods_btn()

if __name__ == '__main__':
    unittest.main()