# 1.导包
import requests

# 2.使用get方法请求
response = requests.get("https://www.baidu.com")
print(response.text)
