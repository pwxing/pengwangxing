# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
import pageobjects


class DS_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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

        dshomepage = DSPage(self.driver)

        menulists = ['商品管理', '分类管理', '页面管理', '订单管理', '商品促销', '优惠套餐', '满立减', \
                    '预售', '限时特价', '抱团购', '代金券', '秒杀', '许愿', '送礼', '客户管理', \
                    '运费模板', '配送模板', '属性模板', '时间模板', '基础设置']
        menu_assert_info_list = [u'导出商品列表', u'保存分类', u'自定义页面', u'打印发货单', u'满包邮设置', \
                                 u'套餐搭配将在主商品的详情页显示', u'多级优惠每级优惠不累计叠加', \
                                 u'预售商品只支持线上付款，同时不能参加其他预售',u'限时特价可以增强商城人气', \
                                 u'用户分享至朋友圈三五抱团即可享受优惠', u'一个卡券只能同时参与一个进行中的活动', \
                                 u'商家可通过秒杀引导用户在商城浏览促进销售转化', u'谁帮我实现愿望，我就', \
                                 u'朋友来填写收货地址收礼', u'客户购买数据', \
                                 u'添加运费模板', u'添加配送区域', u'属性选项', u'用户到店时间', \
                                 u'退款申请时效设置', u'成交金额统计']
        for i in range(1, len(menulists) + 1):
            dshomepage.click_menu(menulists[i-1])
            time.sleep(1)
            dshomepage.assert_page_source(self, menu_assert_info_list[i-1])

if __name__ == '__main__':
    unittest.main()