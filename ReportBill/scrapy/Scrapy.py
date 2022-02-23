from time import sleep

from pykeyboard.windows import PyKeyboard
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from scrapy.ExcelData import ExcelData
from scrapy.MysqlDB import MysqlDB


class Scrapy():

    def __init__(self):
        self.iedriver = webdriver.Ie()
        self.iedriver.get('https://ebank.jlnls.com:448/corporbank')  # 填入URL
        locator = (By.ID, "menuBar2")
        try:
            WebDriverWait(self.iedriver, 60).until(EC.presence_of_element_located(locator))
        except:
            print("login timeout!")
            self.iedriver.quit()
        # current_window = self.iedriver.current_window_handle
        # print(current_window)

    def goToPage(self):
        # 点击 账户查询
        m2_js = 'document.getElementById("m2_0101").click()'
        self.iedriver.execute_script(m2_js)
        sleep(3)

        # 点击 账户交易明细self.查询
        m3_js = 'document.getElementById("m3_010102").click()'
        self.iedriver.execute_script(m3_js)
        sleep(5)

        # 切换入右侧详情页ifram
        iframe = self.iedriver.find_element_by_id('mainFrame')  # 找到iframe这个房间
        self.iedriver.switch_to_frame(iframe)  # 进入iframe房间
        # iedriver.switch_to_defalut_content()  # 退出iframe房间

        # 进入历史交易明细 测试用，如果是当天交易则不用进入
        history_js = self.iedriver.find_element_by_css_selector(".top_link_off > a").get_attribute("href")
        print("history js:", history_js)
        self.iedriver.execute_script(history_js)
        sleep(5)

        # 切换标签后再次切入右侧详情页ifram
        iframe2 = self.iedriver.find_element_by_id('mainFrame')  # 找到iframe这个房间
        self.iedriver.switch_to_frame(iframe2)  # 进入iframe房间

        # self.iedriver.quit()

    def downLoad(self):
        # 单选框
        try:
            radio = self.iedriver.find_element_by_name("detailNum")
        except NoSuchElementException:
            radio = None

        if radio:
            value = self.iedriver.find_element_by_name("detailNum").get_attribute("value")
            print("detail num: ", value)
        else:
            print("no data.")
            return
        self.iedriver.find_element_by_name("detailNum").click()
        for n in range(1, 4):
            if self.iedriver.find_element_by_name("detailNum").is_selected():
                break
            else:
                self.iedriver.find_element_by_name("detailNum").click()
                continue
        # sleep(5)

        # 点击下载
        value = self.iedriver.find_element_by_id("downloadButton").get_attribute("value")
        print("downloadButton num: ", value)
        download_js = 'document.getElementById("downloadButton").click()'
        self.iedriver.execute_script(download_js)
        sleep(3)

        # 默认在取消按钮上，先切换到保存文件上
        k = PyKeyboard()
        k.press_key(k.control_key)
        k.press_key("s")
        k.release_key(k.control_key)
        k.release_key("s")
        sleep(3)
        k.tap_key(k.enter_key)

    def insertDataToDB(self):
        db = MysqlDB()
        excel = ExcelData()
        datas = excel.readExcel()
        db.insertData(datas)
        print(datas)


if __name__ == '__main__':
    scrapy = Scrapy()
    scrapy.goToPage()
    scrapy.downLoad()
    while True:
        scrapy.insertDataToDB()
        sleep(15)
        scrapy.iedriver.find_element_by_id('searchButton').click()
        sleep(2)
        scrapy.downLoad()