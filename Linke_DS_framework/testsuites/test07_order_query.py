# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_orderpage import OrderPage
import pageobjects


class OrderQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_orderQuery(self):
        # self.login()
        loginpage = LoginPage(self.driver)
        loginpage.login()
        time.sleep(2)
        # loginpage.get_windows_img()  # 调用基类截图方法
        # 点击电商按钮
        linkehomepage = LinkeHomePage(self.driver)
        time.sleep(1)
        linkehomepage.send_ds_link_btn()
        time.sleep(1)

        dshomepage = DSPage(self.driver)
        dshomepage.click_menu("订单管理")
        time.sleep(1)
        orderpage = OrderPage(self.driver)
        orderpage.click_menu("交易统计")
        orderpage.click_menu("订单统计")
        orderpage.click_menu("订单列表")

        time.sleep(1)
        # 输入时间
        orderpage.type_pay_time_begin("2015-07-18 11:35")
        orderpage.type_pay_time_end("2017-07-18 11:35")
        orderpage.type_create_time_begin("2015-07-18 11:35")
        orderpage.type_create_time_end("2017-07-18 11:35")
        # self.driver.find_element_by_id("payTimeBegin").send_keys("2015-07-18 11:35")
        # self.driver.find_element_by_id("payTimeEnd").send_keys("2017-07-18 11:35")
        # self.driver.find_element_by_id("createTimeBegin").send_keys("2015-07-18 11:35")
        # self.driver.find_element_by_id("createTimeEnd").send_keys("2017-07-18 11:35")

        orderpage.click_query()
        # 输入到店门店，所属门店
        # orderpage.type_take_store(u"htest总店")
        # orderpage.click_query()

        # time.sleep(5)
        # orderpage.type_belong_store(u"深圳分店")

        # 输入订单号、交易编号、收货电话、收货姓名 买家昵称
        orderpage.type_order_no("201706100000037")
        orderpage.type_transaction_no("400100254788")
        orderpage.type_take_phone("13538008900")
        orderpage.type_take_name(u"彭望兴")
        orderpage.type_nick_name(u"望星")

        # 查询订单状态
        orderpage.click_status(3)
        time.sleep(2)
        # 查询订单类型
        orderpage.click_order_type(4)
        # 查询支付方式
        orderpage.click_pay_way(5)
        # 查询配送方式
        orderpage.click_delivery_type(4)
        # time.sleep(3)
        time.sleep(1)
        # 遍历订单TAB
        # orderpage.click_orders()
        # 商品类别
        orderpage.click_goods_type(3)
        orderpage.click_goods_type2(2)

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()