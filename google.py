from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #몇 초간 셔라
import urllib.request

driver = webdriver.Chrome() #chrome webdriver에 들어감, firefox 쓸거면 chrome 대신 firefox
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") #자동화할 주소
elem = driver.find_element_by_name("q") #검색창 찾는 코드; class값 또는 name값으로 등
elem.send_keys("조코딩") #입력
elem.send_keys(Keys.RETURN) #엔터키를 전송하는 코드

 #반복문을 돌리면서 이미지 모두 다운 - 50장임. 더 많이 원하면 스크롤 내리는 코딩 추가
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #작은 이미지들의 공통된 class명을 가지고 선택하는 코드, elements:이미지 여러개를 선택해서 이미지에 담음
count = 1
for image in images:
    try:
        image.click() #images에서 image 하나씩 클릭
        time.sleep(2) #많은 양의 이미지가 로딩될때까지 2초 기다려주기 
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src") # 선택되어 커진 이미지의 img태그 전체 넣기, src주소 가져오기
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg") #이미지 다운로드, 두 번째 인자는 저장할 이름
        count = count + 1
    except:
        pass #위 시도했을 때 중간에 오류가 나면 그냥 넘어가라

driver.close() #브라우저 창 닫음