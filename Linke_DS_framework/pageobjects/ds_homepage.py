# coding=utf-8
from framework.base_page import BasePage


class DSPage(BasePage):

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

