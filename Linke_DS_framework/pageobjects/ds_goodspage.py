# coding=utf-8
from framework.base_page import BasePage


class GoodsPage(BasePage):
    # 商品类目
    goods_category1 = "xpath=>//*[@id='category1']/p[3]"
    goods_category2 = "xpath=>//*[@id='category2']/p[2]"
    goods_category3 = "xpath=>//*[@id='category3']/p[1]"

    # 商品类别
    goods_type = "id=>selectGoodsType1"
    normal_goods_value = "//option[@value='1']"     # 实体商品
    virtual_goods_value = "//option[@value='2']"    # 虚拟商品
    virtual_goods_type = "id=>selectGoodsType2"
    virtual_goods_value1 = "//option[@value='3']"    # 储值卡
    virtual_goods_value2 = "//option[@value='4']"    # 代金券
    # 商品名称
    goods_name = "id=>add_goodsname"

    # 商品编码
    goods_code = "id=>add_goodsCode"

    # 商品描述
    goods_remark = "id=>add_remark"

    # 上传图片
    goods_pic1 = "xpath=>//*[@id='upload_ls']/dd[1]/div[1]/img[2]"

    # 上传图片frame
    pic_frame ="_uploadPic_iframe"

    # 图库中的第一张图片
    map_storage1 ="xpath=>//*[@id='upload-list']/div[1]/div[1]/img"

    # 图库中的确定按钮
    map_storage_btn = "xpath=>/html/body/div[4]/div[2]/a[1]"

    # 商品价格
    sales_price = "xpath=>//*[@id='ejsxTb2']/tbody/tr/td[1]/input"
    market_price = "xpath=>//*[@id='ejsxTb2']/tbody/tr/td[2]/input"
    worth = "xpath=>//*[@id='ejsxTb2']/tbody/tr/td[3]/input"
    # 库存
    stock_num = "xpath=>//*[@id='ejsxTb2']/tbody/tr/td[4]/input"
    # 货号
    shelf_no = "xpath=>//*[@id='ejsxTb2']/tbody/tr/td[5]/input"
    # 添加代金券frame
    voucher_frame = "addCoupon"
    voucher_select_btn = "xpath=>//*[@id='a38a167c-a290-408f-8a16-7ca290808f1b']/td[5]/a"

    # 配送方式
    express_delivery = "name=>expressDeliverys[0].deliveryType"
    delivery_fees = "xpath=>//*[@id='page_block_4']/div[4]/table[2]/tbody[2]/tr[1]/td[3]/label/input"

    # 总保存按钮
    goods_submit = "id=>submitBtn"

    def click_goods_submit(self):
        self.click(self.goods_submit)

    def click_goods_category(self):
        self.click(self.goods_category1)
        self.click(self.goods_category2)
        self.click(self.goods_category3)

    # def click_goods_type1(self):
    #     self.click(self.goods_type1)

    def click_normal_goods_type(self):
        self.click_select(self.goods_type, self.normal_goods_value)

    def click_virtual_goods_type(self):
        self.click_select(self.goods_type, self.virtual_goods_value)

    def click_virtual_goods_type3(self):    # 储值卡
        self.click_select(self.virtual_goods_type, self.virtual_goods_value1)

    def click_virtual_goods_type4(self):    # 代金券
        self.click_select(self.virtual_goods_type, self.virtual_goods_value2)

    def type_goods_name(self, text):
        self.type(self.goods_name, text)

    def type_goods_code(self, text):
        self.type(self.goods_code, text)

    def type_goods_remark(self, text):
        self.type(self.goods_remark, text)

    def type_sales_price(self, text):
        self.type(self.sales_price, text)

    def type_market_price(self, text):
        self.type(self.market_price, text)

    def type_worth(self, text):
        self.type(self.worth, text)

    def type_stock_num(self, text):
        self.type(self.stock_num, text)

    def type_shelf_no(self, text):
        self.type(self.shelf_no, text)

    def click_goods_pic1(self):
        self.click(self.goods_pic1)

    def click_map_storage1(self):
        self.click(self.map_storage1)

    def click_map_storage_btn(self):
        self.click(self.map_storage_btn)

    def click_voucher_select_btn(self):
        self.click(self.voucher_select_btn)

    def click_express_delivery(self):
        self.click(self.express_delivery)

    def click_delivery_fees(self):
        self.click(self.delivery_fees)

    # -----------------自建商品（加盟）----商品列表（直营）-------------
    unonline = "xpath=>//*[@id='statusCount0']"
    online = "xpath=>//*[@id='statusCount1']"
    sale_out = "xpath=>//*[@id='statusCount4']"
    off_line = "xpath=>//*[@id='statusCount2']"
    # 根据输入的字符（未上架、已上架……），返回商品数量
    def get_goods_status_num(self, text):
        if text == u"未上架":
            return self.get_element_text(self.unonline)
        elif text == u"已上架":
            return self.get_element_text(self.online)
        elif text == u"已售完":
            return self.get_element_text(self.sale_out)
        elif text == u"已下架":
            return self.get_element_text(self.off_line)

    def get_unonline_text(self):
        return self.get_element_text(self.unonline)

    def get_online_text(self):
        return self.get_element_text(self.online)

    def get_sale_out_text(self):
        return self.get_element_text(self.sale_out)

    def get_off_line_text(self):
        return self.get_element_text(self.off_line)

    # def click_menu(self, loc):
    #     self.click_partial_link_text(loc)
    # 查询按钮，1是加盟，0是直营
    def click_query_btn(self, text):
        if int(text) == 1:
            self.click("xpath=>//*[@id='queryForm']/div/div[1]/div[6]/div/div[1]/a")
        elif int(text) == 0:
            self.click("xpath=>//*[@id='queryForm']/div/div[1]/div[4]/div/div[1]/a")

    # 选择门店查询商品
    store_select = "id=>storeSelect"

    def type_store_select(self, text):
        self.type_select(self.store_select, text)

    # 输入查询方式：名称、货号、商品价
    goods_attr_select = "id=>goodsAttrSelect"

    def type_goods_attr_select(self, text):
        self.type_select(self.goods_attr_select, text)
    # 输入要查询的字符
    goods_attr_text ="id=>goodsAttrSelectText"

    def type_goods_attr_text(self, text):
        self.type_select(self.goods_attr_text, text)

    # 商品列表中的商品类目查询，分为一级、二级、三级
    one_category = "id=>oneCategoryId"

    def type_one_category(self, text):
        self.type_select(self.one_category, text)
    two_category = "id=>twoCategoryId"

    def type_two_category(self, text):
        self.type_select(self.two_category, text)

    three_category = "id=>threeCategoryId"

    def type_three_category(self, text):
        self.type_select(self.three_category, text)

    # 商品列表中的商品类型查询：实体、虚拟:(储值卡、券)
    query_goods_type = "id=>selectGoodsType1"

    def type_query_goods_type(self, text):
        self.type_select(self.query_goods_type, text)

    query_virtual_goods = "id=>selectGoodsType2"

    def type_query_virtual_goods(self, text):
        self.type_select(self.query_virtual_goods, text)

    # 下架、移入未上架、删除等操作（可以共用）的确定、取消按
    off_line_submit_btn = "xpath=>/html/body/div[2]/div[3]/a[1]"
    off_line_cancel_btn = "xpath=>/html/body/div[2]/div[3]/a[2]"

    def click_off_line_submit_btn(self):
        self.click(self.off_line_submit_btn)

    def click_off_line_cancel_btn(self):
        self.click(self.off_line_cancel_btn)

    # 全选商品列表当前页
    all_goods_current_page_btn = "xpath=>//*[@id='queryForm']/div/div[1]/div[7]/label/input"

    def click_all_goods_current_page_btn(self):
        self.select_checkbox(self.all_goods_current_page_btn)

    def cancel_all_goods_current_page_btn(self):
        self.cancel_checkbox(self.all_goods_current_page_btn)


    goods_list_name = "xpath=>//*[@id='queryForm']/div/div[1]/table/tbody/tr[1]/td[3]/p"
    # // *[ @ id = "queryForm"] / div / div[1] / table / tbody / tr[1] / td[4]
    # // *[ @ id = "queryForm"] / div / div[1] / table / tbody / tr[2] / td[4]
    def get_goods_list_name(self):
        self.get_element_text(self.goods_list_name)

    def print_goods_info_by_index(self, index):
        print "index:", index
        table_name_list = [u"商品名称、价格",u"库存",u"销量", u"流量",u"销售额",\
                         u"成交顾客",u"客单价",u"退货数",u"商品类别"]
        for i in range(1, 10):
            goods_info_name = table_name_list[i-1]
            goods_info_value = self.driver.find_element_by_xpath \
                ("//*[@id='queryForm']/div/div/table/tbody/tr["+str(index)+"]/td["+str(i+2)+"]").text
            print goods_info_name, ":  ", goods_info_value




