# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_goodspromo import GoodsPromo
import pageobjects


class Goods_Promo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_goodsPromo(self):
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
        dshomepage.click_menu("商品促销")
        time.sleep(1)

        goodspromo = GoodsPromo(self.driver)

        goodspromo.click_menu("限购")
        goodspromo.click_menu("积分抵扣")
        goodspromo.click_menu("代金券抵扣")
        goodspromo.click_menu("满包邮设置")
        goodspromo.click_menu("推荐")
        time.sleep(1)
        goodspromo.click_keyword_type(2)
        goodspromo.type_input_keyword("ABC")
        goodspromo.click_query_btn()
        goodspromo.click_recommend_submit()









if __name__ == '__main__':
    unittest.main()