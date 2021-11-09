

# 웹 크롤링 

# 인터넷에서 정보를 수집하여 분석
# HTML, CSS, JAVA SCRIPT 웹의 3요소

# 명언 수집
# quotes.toscrape.com

# 1. 웹 페이지를 불러온다.
# 2. 크롤링 원하는 위치를 찾는다.
# 3. 원하는 내용을 찾아서 출력한다.

import re  # 정규 표현식
import os # 시스템 관련
import requests # 웹 연결
import urllib.request as ur # 웹에서 가져온 데이터 다루기
from bs4 import BeautifulSoup as bs

url = "http://quotes.toscrape.com/"

html = ur.urlopen(url)

soup = bs(html.read(),'html.parser')