# coding=utf-8
from framework.base_page import BasePage
from selenium.webdriver.support.select import Select


class DeliveryTime(BasePage):
    # 商家配送时间 ------------------ Merchant distribution
    # 默认时间
    default_delivery_setting = "id=>default1"

    def select_default_dtime(self):
        self.select_checkbox(self.default_delivery_setting)

    def cancel_default_dtime(self):
        self.cancel_checkbox(self.default_delivery_setting)

    # 购买起X天有效-------------
    delivery_option1 = "id=>exptype1"
    which_day_start1 = "id=>beforegd1"
    # 选择哪天起，1为当天，2为第二天，以此类推最多七天

    def click_delivery_option1(self):
        self.click(self.delivery_option1)

    def click_which_day_start1(self, text):
        self.click("xpath=>//*[@id='beforegd1']/option[" + str(text) + "]")

    day_count = "name=>dayCount"

    def type_day_count(self, text):
        self.type(self.day_count, text)

    # 购买起到XX日期有效
    delivery_option2 = "id=>exptype2"
    which_day_start2 = "id=>beforegd2"
    dayDate ="name=>dayDate"

    def click_delivery_option2(self):
        self.click(self.delivery_option2)

    def click_which_day_start2(self, text):
        self.click("xpath=>//*[@id='beforegd2']/option[" + str(text) + "]")

    def type_dayDate(self, text):
        js = "$('input[name=dayDate]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.dayDate, text)

    # 从哪天到哪天配送
    delivery_option3 = "id=>exptype3"
    start_expire = "id=>startexpire"
    end_expire = "id=>endexpire"

    def click_delivery_option3(self):
        self.click(self.delivery_option3)

    def type_start_expire(self, text):
        js = "$('input[id=startexpire]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.start_expire, text)

    def type_end_expire(self, text):
        js = "$('input[id=endexpire]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.end_expire, text)

    # 购买XX时间后，延至第二天配送
    buy_time_check = "id=>buytime-check"
    buy_time ="name=>buyTime"

    def select_buy_time_check(self):
        self.select_checkbox(self.buy_time_check)

    def cancel_buy_time_check(self):
        self.cancel_checkbox(self.buy_time_check)

    # 输入时间如 19:30
    def type_buy_time_check(self, text):
        js = "$('input[name=buyTime]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.buy_time, text)

    # 可配送时间
    deliver_start = "name=>deliverStart"
    deliver_end = "name=>deliverEnd"
    add_time_btn = "id=>addTime1"

    def add_deliver_time(self,start_time, end_time ):
        js = "$('input[name=deliverStart]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.deliver_start, start_time)

        js = "$('input[name=deliverEnd]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.deliver_end, end_time)

    def click_add_time_btn(self):
        self.click(self.add_time_btn)

    # 总保存按钮
    dtime_submit = "xpath=>//*[@id='deliveryTime']/p/button"

    def click_dtime_submit(self):
        self.click(self.dtime_submit)

    def click_menu(self, loc):
        self.click_partial_link_text(loc)





