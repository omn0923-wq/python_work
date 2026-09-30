from urllib.parse import parse_qsl, urlparse
import requests

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=mrsls740&channel=user"

# url의 쿼리 파라미터를 분리 처리해 주는 라이브러리
parsed = urlparse(url)

base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
params = dict(parse_qsl(parsed.query, keep_blank_values=True))

print("base_url: ", base_url)
print("params: ", params)

# User_Agent를 헤더 추가해서 요청
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}

response = requests.get(base_url, params=params, headers=headers)
print("status_code: ", response.status_code)
print("최종 요청 url: ", response.url)
print("응답 길이: ", len(response.text))
print("\n === 응답 앞부분 500자 ===")
print(response.text[:500])