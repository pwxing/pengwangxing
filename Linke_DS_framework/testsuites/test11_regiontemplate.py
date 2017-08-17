# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_regiontemplate import Region
import pageobjects


class RegionTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_shipment(self):
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
        dshomepage.click_menu("配送模板")
        time.sleep(1)
        regiontemplate = Region(self.driver)
        regiontemplate.click_menu("添加配送区域")
        self.driver.switch_to.frame(Region.add_frame)
        regiontemplate.type_template_name("selenium0706")
        regiontemplate.add_area(u"江西省", u"九江市")
        # 切换到主frame
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click()












if __name__ == '__main__':
    unittest.main()