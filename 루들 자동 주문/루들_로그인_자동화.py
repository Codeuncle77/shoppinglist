from selenium import webdriver

url = "https://looddl.ch/ko/login?back=my-account"
browser = webdriver.Chrome("c:/chromedriver.exe") 
browser.implicitly_wait(10) #페이지가 로딩될때까지 최대 10초 기다려줌
browser.maximize_window() #화면 최대화
browser.get(url) #페이지 열기

import time
# 아이디 입력창 
id = browser.find_element_by_css_selector("#login-form > section > div:nth-child(2) > div.col-md-6 > input")
id.click()
id.send_keys("ktc5@kotra.ch")
time.sleep(2)

# 비밀번호 입력창
pw = browser.find_element_by_css_selector("#login-form > section > div:nth-child(3) > div.col-md-6 > div > input")
pw.click()
pw.send_keys("kotraktc5")
time.sleep(2)

# 로그인 버튼
login_btn = browser.find_element_by_css_selector("#login-form > footer > button")
login_btn.click()

#엑셀로부터 링크 불러오기
import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
ws = wb.get_sheet_by_name('Sheet1')
print(ws.cell(row=1, column=2).hyperlink.target)
