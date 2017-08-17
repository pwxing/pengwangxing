# coding=utf-8
from framework.base_page import BasePage


class ShopManage(BasePage):
    # 昨日订单
    y_order_link = "xpath=>/html/body/contextpath/div/div[3]/div[1]/div[1]/table/tbody/tr/td[1]/a"
    y_order = "id=>y_order"

    def click_y_order(self):
        self.click(self.y_order)

    def get_y_order_text(self):
        return self.get_element_text(self.y_order)

    # 昨天销售额
    y_amount = "id=>y_amount"

    def click_y_amount(self):
        self.click(self.y_amount)

    def get_y_amount_text(self):
        return self.get_element_text(self.y_amount)
    # 未发货
    no_send = "id=>y_nosend"

    def click_no_send(self):
        self.click(self.no_send)

    def get_no_send_text(self):
        return self.get_element_text(self.no_send)
    # 待备货
    prepare_goods = "id=>y_wait"

    def click_prepare_goods(self):
        self.click(self.prepare_goods)

    def get_prepare_goods_text(self):
        return self.get_element_text(self.prepare_goods)
    # 待退货
    refund = "id=>y_refund"

    def click_refund(self):
        self.click(self.refund)

    def get_refund_text(self):
        return self.get_element_text(self.refund)

    # 电商探索
    ds_info = "c=>ques"

    def click_ds_info(self):
        self.click(self.ds_info)

    # 查询时间
    query_time = "id=>timeFlag"

    def type_select_query_time(self, text):
        self.type_select(self.query_time, text)

    # 设置自定义时间
    cus_start_time = "id=>startTime"
    cus_end_time = "id=>endTime"

    def type_cus_time(self, start_time, end_time ):
        js = "$('input[id=startTime]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.cus_start_time, start_time)

        js = "$('input[id=endTime]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.cus_end_time, end_time)

    # 查询按钮
    query_btn ="xpath=>//*[@id='queryForm']/div[1]/a"

    def click_query_btn(self):
        self.click(self.query_btn)
    # --------------------------------





