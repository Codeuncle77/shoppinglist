#조건 1) 구글스프레드시트 데이타 기입 - 엑셀 항목 : 링크, 수량
#0 루들 로그인  홈페이지 https://looddl.ch/
#              아이디(공용)	ktc5@kotra.ch
#              비밀번호	kotraktc5
#1 엑셀로 다운로드 > *구글 스프레드시트에서 바로 가능? 
#2 다운로드 받은 스프레드스 시트(엑셀) 열기 
#3A 장바구니 
#3A-1 링크 오픈 :A열 1행
#3A-2 수량 조정 :B열
#3A-3 장바구니 클릭 
#3A-4 다음 링크 오픈(반복문) A열 2행 
#3A-5 수량 조정: B열 2행

#3B 가격 크롤링 
#3B-1 링크 오픈 : A열 1행
#3B-2 가격 Class 값 찾기
#3B-3 가격 엑셀로 가져오기: C열 1행
#3B-4 다음 링크 오픈(반복문)
#마지막 링크까지 다 열면 B열 * C열 = D열 입력
#-------------------------------------------------------------------------------------------------------

#0 루들 로그인
#루들 홈페이지 오픈
#import webbrowser
#webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://looddl.ch/")

from selenium import webdriver

browser = webdriver.Chrome("c:/chromedriver.exe")
browser.get("https://looddl.ch/")


