# coding=utf-8
from framework.base_page import BasePage
from selenium.webdriver.support.select import Select


class Setmeal(BasePage):
    # 活动标题
    act_title = "id=>title"

    def type_act_title(self, text):
        self.type(self.act_title, text)

    # 活动时间
    act_start_time = "id=>startValidTime"
    act_end_time = "id=>endValidTime"

    def type_act_time(self, start_time, end_time ):
        js = "$('input[id=startValidTime]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.act_start_time, start_time)

        js = "$('input[id=endValidTime]').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.type(self.act_end_time, end_time)

    # 上传图片
    upload_pic_btn = "xpath=>//*[@id='command']/div[3]/div[2]/table/tbody/tr[4]/td/div/dl/dd/div/img[1]"
    upload_frame_id = "_uploadPic_iframe"
    #   本地上传
    upload_pic_menu = "id=>uppic"
    #   选择图库
    choose_pic_menu = "id=>choosepic"
    #   选择图库的第一张图片
    choose_first_pic = "xpath=>//*[@id='upload-list']/div[1]/div[1]/img"
    #   图库的保存按钮
    upload_submit = "xpath=>/html/body/div[3]/div[2]/a[1]"

    # 优惠方式
    #   打折
    discount1 = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[1]/td/div/span[1]/input"
    #   减价
    discount2 = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[1]/td/div/span[2]/input"

    def click_discount_type(self, text):
        if str(text) == "1":
            self.click(self.discount1)
        elif str(text) == "2":
            self.click(self.discount2)

    #   搭配商品数
    discount_goods_num = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[1]/td/ul[2]/li[1]/input[1]"

    def type_discount_goods_num(self, text):
        self.type(self.discount_goods_num, text)
    discount_price = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[1]/td/ul[2]/li[1]/input[2]"

    def type_discount_price(self, text):
        self.type(self.discount_price, text)

    add_discount_btn = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[1]/td/ul[2]/li[1]/a"

    def click_add_discount_btn(self):
        self.click(self.add_discount_btn)

    minus_discount_btn = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[1]/td/ul[2]/li[2]/a"
    def click_minus_discount_btn(self):
        self.click(self.minus_discount_btn)

    # 活动邮费   1包邮 2按运费模板计算
    free = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[2]/td/span[1]/input"
    yunfei = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[2]/td/span[2]/input"

    def click_delivery_fee(self, text):
        if str(text) == "1":
            self.click(self.free)
        elif str(text) == "2":
            self.click(self.yunfei)

    # 其它优惠  粉丝折扣  积分抵扣  代金券抵扣  满立减
    fans_discount = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[3]/td/span[1]/input"
    integral_discount = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[3]/td/span[2]/input"
    cash_discount = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[3]/td/span[3]/input"
    fulreduce_discount = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[3]/td/span[4]/input"

    def select_fans_discount(self):
        self.select_checkbox(self.fans_discount)

    def cancel_fans_discount(self):
        self.cancel_checkbox(self.fans_discount)

    def select_integral_discount(self):
        self.select_checkbox(self.integral_discount)

    def cancel_integral_discount(self):
        self.cancel_checkbox(self.integral_discount)

    def select_cash_discount(self):
        self.select_checkbox(self.cash_discount)

    def cancel_cash_discount(self):
        self.cancel_checkbox(self.cash_discount)

    def select_fulreduce_discount(self):
        self.select_checkbox(self.fulreduce_discount)

    def cancel_fulreduce_discount(self):
        self.cancel_checkbox(self.fulreduce_discount)

    # 是否在活动广场中显示
    act_square_show = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[4]/td/span[1]/input"
    act_square_not_show = "xpath=>//*[@id='command']/div[4]/div[2]/table/tbody/tr[4]/td/span[2]/input"

    def get_act_square_show(self):
        if self.get_element_is_select(self.act_square_show):
            return 1
        elif self.get_element_is_select(self.act_square_not_show):
            return 2
        else:
            return 0

    def select_act_square_show(self, text):
        if text == 1:
            self.click(self.act_square_show)
        elif text == 2:
            self.click(self.act_square_not_show)

    # 活动描述
    act_remark = "id=>description"

    def type_act_remark(self, text):
        self.type(self.act_remark, text)

    # ----------------添加主商品
    add_main_goods_btn = "xpath=>//*[@id='addMainGoodsTr']/td/a"

    # ----------------添加搭配商品
    add_other_goods_btn ="xpath=>//*[@id='addFgoodsTr']/td/a"

    def click_add_main_goods_btn(self):
        self.click(self.add_main_goods_btn)

    def click_add_other_goods_btn(self):
        self.click(self.add_other_goods_btn)

    add_goods_frame = "goodsList"
    goods_name = "name=>goodsName"

    # 选择商品类别 0全部 1实体商品 2虚拟商品
    def click_goods_type(self, text):
        self.click("xpath=>//*[@id='type']/option[" + str(text) + "]")

    def type_goods_name(self, text):
        self.type(self.goods_name, text)

    # 选择商品状态 0全部 1未上架 2已上架
    def click_status(self, text):
        self.click("xpath=>//*[@id='status']/option[" + str(text) + "]")

    # 商品是否可参与 0全部 1可参与 2不可参与
    choose_goods_all = "xpath=>//*[@id='queryGoodsForm1']/div/div/label[4]/input"
    choose_goods_y = "xpath=>//*[@id='queryGoodsForm1']/div/div/label[5]/input"
    choose_goods_n = "xpath=>//*[@id='queryGoodsForm1']/div/div/label[6]/input"

    def choose_goods_is_selected(self):
        if self.get_element_is_select(self, self.choose_goods_all):
            return 0
        if self.get_element_is_select(self, self.choose_goods_y):
            return 1
        if self.get_element_is_select(self, self.choose_goods_n):
            return 2

    def choose_goods_join(self, text):
        if text == 0:
            self.click(self.choose_goods_all)
        elif text == 1:
            self.click(self.choose_goods_y)
        elif text == 2:
            self.click(self.choose_goods_n)
    # 搜索
    query_btn = "xpath=>//*[@id='queryGoodsForm1']/div/div/a"

    def click_query_btn(self):
        self.click(self.query_btn)

    # 商品复选框
    choose_goods_name = "xpath=>//*[@name='goodsIdCheckbox']"

    def click_choose_goods(self):
        self.click(self.choose_goods_name)

    def choose_goods_index(self, text):
        goods_list = self.driver.find_elements_by_name("goodsIdCheckbox")
        print goods_list
        goods_list[2].click()

    # 根据输入ID进行选择
    def choose_goods_id(self, ID):
        self.click("xpath=>//*[@id='" + ID + "']")

    # 全选当前页、 全选当前类
    current_page_goods = "id=>pagechecked"
    all_page_goods = "id=>allchecked"

    def select_current_page_goods_check(self):
        self.select_checkbox(self.current_page_goods)

    def cancel_current_page_goods_check(self):
        self.cancel_checkbox(self.current_page_goods)

    def select_all_page_goods_check(self):
        self.select_checkbox(self.all_page_goods)

    def cancel_all_page_goods_check(self):
        self.cancel_checkbox(self.all_page_goods)

    # 选择商品确认按钮
    choose_goods_btn = "xpath=>/html/body/div[3]/div[2]/a"

    def click_choose_goods_btn(self):
        self.click(self.choose_goods_btn)

    # 活动保存按钮
    act_submit = "id=>submit"

    def click_act_submit(self):
        self.click(self.act_submit)

    def click_menu(self, loc):
        self.click_partial_link_text(loc)





