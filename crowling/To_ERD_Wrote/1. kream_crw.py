import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

# 저장 폴더 준비
SAVE_DIR = "kream_data"
IMG_DIR = os.path.join(SAVE_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

# 크롬 설정
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# 크롤링 대상 URL
url = "https://kream.co.kr/products/82991"
driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

# 🔍 주요 정보 추출
product_name = soup.find("p", class_="product_title").text.strip()
brand = soup.find("p", class_="product_info_brand").text.strip()
release_price_tag = soup.select_one("div.price_box span.num")
release_price = release_price_tag.text.strip() if release_price_tag else "N/A"

# 이미지 다운로드
img_tag = soup.find("img", class_="product_img")
img_url = "https:" + img_tag["src"]
img_filename = os.path.join(IMG_DIR, f"{product_name.replace(' ', '_')}.jpg")

with open(img_filename, "wb") as f:
    f.write(requests.get(img_url).content)

# 📦 구조화된 딕셔너리로 저장
product_data = {
    "product_name": product_name,
    "brand": brand,
    "release_price": release_price,
    "image_path": img_filename
}

# JSON 저장
with open(os.path.join(SAVE_DIR, "product.json"), "w", encoding="utf-8") as f:
    json.dump(product_data, f, ensure_ascii=False, indent=4)

print("✅ 완료: 데이터 수집 및 저장")

driver.quit()
