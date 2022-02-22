import datetime
from time import sleep

from pykeyboard.windows import PyKeyboard
from selenium import webdriver
from tablib.packages.xlrd.xldate import xldate_as_tuple


def scrapy():
    iedriver = webdriver.Ie()
    iedriver.get('https://ebank.jlnls.com:448/corporbank')  # 填入URL
    current_window = iedriver.current_window_handle
    print(current_window)
    sleep(40)
    # all_window = iedriver.window_handles
    # print(all_window)

    # 点击 账户查询
    m2_js = 'document.getElementById("m2_0101").click()'
    iedriver.execute_script(m2_js)
    sleep(3)

    # 点击 账户交易明细查询
    m3_js = 'document.getElementById("m3_010102").click()'
    iedriver.execute_script(m3_js)
    sleep(5)

    # 切换入右侧详情页ifram
    iframe = iedriver.find_element_by_id('mainFrame')  # 找到iframe这个房间
    iedriver.switch_to_frame(iframe)  # 进入iframe房间
    # iedriver.switch_to_defalut_content()  # 退出iframe房间

    # 进入历史交易明细
    history_js = iedriver.find_element_by_css_selector(".top_link_off > a").get_attribute("href")
    print("history js:", history_js)
    iedriver.execute_script(history_js)
    sleep(5)

    # 切换标签后再次切入右侧详情页ifram
    iframe2 = iedriver.find_element_by_id('mainFrame')  # 找到iframe这个房间
    iedriver.switch_to_frame(iframe2)  # 进入iframe房间

    # 单选框
    value = iedriver.find_element_by_name("detailNum").get_attribute("value")
    print("detail num: ", value)

    iedriver.find_element_by_name("detailNum").click()
    for n in range(1, 4):
        if iedriver.find_element_by_name("detailNum").is_selected():
            break
        else:
            iedriver.find_element_by_name("detailNum").click()
            continue
    sleep(5)

    # 点击下载
    value = iedriver.find_element_by_id("downloadButton").get_attribute("value")
    print("downloadButton num: ", value)
    download_js = 'document.getElementById("downloadButton").click()'
    iedriver.execute_script(download_js)
    sleep(5)

    # all_window = iedriver.window_handles
    # print(all_window)
    # iedriver.find_element_by_id('searchButton').click()
    # sleep(2)

    # alert = iedriver.switch_to_alert()
    # print(alert.text)
    # alert.accept()
    # 默认在取消按钮上，先切换到保存文件上
    k = PyKeyboard()
    k.press_key(k.control_key)
    k.press_key("s")
    k.release_key(k.control_key)
    k.release_key("s")
    sleep(5)

    k.tap_key(k.enter_key)

    # iedriver.quit()


def readexcel(self):
    # 定义一个空列表
    datas = []
    for i in range(1, self.rowNum):
        # 定义一个空字典
        sheet_data = {}
        for j in range(self.colNum):
            # 获取单元格数据类型
            c_type = self.table.cell(i, j).ctype
            # 获取单元格数据
            c_cell = self.table.cell_value(i, j)
            if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
                c_cell = int(c_cell)
            elif c_type == 3:
                # 转成datetime对象
                date = datetime.datetime(*xldate_as_tuple(c_cell, 0))
                c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
            elif c_type == 4:
                c_cell = True if c_cell == 1 else False
            sheet_data[self.keys[j]] = c_cell
            # 循环每一个有效的单元格，将字段与值对应存储到字典中
            # 字典的key就是excel表中每列第一行的字段
            # sheet_data[self.keys[j]] = self.table.row_values(i)[j]
        # 再将字典追加到列表中
        datas.append(sheet_data)
    # 返回从excel中获取到的数据：以列表存字典的形式返回
    return datas

def insertDataToDB():
    print("")


if __name__ == '__main__':
    scrapy()