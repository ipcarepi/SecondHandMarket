import json
import os
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ WebDriver 설정
options = Options()
# options.add_argument("--headless")  # 개발 중엔 주석 처리
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

# ✅ 셀레니움 감지 우회
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

# ✅ 대상 URL
url = "https://kream.co.kr/products/97779"
print(f"🔗 접속할 URL: {url}")
driver.get(url)

# ✅ 요소 로딩 대기
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_title"))
    )
except:
    print("❌ 페이지 로딩 실패")

# ✅ HTML 파싱
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# ✅ 결과 저장 dict
result = {"url": url}

# ✅ name & brand from <title>
title_tag = soup.find("title")
if title_tag:
    title_parts = title_tag.text.strip().split("|")
    if len(title_parts) >= 2:
        result["name"] = title_parts[0].strip()
        result["brand"] = title_parts[1].strip()

# ✅ model_number
model_number = soup.find(text=re.compile("모델번호"))
if model_number:
    sibling = model_number.find_parent().find_next("div")
    result["model_number"] = sibling.text.strip() if sibling else None

# ✅ release_price
release_price_tag = soup.find(text=re.compile("발매가"))
if release_price_tag:
    sibling = release_price_tag.find_parent().find_next("div")
    if sibling:
        result["release_price"] = re.sub(r"[^\d]", "", sibling.text.strip())

# ✅ current_price
price_tag = soup.select_one(".price .amount")
result["current_price"] = re.sub(r"[^\d]", "", price_tag.text.strip()) if price_tag else None

# ✅ last_trade_price
last_price = soup.find(text=re.compile("최근 거래가"))
if last_price:
    sibling = last_price.find_parent().find_next("div")
    result["last_trade_price"] = re.sub(r"[^\d]", "", sibling.text.strip()) if sibling else None

# ✅ color
color_tag = soup.find(text=re.compile("대표 색상"))
if color_tag:
    sibling = color_tag.find_parent().find_next("div")
    result["color"] = sibling.text.strip() if sibling else None

# ✅ description (없으면 name으로 대체)
desc = soup.select_one("div.detail_section .description")
result["description"] = desc.text.strip() if desc else result.get("name")

# ✅ delivery_info
delivery_tag = soup.find(text=re.compile("배송 정보"))
if delivery_tag:
    delivery_section = delivery_tag.find_parent("div")
    if delivery_section:
        result["delivery_info"] = delivery_section.get_text(strip=True)

# ✅ image_url
image = soup.select_one("picture img")
result["image_url"] = image["src"] if image else None

# ✅ review_score
score_tag = soup.find("div", class_=re.compile("score_area"))
if score_tag:
    score_text = score_tag.get_text()
    match = re.search(r"\d\.\d", score_text)
    if match:
        result["review_score"] = float(match.group())

# ✅ review_count
review_tag = soup.find(text=re.compile("리뷰"))
if review_tag:
    match = re.search(r"\d[\d,]*", review_tag)
    if match:
        result["review_count"] = int(match.group().replace(",", ""))

# ✅ 수집 필드 확인
collected = [k for k, v in result.items() if v]
missing = [k for k, v in result.items() if not v]
print(f"🟢 수집된 필드: {collected}")
print(f"🔴 누락된 필드: {missing}")

# ✅ JSON 저장
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
safe_name = result.get("name", "unknown").replace(" ", "_").replace("/", "_")
json_path = os.path.join(BASE_DIR, f"{safe_name}.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"✅ JSON 저장 완료: {json_path}")

driver.quit()
