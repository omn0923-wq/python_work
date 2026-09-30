import os
import requests
import json
import csv
# pip install python-dotenv
from dotenv import load_dotenv
# 자동으로 .env 파일을 읽는다.
# OPENAI_API_KEY: 이 경우는 환경변수 이름만으로도 
# openai의 LLM에 자동 로그인 된다.
load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")

headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
}

url = "https://openapi.naver.com/v1/search/shop.json"
params = {"query": "노트북", "display": 10, "sort": "sim"}

response= requests.get(url, headers=headers, params=params)
print(response.status_code)

data = response.json()

# JSON 파일로 저장 (원본 구조 그대로)
with open("naver_shop_result.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# CSV 파일로 저장 (표 형태)
items = data.get("items", [])
with open("naver_shop_result.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["제목", "가격", "쇼핑몰", "링크"])
    for item in items:
        title = item["title"].replace("<b>", "").replace("</b>", "")  # 검색어 강조 태그 제거
        writer.writerow([title, item["lprice"], item.get("mallName", ""), item["link"]])

print("저장 완료")