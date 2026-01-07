# from urllib.parse import urlparse, parse_qs

# url = "https://google.com/search?q=python&page=2"

# parsed_url = urlparse(url)
# params = parse_qs(parsed_url.query)

# print("전체 URL:", url)
# print("경로(Path):", parsed_url.path)
# print("쿼리(Query):", parsed_url.query)
# 
# import requests
# url = "https://jsonplaceholder.typicode.com/todos"

# response = requests.get(url)

# print("Status Code:", response.status_code)

# data = response.json()

# print("응답 타입:", type(data))

# print("전체 할 일 개수:", len(data))

# first = data[0]

# print("\n[첫 번째 TODO]")
# print(first)

# print("\n[앞 5개의 제목만 출력]")
# for todo in data[:5]:

#     print(f"- (id={todo['id']}) {todo['title']}")

