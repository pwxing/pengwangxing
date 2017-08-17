# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    input_username = "id=>user2"
    input_password = "id=>password2"
    verification_code = "id=>yzm2"
    login_submit_btn = "id=>submit2"

    def type_username(self, text):
        self.type(self.input_username, text)

    def type_password(self, text):
        self.type(self.input_password, text)

    def send_submit_btn(self):
        self.click(self.login_submit_btn)

    def linke_login(self, username, password, code):
        self.type(self.input_username, username)
        self.type(self.input_password, password)
        self.type(self.verification_code, code)
        self.click(self.login_submit_btn)

    def login(self):
        self.type(self.input_username, "htest")
        self.type(self.input_password, "123456")
        self.type(self.verification_code, "HY7102$")
        self.click(self.login_submit_btn)

    logout_btn = "xpath=>//*[@id='headerLogout']"

    def logout(self):
        self.click(self.logout_btn)

