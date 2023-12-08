from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import openpyxl
import requests

options = webdriver.ChromeOptions()

browser = webdriver.Chrome()

# mTworks Admin Page 진입
browser.get("http://192.168.7.72:81/login/login.do")

# 로그인
input_id = browser.find_element(By.XPATH, '//*[@id="login_id"]').send_keys("mtcadmin")
login_pw = browser.find_element(By.XPATH, '//*[@id="login_pw"]').send_keys("mtworks12!@")
login_button = browser.find_element(By.XPATH, '//*[@id="login_wrap"]/div/form/div[2]/ul/li/a[1]').click()

sleep(3)

# 기타 탭 선택
click_etc = browser.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/ul/li[5]/a').click()

sleep(3)

# 일일점검 이력관리 탭 선택
click_daily_check = browser.find_element(By.CSS_SELECTOR, '#header > div > div.navigation > ul > li.menu5.active > div > ul > li:nth-child(2) > a')
click_daily_check.send_keys('\n')

sleep(5)

# 날짜 선택 (어제 날짜 선택)
# yesterday = 

first_datepicker = browser.find_element(By.XPATH, '//*[@id="device_format"]/table/tbody/tr[1]/td[2]/div/div[1]/img').click()
first_datepicker_widget = browser.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[5]/a').click()

second_datepicker = browser.find_element(By.XPATH, '//*[@id="device_format"]/table/tbody/tr[1]/td[2]/div/div[3]/img').click()
second_datepicker_widget = browser.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[5]/a').click()



# 구분 선택 > 검색
cata = browser.find_element(By.XPATH, '//*[@id="gubun"]').click()
cata_name = browser.find_element(By.XPATH, '//*[@id="gubun"]/option[2]').click()
cata_name_galaxy = browser.find_element(By.XPATH, '//*[@id="gubunVal"]').send_keys('iPhone') # Galaxy / iPhone
search_button = browser.find_element(By.XPATH, '//*[@id="device_format"]/table/tbody/tr[3]/td/div/a[1]').click()

sleep(5)

# 노출된 데이터 가져오기
table = browser.find_element(By.XPATH, '//*[@id="device_format"]/div[2]/table')
td_elements = table.find_elements(By.TAG_NAME, 'td')

# 가져온 td 값을 엑셀 파일로 정리
wb = openpyxl.Workbook()
sheet = wb.active
column_headers = ["점검일시", "테스트명", "서비스명", "상품명", "스크립트", "회차", "점검결과", "담당자"]
sheet.append(column_headers)

# td 값을 7개씩 묶어서 엑셀에 쓰기
for i in range(0, len(td_elements), 9):
    td_values = [td.text for td in td_elements[i:i+9]]
    sheet.append(td_values)

wb.save("mtworks_iOS.xlsx") #AOS / iOS

browser.quit()