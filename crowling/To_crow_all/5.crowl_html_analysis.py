import os
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ✅ 디렉토리 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LINKS_FILE = os.path.join(BASE_DIR, "product_links.json")

# ✅ 셀레니움 설정
options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)")
driver = webdriver.Chrome(options=options)

# ✅ KREAM 홈 인기 신발 페이지로 이동
url = "https://kream.co.kr/?tab=home_richshoes"
driver.get(url)
time.sleep(5)

# ✅ HTML 파싱
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# ✅ 상품 링크 추출
product_links = []
for tag in soup.select("a"):

    href = tag.get("href", "")
    if href.startswith("/products/") and href.count("/") == 2:
        full_url = "https://kream.co.kr" + href
        if full_url not in product_links:
            product_links.append(full_url)

# ✅ 링크 저장
with open(LINKS_FILE, "w", encoding="utf-8") as f:
    json.dump(product_links, f, indent=2, ensure_ascii=False)

print(f"✅ 총 {len(product_links)}개의 링크 저장 완료: {LINKS_FILE}")
