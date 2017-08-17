# coding=utf-8
from framework.base_page import BasePage


class GoodsPromo(BasePage):
    # 推荐
    query_btn = "id=>searchQuery1"
    input_keyword = "id=>keyword"
    keyword_type = "id=>searchKeywordType"
    recommend_submit = "id=>sub-btn"

    # 限购

    # 积分抵扣

    # 代金券抵扣

    # 满包邮设置

    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    # ----------------------推荐------------------------------
    def click_keyword_type(self, text):
        self.click("xpath=>//*[@id='searchKeywordType']/option[" + str(text) + "]")

    def type_input_keyword(self, text):
        self.type(self.input_keyword, text)

    def click_query_btn(self):
        self.click(self.query_btn)

    def click_recommend_submit(self):
        self.click(self.recommend_submit)

    # ------------------------商品详情页-------------------------

    # -------------------自定义页面----------------------------------








