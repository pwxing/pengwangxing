# coding=utf-8
from framework.base_page import BasePage


class LinkeHomePage(BasePage):
    input_username = "id=>user2"
    input_password = "id=>password2"
    search_submit_btn = "id=>submit2"
    ds_link_btn = "xpath=>/html/body/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/a"

    login_username = "id=>user2"
    login_password = "id=>password2"
    login_submit = "id=>submit2"
    linke_homepage_dslink = "xpath=>/html/body/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/a"

    def type_username(self, text):
        self.type(self.input_username, text)

    def type_password(self, text):
        self.type(self.input_password, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def send_ds_link_btn(self):
        self.click(self.ds_link_btn)

