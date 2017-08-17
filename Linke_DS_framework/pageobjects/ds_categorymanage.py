# coding=utf-8
from framework.base_page import BasePage


class CategoryManage(BasePage):
    # 展开第N个一级分类
    def click_category1_by_index(self, index):
        self.click("xpath=>//*[@id='saveForm']/table/tbody["+str(index)+"]/tr[1]/td[1]/img[1]")
    # 点击一级分类的按钮，第一个参数row是第N个分类，第二个参数column是操作类型：1顶、2向上一级、3向下一级、4尾
    def click_one_sort(self, first, mode):
        self.click("xpath=>//*[@id='saveForm']/table/tbody["+str(first)+ \
                   "]/tr[1]/td[2]/img["+str(mode)+")]")

    def click_two_sort(self, first, two, mode):
        self.click("xpath=>//*[@id='saveForm']/table/tbody["+str(first)+ \
        "]/tr["+str(two+2)+"]/td/table/tbody/tr[1]/td[2]/img["+str(mode)+")]")

    def click_three_sort(self, first, two, three, mode):
        self.click("xpath=>//*[@id='saveForm']/table/tbody["+str(first)+ \
        "]/tr["+str(two+2)+"]/td/table/tbody/tr["+str(three+2)+"]/td[2]/img["+str(mode)+")]")


