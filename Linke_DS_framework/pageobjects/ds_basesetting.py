# coding=utf-8
from framework.base_page import BasePage


class BaseSetting(BasePage):
    # 退款申请时效设置
    # undelivered_refund = "css=>input[name='undeliverStatus'][value='0']"
    # undelivered_non_refund = "css=>input[name='undeliverStatus'][value='1']"
    undelivered_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/label[1]/input"
    undelivered_non_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/label[2]/input"
    # delivered_refund = "c=>input[name='confirmDeliverStatus'][value='0']"
    # delivered_non_refund = "c=>input[name='confirmDeliverStatus'][value='1']"
    delivered_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/label[1]/input"
    delivered_non_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/label[2]/input"
    # take_goods_refund = "c=>input[name='finishStatus'][value='0']"
    # take_goods_non_refund = "c=>input[name='finishStatus'][value='1']"
    take_goods_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/label[1]/input"
    take_goods_non_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/label[2]/input"

    refund_remark = "name=>remark"
    refund_time_btn = "id=>saveButton"

    # 付款时间设置
    pay_time_day = "xpath=>//*[@id='limitedType1']/input[1]"
    pay_time_hour = "xpath=>//*[@id='limitedType1']/input[2]"
    pay_time_min = "xpath=>//*[@id='limitedType1']/input[3]"
    pay_time_submit = "id=>limitedType1-save"

    # 收货时间设置
    take_time_day = "xpath=>//*[@id='limitedType2']/input[1]"
    take_time_hour = "xpath=>//*[@id='limitedType2']/input[2]"
    take_time_submit = "id=>limitedType2-save"

    # ----------------退款时效设置-----------------

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    def click_undelivered_refund(self):
        self.click(self.undelivered_refund)

    def click_undelivered_non_refund(self):
        self.click(self.undelivered_non_refund)

    def click_delivered_refund(self):
        self.click(self.delivered_refund)

    def click_delivered_non_refund(self):
        self.click(self.delivered_non_refund)

    def click_take_goods_refund(self):
        self.click(self.take_goods_refund)

    def click_take_goods_non_refund(self):
        self.click(self.take_goods_non_refund)

    def select_refund_num(self, text):
        self.click("xpath=>//*[@name='finishDay']/option[" + str(text) + "]")

    def type_refund_remark(self, text):
        self.type(self.refund_remark, text)

    def click_refund_time_btn(self):
        self.click(self.refund_time_btn)

    # ----------------------付款时间设置---------------------
    def type_pay_time_day(self, text):
        self.type(self.pay_time_day, text)

    def type_pay_time_hour(self, text):
        self.type(self.pay_time_hour, text)

    def type_pay_time_min(self, text):
        self.type(self.pay_time_min, text)

    def click_pay_time_submit(self):
        self.click(self.pay_time_submit)

    # -------------------收货时间设置----------------------------
    def type_take_time_day(self, text):
        self.type(self.take_time_day, text)

    def type_take_time_hour(self, text):
        self.type(self.take_time_hour, text)

    def click_take_time_submit(self):
        self.click(self.take_time_submit)