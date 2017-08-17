# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_pagemanage import PageManage
import pageobjects


class PageManage1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_pageManage001(self):
        u"""验证页面管理五个菜单是否正常 """
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
        dshomepage.click_menu("页面管理")
        time.sleep(1)
        pagemanage = PageManage(self.driver)
        pagemanage.click_menu("列表展示")
        pagemanage.assert_page_source(self, u"分类展示1")
        pagemanage.click_menu("加载页")
        pagemanage.assert_page_source(self, u"编辑加载页")
        pagemanage.click_menu("商品详情页")
        pagemanage.assert_page_source(self, u"标准模板")
        pagemanage.assert_page_source(self, u"简化模板")
        pagemanage.click_menu("自定义页面")
        pagemanage.assert_page_source(self, u"自定义列表")
        pagemanage.click_menu("主页")
        pagemanage.assert_page_source(self, u"自定义模板")
        time.sleep(1)

    def test_pageManage002(self):
        u"""主页"""
        # 点击主题的图片一至五
        pagemanage = PageManage(self.driver)
        time.sleep(1)
        pagemanage.click_theme_img(2)

        # 列表展示
        # 获取点击状态


    def test_pageManage003(self):
        u"""列表展示"""
        # 点击主题的图片一至五
        pagemanage = PageManage(self.driver)
        pagemanage.click_menu("列表展示")
        time.sleep(1)
        # pagemanage.cancel_show_img("1")
        pagemanage.click_show_img(3)
        pagemanage.click_default_show_img(5)

        # # 保存按钮
        pagemanage.click_list_submit()

    def test_pageManage004(self):
        u"""加载页"""
        pagemanage = PageManage(self.driver)
        pagemanage.click_menu("加载页")
        # time.sleep(1)
        pagemanage.click_editor_load_page()
        pagemanage.click_img_load_page()
        # time.sleep(1)

        pagemanage.click_switch_btn()
        # time.sleep(3)
        # pagemanage.click_switch_btn()
        #
        pagemanage.click_load_page_submit()
        time.sleep(4)

    def test_pageManage005(self):
        u"""商品详情页"""
        pagemanage = PageManage(self.driver)
        pagemanage.click_menu("商品详情页")
        time.sleep(1)
        pagemanage.click_simple_mode()
        time.sleep(1)
        pagemanage.click_stardard_mode()
        time.sleep(1)
        pagemanage.click_goods_mode_submit()

    def test_pageManage006(self):
        u"""自定义页面"""
        pagemanage = PageManage(self.driver)
        pagemanage.click_menu("自定义页面")
        # pagemanage.type_cus_title("selenium001")
        # pagemanage.type_cus_remark(u"这里是描述")
        # time.sleep(1)
        # pagemanage.click_cus_submit()
        # time.sleep(1)
        # pagemanage.click_cus_delete()
        # time.sleep(1)
        # pagemanage.click_cus_release_btn()







if __name__ == '__main__':
    unittest.main()