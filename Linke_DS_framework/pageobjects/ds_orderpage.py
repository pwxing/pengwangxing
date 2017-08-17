# coding=utf-8
from framework.base_page import BasePage


class OrderPage(BasePage):
    # 订单编号
    order_no = "name=>orderNo"
    transaction_no = "name=>transactionNo"
    take_phone = "name=>takePhone"
    take_name = "name=>takeName"
    nick_name = "name=>nick"
    search_query = "id=>searchQuery1"
    all_order = "xpath=>//*[@id='switchTab1']/td[1]/a"
    unpay = "xpath=>//*[@id='switchTab1']/td[2]/a"
    take_store = "xpath=>//*[@id='queryForm']/div[1]/div[7]/div[2]/div/input[2]"
    belong_store = "xpath=>//*[@id='queryForm']/div[1]/div[16]/div[2]/div/input[2]"
    pay_time_begin = "id=>payTimeBegin"
    pay_time_end = "id=>payTimeEnd"
    create_time_begin = "id=>createTimeBegin"
    create_time_end = "id=>createTimeEnd"
    # 订单状态
    order_status = "name=>status"
    status_value0 = "//option[@value='0']"
    status_value2 = "//option[@value='2']"
    status_value3 = "//option[@value='3']"
    status_value4 = "//option[@value='4']"
    status_value5 = "//option[@value='5']"
    status_value6 = "//option[@value='6']"

    # 订单类型
    order_type = "name=>dyOrderType"

    # 支付类型
    # pay_way = "name=>payWay"

    pay_way1 = "xpath=>//div[@class='form']/div[5]/div[2]/div/select//option[3]"

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    def click_query(self):
        self.click(self.search_query)

    def type_order_no(self, text):
        self.type(self.order_no, text)

    def type_transaction_no(self, text):
        self.type(self.transaction_no, text)

    def type_take_phone(self, text):
        self.type(self.take_phone, text)

    def type_take_name(self, text):
        self.type(self.take_name, text)

    def type_nick_name(self, text):
        self.type(self.nick_name, text)

    def type_take_store(self, text):
        self.type(self.take_store, text)

    def type_belong_store(self, text):
        self.type(self.belong_store, text)

    def type_pay_time_begin(self, text):
        self.type(self.pay_time_begin, text)

    def type_pay_time_end(self, text):
        self.type(self.pay_time_end, text)

    def type_create_time_begin(self, text):
        self.type(self.create_time_begin, text)

    def type_create_time_end(self, text):
        self.type(self.create_time_end, text)

    def click_orders(self):
        for i in range(1, 10):
            self.click("xpath=>//*[@id='switchTab1']/td[" + str(i) + "]/a")

    # 订单状态:1全部 2未付款 3未发货 4已发货 5交易完成 6已取消 7退款
    def click_status(self, text):
        self.click("xpath=>//div[@class='form']/div[3]/div[2]/div/select//option[" + str(text) + "]")

    def click_status_query(self, text):
        self.click("xpath=>//div[@class='form']/div[3]/div[2]/div/select//option[" + str(text) + "]")
        self.click_query()

    # 订单类型：1全部 2购买 3许愿 4送礼 5秒杀 6预售 7抱团
    def click_order_type(self, text):
        self.click("xpath=>//div[@class='form']/div[4]/div[2]/div/select//option[" + str(text) + "]")

    def click_order_type_query(self, text):
        self.click("xpath=>//div[@class='form']/div[4]/div[2]/div/select//option[" + str(text) + "]")
        self.click_query()

    # 支付方式:  1全部 2支付宝 3微信 4到店支付 5货到付款 6余额支付 7优惠抵扣
    def click_pay_way(self, text):
        self.click("xpath=>//div[@class='form']/div[5]/div[2]/div/select//option[" + str(text) + "]")

    def click_pay_way_query(self, text):
        self.click("xpath=>//div[@class='form']/div[5]/div[2]/div/select//option[" + str(text) + "]")
        self.click_query()

    # 配送方式 1全部 2快递配送 3商家配送 4用户到店 5系统配送
    def click_delivery_type(self, text):
        self.click("xpath=>//div[@class='form']/div[6]/div[2]/div/select//option[" + str(text) + "]")

    def click_delivery_type_query(self, text):
        self.click("xpath=>//div[@class='form']/div[6]/div[2]/div/select//option[" + str(text) + "]")
        self.click_query()

    # 商品类别 1全部 2实体商品 3虚拟商品
    def click_goods_type(self, text):
        self.click("xpath=>//*[@id='goodsType1']/option[" + str(text) + "]")

    def click_goods_type_query(self, text):
        self.click("xpath=>//*[@id='goodsType1']/option[" + str(text) + "]")
        self.click_query()

    # 虚拟商品类别 1全部 2储值卡 3代金券
    def click_goods_type2(self, text):
        self.click("xpath=>//*[@id='goodsType2']/option[" + str(text) + "]")

    def click_goods_type2_query(self, text):
        self.click("xpath=>//*[@id='goodsType2']/option[" + str(text) + "]")
        self.click_query()

    def click_py(self):
        self.click(self.pay_way1)
    # def click_order_type_query(self, text):
    #     self.click_select(self.order_type, "//option[@value='" + text + "']")
    #     self.click_query()




