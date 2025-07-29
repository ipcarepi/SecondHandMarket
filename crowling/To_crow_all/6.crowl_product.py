import os
import csv
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 디렉토리 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# 셀레니움 설정
options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0")
driver = webdriver.Chrome(options=options)

# 접속할 URL
url = "https://kream.co.kr/?tab=home_richshoes"
driver.get(url)
time.sleep(5)

# HTML 파싱
soup = BeautifulSoup(driver.page_source, "html.parser")
product = soup.select_one(".product_card")

# 크롤링 결과 추출
name = product.select_one(".translated_name").text.strip()
brand = product.select_one(".product_info_brand").text.strip()
price = product.select_one(".product_info_price .amount").text.strip().replace(",", "")
img_url = product.select_one(".product_img img")["src"]
detail_url = "https://kream.co.kr" + product.select_one("a")["href"]

driver.quit()

# 더미 데이터 (추후 상세 크롤링시 업데이트 가능)
product_id = 1
brand_id = 1
release_price = ''
last_trade_price = ''
model_number = ''
color = ''
description = ''
delivery_info = ''
created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# ✅ Product.csv 저장
with open(os.path.join(BASE_DIR, f"Product_{timestamp}.csv"), mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "brand_id", "model_number", "release_price", "current_price", "last_trade_price", "color", "description", "delivery_info", "created_at"])
    writer.writerow([product_id, name, brand_id, model_number, release_price, price, last_trade_price, color, description, delivery_info, created_at])

# ✅ Brand.csv 저장
with open(os.path.join(BASE_DIR, f"Brand_{timestamp}.csv"), mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name"])
    writer.writerow([brand_id, brand])

# ✅ ProductImage.csv 저장
with open(os.path.join(BASE_DIR, f"ProductImage_{timestamp}.csv"), mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "product_id", "image_url"])
    writer.writerow([1, product_id, img_url])

print("✅ CSV 파일 저장 완료")
