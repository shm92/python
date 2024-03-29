import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://n.news.naver.com/mnews/article/001/0014398481?rc=N&ntype=RANKING"  # 이메일을 수집할 웹 페이지 주소
response = requests.get(url)  # 웹 페이지 요청

soup = BeautifulSoup(response.text, "html.parser")  # BeautifulSoup 객체 생성
emails = []

# 이메일 패턴
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 웹 페이지에서 모든 텍스트 추출
text = soup.get_text()

# 이메일 패턴 매칭 후 리스트에 추가
for match in re.findall(email_pattern, text):
    emails.append(match)

# 중복 제거
emails = list(set(emails))

# 결과 출력
print(emails)

# 이메일을 엑셀 파일로 저장
df = pd.DataFrame(emails, columns=["Email"])
df.to_excel("10.이메일을 수집하여 엑셀에 기록하기/이메일.xlsx", index=False)
