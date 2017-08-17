# coding=utf-8
from framework.base_page import BasePage
from selenium.webdriver.support.select import Select


class AttributePage(BasePage):
    # 添加模板
    custom_menu = "xpath=>/html/body/contextpath/div/div[3]/div[1]/div[5]/span[2]"
    clothes_menu = "xpath=>/html/body/contextpath/div/div[3]/div[1]/div[5]/span[3]"
    food_menu = "xpath=>/html/body/contextpath/div/div[3]/div[1]/div[5]/span[4]"
    jewelry_menu = "xpath=>/html/body/contextpath/div/div[3]/div[1]/div[5]/span[5]"
    shoe_menu = "xpath=>/html/body/contextpath/div/div[3]/div[1]/div[5]/span[6]"
    cosmetic_menu = "xpath=>/html/body/contextpath/div/div[3]/div[1]/div[5]/span[7]"
    add_attr_btn = "id=>addmodeltemplate"

    def click_custom_menu(self):
        self.click(self.custom_menu)

    def click_clothes_menu(self):
        self.click(self.clothes_menu)

    def click_food_menu(self):
        self.click(self.food_menu)

    def click_jewelry_menu(self):
        self.click(self.jewelry_menu)

    def click_shoe_menu(self):
        self.click(self.shoe_menu)

    def click_cosmetic_menu(self):
        self.click(self.cosmetic_menu)

    def click_add_attr_btn(self):
        self.click(self.add_attr_btn)
    # 属性名
    attribute_name = "name=>attributeName"

    def type_attribute_name(self, text):
        self.type(self.attribute_name, text)
    # 属性选项

    def type_attr_option(self, index, text):
        add_attr_option_loc = "xpath=>//*[@id='zdy']/form/table/tbody/tr/td[2]/input[" + str(index) + "]"
        # self.driver.find_element_by_x("options[" + index + "].optionName").send_keys(text)
        self.type(add_attr_option_loc, text)

    # 添加属性的保存按钮
    add_attr_submit = "xpath=>//*[@id='zdy']/form/p/a[2]"

    def click_add_attr_submit(self):
        self.click(self.add_attr_submit)
    # 模板列表
    # 第N个编辑按钮
    def click_edit_attr_btn(self, index):
        self.click("xpath=>//*[@id='contentDiv']/div[" + str(index) + "]/div/a[1]")

    def click_delete_attr_btn(self, index):
        self.click("xpath=>//*[@id='contentDiv']/div[" + index + "]/div/a[2]")

    def type_edit_attr(self, index, text):
        i = index*2 - 1
        self.clear("xpath=>//*[@id='edit']/form/table/tbody/tr/td[2]/input[" + str(i) + "]")
        self.type("xpath=>//*[@id='edit']/form/table/tbody/tr/td[2]/input[" + str(i) + "]", text)

    edit_attr_submit = "xpath=>//*[@id='edit']/form/p/a[2]"

    def click_edit_attr_submit(self):
        self.click(self.edit_attr_submit)

    def click_menu(self, loc):
        self.click_partial_link_text(loc)





