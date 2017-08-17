# coding=utf-8
from framework.base_page import BasePage


class BuyManage(BasePage):
    # 查询条件
    # undelivered_refund = "css=>input[name='undeliverStatus'][value='0']"
    # undelivered_non_refund = "css=>input[name='undeliverStatus'][value='1']"
    nick_name = "name=>nick"
    order_status = "name=>status"

    createTimeBegin = "name=>createTimeBeginStr"
    createTimeEnd = "name=>createTimeEndStr"
    # take_goods_refund = "c=>input[name='finishStatus'][value='0']"
    # take_goods_non_refund = "c=>input[name='finishStatus'][value='1']"
    take_goods_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/label[1]/input"
    take_goods_non_refund = "xpath=>//*[@id='refundSettingForm']/table/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/label[2]/input"

    refund_remark = "name=>remark"
    refund_time_btn = "id=>saveButton"

    order_frame = "kfgmsj"
    order_detail_btn = "s=>a.g-btn.g-btn-init"

    # --------------------------------

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    def type_nick_name(self, text):
        self.type(self.nick_name, text)

    # 1全部 2待付款 3商家取消 4待发货
    def select_order_status(self, text):
        self.click("xpath=>//*[@name='status']/option[" + str(text) + "]")

    def type_create_time_begin(self, text):
        js = "$('input[name=createTimeBeginStr]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.driver.find_element_by_name("createTimeBeginStr").send_keys(text)

    def type_create_time_end(self, text):
        js = "$('input[name=createTimeEndStr]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.driver.find_element_by_name("createTimeEndStr").send_keys(text)

    def click_order_detail_btn(self):
        self.click(self.order_detail_btn)

