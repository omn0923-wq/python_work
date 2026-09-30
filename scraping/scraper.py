from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}

response =requests.get(url, headers=headers)
# print(response.status_code)
# print(response.text[:1000])

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
item_list = []

print(f"전체 책 수: {len(books)}")
print(books)

for book in books:
    book_name = book.find("h3").find("a")["title"]
    book_price = book.find("div", class_="product_price").find("p", class_="price")
    # 찾은 결과를 dict 생성
    item = {
        "title": book_name,
        "price": book_price
    }
    # item_list에 추가
    item_list.append(item)
    print(f"제목: {book_name}, 가격: {book_price}")

print(item_list)
