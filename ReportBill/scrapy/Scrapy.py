from time import sleep

from pykeyboard.windows import PyKeyboard
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from scrapy.ExcelData import ExcelData
from scrapy.MysqlDB import MysqlDB


def scrapy():
    iedriver = webdriver.Ie()
    iedriver.get('https://ebank.jlnls.com:448/corporbank')  # 填入URL
    locator = (By.ID, "m2_0101")
    try:
        WebDriverWait(iedriver, 150).until(EC.presence_of_element_located(locator))
    except:
        print("login timeout!")
        iedriver.quit()

    # 点击 账户查询
    m2_js = 'document.getElementById("m2_0101").click()'
    iedriver.execute_script(m2_js)
    sleep(2)
    gotoPage(iedriver)
    while True:
        downLoad(iedriver)
        insertDataToDB()
        sleep(15)
        gotoPage(iedriver)


def gotoPage(iedriver):
    # 点击 账户交易明细查询
    m3_js = 'document.getElementById("m3_010102").click()'
    iedriver.execute_script(m3_js)

    # 切换入右侧详情页ifram
    iframe = iedriver.find_element_by_id('mainFrame')  # 找到iframe这个房间
    print(iframe)
    iedriver.switch_to.frame(iframe)  # 进入iframe房间

    downloadButton = (By.ID, "downloadButton")
    try:
        WebDriverWait(iedriver, 6).until(EC.presence_of_element_located(downloadButton))
    except:
        print("loading page...")
        sleep(3)


def downLoad(iedriver):
    # 单选框
    detailNum = (By.NAME, "detailNum")
    try:
        WebDriverWait(iedriver, 6).until(EC.presence_of_element_located(detailNum))
    except:
        print("loading detailNum...")

    try:
        radio = iedriver.find_element_by_name("detailNum")
    except NoSuchElementException:
        print("no radio.")
        radio = None

    if not radio:
        print("no data.")
        return
    sleep(2)
    radio = iedriver.find_element_by_name("detailNum")
    for n in range(1, 4):
        if radio.is_selected():
            break
        else:
            radio.click()
            continue

    # 点击下载
    download_js = 'document.getElementById("downloadButton").click()'
    iedriver.execute_script(download_js)
    sleep(3)

    # 默认在取消按钮上，先切换到保存文件上
    k = PyKeyboard()
    k.press_key(k.control_key)
    k.press_key("s")
    k.release_key(k.control_key)
    k.release_key("s")
    sleep(4)
    k.tap_key(k.enter_key)
    # sleep(5)
    try:
        WebDriverWait(iedriver, 6).until(not EC.alert_is_present()(iedriver))
    except:
        print("alert处理")


def insertDataToDB():
    db = MysqlDB()
    excel = ExcelData()
    if not excel.data_path:
        print('db today no data.')
        return
    datas = excel.readExcel()
    db.insertData(datas)
    print(datas)


if __name__ == '__main__':
    scrapy()