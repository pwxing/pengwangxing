# coding=utf-8
from framework.base_page import BasePage


class PageManage(BasePage):
    # 主页
    order_no = "name=>orderNo"

    # 列表展示页
    show_sort = "xpath=>//*[@id='goodShowForm']/div[3]/table/tbody/tr/td[1]/div/p/label/input"
    show_category = "xpath=>//*[@id='goodShowForm']/div[3]/table/tbody/tr/td[2]/div/p/label/input"
    list_submit = "id=>submitBtn"

    # 加载页
    img_load_page = "xpath=>//*[@id='tloadForm']/div[4]/div/div[2]/table/tbody/tr[1]/td[2]/label[1]/input"
    editor_load_page ="xpath=>//*[@id='tloadForm']/div[4]/div/div[2]/table/tbody/tr[1]/td[2]/label[2]/input"
    switch_btn ="id=>openAndColesBtn"
    load_page_submit = "xpath=>//*[@id='tloadForm']/div[4]/div/div[2]/p/button"

    # 1大图 2中图 3小图 4小图2 5分类
    show_img1 = "id=>c1"
    show_img2 = "id=>c2"
    show_img3 = "id=>c3"
    show_img4 = "id=>c4"
    show_img5 = "id=>c5"

    defalut_show_img = "id=>r1"
    # 商品详情页
    standard_mode = "xpath=>//*[@id='goodDetailFrom']/table/tbody/tr/td[1]/div/p/label/input"
    simple_mode ="xpath=>//*[@id='goodDetailFrom']/table/tbody/tr/td[2]/div/p/label/input"
    goods_mode_submit = "xpath=>//*[@id='submitBtn']"
    # 自定义页面


    def click_menu(self, loc):
        self.click_partial_link_text(loc)

    # 点击主题上的图片一至图片五
    def click_theme_img(self, text):
        imglist = self.driver.find_elements_by_id("sort_img")
        print imglist[text-1]
        imglist[text-1].click()

    def click_show_img(self, text):
        if self.driver.find_element_by_id("c" + str(text)).is_selected():
            pass
        else:
            self.click("id=>c" + str(text))

    def cancel_show_img(self, text):
        if self.driver.find_element_by_id("c" + str(text)).is_selected():
            self.click("id=>c" + str(text))
        else:
            pass

    def click_default_show_img(self, text):
        self.click("id=>r" + str(text))

    def get_show_img_status(self, text):
        return self.driver.find_element_by_id("c" + str(text)).is_selected()

    def get_default_show_img(self):
        for i in range(1, 6):
            if self.driver.find_element_by_id("r" + str(i)).is_selected():
                return i
                break

    def click_list_submit(self):
        self.click(self.list_submit)

    # ----------------------加载页------------------------------
    def click_img_load_page(self):
        self.click(self.img_load_page)

    def click_editor_load_page(self):
        self.click(self.editor_load_page)

    def click_switch_btn(self):
        self.click(self.switch_btn)

    def click_load_page_submit(self):
        self.click(self.load_page_submit)

    # ------------------------商品详情页-------------------------
    def click_stardard_mode(self):
        self.click(self.standard_mode)

    def click_simple_mode(self):
        self.click(self.simple_mode)

    def click_goods_mode_submit(self):
        self.click(self.goods_mode_submit)









