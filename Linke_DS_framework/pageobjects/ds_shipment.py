# coding=utf-8
from framework.base_page import BasePage


class Shipment(BasePage):
    # 查询条件

    add_frame = "addTemplete"
    # 添加运费模板
    template_name = "name=>templateName"

    # 按件计费
    pieces_fee = "xpath=>//*[@id='shipmentTemplate']/div/table/tbody/tr[3]/td/label[1]/input"

    # 按重量计费
    weight_fee = "xpath=>//*[@id='shipmentTemplate']/div/table/tbody/tr[3]/td/label[2]/input"

    # 首件/首重
    first_piece = "id=>first"
    # 首费
    first_fee = "xpath=>//*[@id='shipmentTemplate']/div/div[3]/div[2]/table[1]/tbody/tr/td/input[2]"
    # 续件
    add_pieces = "id=>append"
    # 续费
    add_fee = "xpath=>//*[@id='shipmentTemplate']/div/div[3]/div[2]/table[1]/tbody/tr/td/input[4]"
    # 添加运费模板保存按钮
    add_submit = "xpath=>/html/body/div[2]/div[2]/a"

    # --------------------------------

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    def type_template_name(self, text):
        self.type(self.template_name, text)

    def click_pieces_fee(self):
        self.click(self.pieces_fee)

    def click_weight_fee(self):
        self.click(self.weight_fee)

    def click_add_submit(self):
        self.click(self.add_submit)

    def type_first_piece(self, text):
        self.type(self.first_piece, text)

    def type_first_fee(self, text):
        self.type(self.first_fee, text)
        
    def type_add_pieces(self, text):
        self.type(self.add_pieces, text)

    def type_add_fee(self, text):
        self.type(self.add_fee, text)

