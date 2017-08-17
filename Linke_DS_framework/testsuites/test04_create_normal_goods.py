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


class Create_Normal_Goods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass
    def test_create_goods001(self):
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
        goodspage.click_menu("发布商品")

        # 选择商品类目
        goodspage.click_goods_category()

        # 选择商品类别
        goodspage.click_normal_goods_type()
        # 输入商品名称
        goodspage.type_goods_name(u"python自动创建普通商品"+ goodspage.now)
        # 输入商品编码
        goodspage.type_goods_code("goods_code")
        # 上传图片，选择图库第一张图片
        goodspage.click_goods_pic1()
        self.driver.switch_to.frame(goodspage.pic_frame)
        time.sleep(1)
        goodspage.click_menu("图库选择")
        time.sleep(1)
        goodspage.click_map_storage1()
        time.sleep(1)
        self.driver.switch_to_default_content()
        goodspage.click_map_storage_btn()

        # 输入商品描述
        goodspage.type_goods_remark(u"这里是商品描述")
        time.sleep(1)
        # 输入商品价格、库存
        goodspage.type_sales_price("111")
        goodspage.type_market_price("222")
        goodspage.type_stock_num("333")
        goodspage.type_shelf_no("444")
        time.sleep(1)

        # 配送方式
        goodspage.click_express_delivery()
        goodspage.click_delivery_fees()

        time.sleep(1)

        # 保存按钮
        # goodspage.click_goods_submit()



if __name__ == '__main__':
    unittest.main()