# coding=utf-8
from framework.base_page import BasePage
from selenium.webdriver.support.select import Select

class Region(BasePage):
    # 查询条件

    add_frame = "addTemplete"
    # 添加配送模板
    template_name = "name=>templateName"

    # 按行政区配送
    district_area = "xpath=>//*[@id='tregionTemplate']/div/table/tbody/tr[1]/td/label[1]/input"

    # 按自定义区域
    custom_area = "xpath=>//*[@id='tregionTemplate']/div/table/tbody/tr[1]/td/label[2]/input"

    # 添加按钮
    add_area_btn = "id=>show-city"
    add_area_frame = "city"

    # --------------------------------

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    def click_add_area_btn(self):
        self.click(self.add_area_btn)

    def type_template_name(self, text):
        self.type(self.template_name, text)

    def add_area(self, province, city):
        self.click_add_area_btn()
        self.driver.switch_to.frame(self.add_area_frame)

        sel = self.driver.find_element_by_xpath("/html/body/contextpath/div/div[2]/div/select")
        Select(sel).select_by_visible_text(province)
        sel2 = self.driver.find_element_by_xpath("/html/body/contextpath/div/div[3]/div/select")
        Select(sel2).select_by_visible_text(city)
        self.driver.find_element_by_id("checkallarea").click()
        # 切换到上一个frame
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click()



