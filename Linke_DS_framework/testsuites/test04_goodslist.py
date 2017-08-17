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


class GoodsListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass
    def test_goodslist001(self):
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

    def test_goodslist002(self):
        goodspage = GoodsPage(self.driver)
        print goodspage.get_unonline_text()
        print goodspage.get_online_text()
        print goodspage.get_sale_out_text()
        print goodspage.get_off_line_text()

        # 输入门店名称
        goodspage.type_store_select(u"测试同步")

        # 输入搜索方式
        goodspage.type_goods_attr_select(u"商品价")
        goodspage.type_goods_attr_text("50")

        time.sleep(1)
        goodspage.type_one_category(u"本地生活")
        goodspage.type_two_category(u"卡券消费")
        goodspage.type_three_category(u"水果蔬菜礼品卡")
        goodspage.type_query_goods_type(u"实体商品")

        # self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/div[6]/div/div[1]/a").click()
        # 查询按钮，1是加盟，0是直营
        goodspage.click_query_btn(0)

        # 保存按钮
        # goodspage.click_goods_submit()
    def test_goodslist003(self):
        u"""删除商品列表中的第N个商品"""
        goodspage = GoodsPage(self.driver)
        editlist = self.driver.find_elements_by_partial_link_text("编辑")
        editlist[2].click()
        self.driver.back()

    def test_goodslist004(self):
        u"""查看商品列表中的第N个商品"""
        goodspage = GoodsPage(self.driver)
        editlist = self.driver.find_elements_by_partial_link_text("查看")
        editlist[3].click()
        self.driver.back()
        time.sleep(1)

    def test_goodslist005(self):
        u"""下架商品列表中的第N个商品"""
        goodspage = GoodsPage(self.driver)
        editlist = self.driver.find_elements_by_partial_link_text("下架")
        editlist[5].click()
        # goodspage.click_off_line_submit_btn()
        goodspage.click_off_line_cancel_btn()
        time.sleep(1)

    def test_goodslist006(self):
        u"""在商品列表中移入未上架第N个商品"""
        goodspage = GoodsPage(self.driver)
        editlist = self.driver.find_elements_by_partial_link_text("移入未上架")
        print len(editlist)
        editlist[5].click()
        time.sleep(3)
        goodspage.click_off_line_cancel_btn()
        time.sleep(2)

    def test_goodslist007(self):
        u"""删除商品列表中的第N个商品"""
        goodspage = GoodsPage(self.driver)
        editlist = self.driver.find_elements_by_partial_link_text("删除")
        print len(editlist)
        editlist[5].click()
        time.sleep(3)
        goodspage.click_off_line_cancel_btn()
        time.sleep(2)

    def test_goodslist008(self):
        u"""复制商品列表中第N个商品"""
        goodspage = GoodsPage(self.driver)
        editlist = self.driver.find_elements_by_partial_link_text("复制")
        print len(editlist)
        editlist[5].click()
        time.sleep(3)

    def test_goodslist009(self):
        u"""导出商品列表"""
        goodspage = GoodsPage(self.driver)
        # editlist = self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/div[7]/label/input")
        # self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/div[7]/label/input").click()
        goodspage.click_all_goods_current_page_btn()
        self.driver.find_element_by_partial_link_text("导出商品列表").click()
        time.sleep(3)
        goodspage.cancel_all_goods_current_page_btn()

    def test_goodslist0010(self):
        u"""导出价格/库存"""
        goodspage = GoodsPage(self.driver)
        # editlist = self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/div[7]/label/input")
        # self.driver.find_element_by_xpath("//*[@id='queryForm']/div/div[1]/div[7]/label/input").click()
        goodspage.click_all_goods_current_page_btn()
        self.driver.find_element_by_partial_link_text("导出价格/库存").click()
        time.sleep(1)
        goodspage.cancel_all_goods_current_page_btn()


if __name__ == '__main__':
    unittest.main()